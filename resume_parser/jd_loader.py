import re
import pandas as pd


class JDParser:
    """
    Parse Job Description and extract:
    - Skills
    - Degrees
    - Experience
    """

    def __init__(
        self,
        skill_file="data/skills/technical_skills.csv",
        degree_file="data/skills/degree_keywords.csv",
    ):
        self.skills = pd.read_csv(skill_file)["skill"].tolist()
        self.degrees = pd.read_csv(degree_file)["degree"].tolist()

    def parse(self, jd_text: str) -> dict:

        jd_text_lower = jd_text.lower()

        # -------------------------
        # Extract Skills
        # -------------------------
        found_skills = []

        for skill in self.skills:
            if skill.lower() in jd_text_lower:
                found_skills.append(skill)

        # -------------------------
        # Extract Degrees
        # -------------------------
        found_degrees = []

        for degree in self.degrees:
            if degree.lower() in jd_text_lower:
                found_degrees.append(degree)

        # -------------------------
        # Extract Experience
        # -------------------------
        experience = re.findall(
            r"(\d+)\+?\s*(?:years?|yrs?)",
            jd_text_lower
        )

        experience = [int(x) for x in experience]

        required_experience = max(experience) if experience else 0

        # -------------------------
        # Return Parsed Data
        # -------------------------
        return {
            "skills": sorted(set(found_skills)),
            "degrees": sorted(set(found_degrees)),
            "required_experience": required_experience
        }