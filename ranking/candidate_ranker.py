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

            resume_text = ResumeParser.extract_text(str(file))

            contact = ContactExtractor.extract(resume_text)

            skills = self.skill_extractor.extract(resume_text)

            education = self.education_extractor.extract(resume_text)

            experience = ExperienceExtractor.extract(resume_text)

            semantic = self.embedding.similarity(
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
                semantic,
                skill_score,
                experience_score,
                education_score
            )

            candidates.append({

                "candidate": contact["name"],

                "email": contact["email"],

                "phone": contact["phone"],

                "semantic_score": semantic,

                "skill_score": skill_score,

                "education_score": education_score,

                "experience_score": experience_score,

                "final_score": final_score

            })

        candidates = sorted(
            candidates,
            key=lambda x: x["final_score"],
            reverse=True
        )

        for i, candidate in enumerate(candidates, start=1):
            candidate["rank"] = i

        pd.DataFrame(candidates).to_csv(
            "data/output/ranked_candidates.csv",
            index=False
        )

        with open(
            "data/output/ranked_candidates.json",
            "w"
        ) as file:
            json.dump(candidates, file, indent=4)

        return candidates