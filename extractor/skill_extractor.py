import pandas as pd


class SkillExtractor:

    def __init__(self, skill_file="data/skills/technical_skills.csv"):
        df = pd.read_csv(skill_file)
        self.skills = [s.lower() for s in df["skill"].tolist()]

    def extract(self, text):

        text = text.lower()

        found = []

        for skill in self.skills:
            if skill in text:
                found.append(skill)

        return sorted(set(found))