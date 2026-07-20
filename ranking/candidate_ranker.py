from pathlib import Path
import json
import pandas as pd

from resume_parser.resume_loader import ResumeParser
from resume_parser.jd_loader import JDParser

from extractor.contact_extractor import ContactExtractor
from extractor.skill_extractor import SkillExtractor
from extractor.education_extractor import EducationExtractor
from extractor.experience_extractor import ExperienceExtractor

from embeddings.embedding_model import EmbeddingModel

from scoring.skill_match import SkillMatcher
from scoring.education_score import EducationScorer
from scoring.experience_score import ExperienceScorer
from scoring.final_score import FinalScorer


class CandidateRanker:

    def __init__(self):

        self.embedding = EmbeddingModel()
        self.skill_extractor = SkillExtractor()
        self.education_extractor = EducationExtractor()

    def rank_all(self, resume_folder, jd_text):

        jd = JDParser().parse(jd_text)

        candidates = []

        for file in Path(resume_folder).iterdir():

            if file.suffix.lower() not in [".pdf", ".docx", ".txt"]:
                continue

            # -------------------------
            # Resume Parsing
            # -------------------------

            resume_text = ResumeParser.extract_text(str(file))

            contact = ContactExtractor.extract(resume_text)

            skills = self.skill_extractor.extract(resume_text)

            education = self.education_extractor.extract(resume_text)

            experience = ExperienceExtractor.extract(resume_text)

            # -------------------------
            # Matching
            # -------------------------

            matched_skills = sorted(
                list(set(skills) & set(jd["skills"]))
            )

            missing_skills = sorted(
                list(set(jd["skills"]) - set(skills))
            )

            # -------------------------
            # Scores
            # -------------------------

            semantic_score = self.embedding.similarity(
                resume_text,
                jd_text
            )

            skill_score = SkillMatcher.score(
                skills,
                jd["skills"]
            )

            education_score = EducationScorer.score(
                education["degrees"],
                jd["degrees"]
            )

            experience_score = ExperienceScorer.score(
                experience["years_of_experience"],
                jd["required_experience"]
            )

            final_score = FinalScorer.calculate(
                semantic_score,
                skill_score,
                experience_score,
                education_score
            )

            # -------------------------
            # Recommendation
            # -------------------------

            if final_score >= 85:
                recommendation = "🟢 Highly Recommended"

            elif final_score >= 70:
                recommendation = "🟢 Recommended"

            elif final_score >= 50:
                recommendation = "🟡 Consider"

            else:
                recommendation = "🔴 Not Recommended"

            # -------------------------
            # Candidate Data
            # -------------------------

            candidates.append({

                "rank": 0,

                "resume_file": file.name,

                "candidate": contact["name"] if contact["name"] else "Unknown Candidate",

                "email": contact["email"] if contact["email"] else "Not Available",

                "phone": contact["phone"] if contact["phone"] else "Not Available",

                "matched_skills": ", ".join(matched_skills),

                "missing_skills": ", ".join(missing_skills),

                "semantic_score": round(semantic_score, 2),

                "skill_score": round(skill_score, 2),

                "education_score": round(education_score, 2),

                "experience_score": round(experience_score, 2),

                "final_score": round(final_score, 2),

                "recommendation": recommendation

            })

        # -------------------------
        # Sort by Final Score
        # -------------------------

        candidates = sorted(
            candidates,
            key=lambda x: x["final_score"],
            reverse=True
        )

        # -------------------------
        # Assign Rank
        # -------------------------

        for i, candidate in enumerate(candidates, start=1):
            candidate["rank"] = i

        # -------------------------
        # Save Results
        # -------------------------

        df = pd.DataFrame(candidates)

        df.to_csv(
            "data/output/ranked_candidates.csv",
            index=False
        )

        with open(
            "data/output/ranked_candidates.json",
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                candidates,
                file,
                indent=4,
                ensure_ascii=False
            )

        return candidates