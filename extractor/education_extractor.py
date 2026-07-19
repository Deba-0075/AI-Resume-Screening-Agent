import re
import pandas as pd


class EducationExtractor:

    def __init__(self, degree_file="data/skills/degree_keywords.csv"):
        df = pd.read_csv(degree_file)
        self.degrees = df["degree"].tolist()

    def extract(self, text):

        education = []

        for degree in self.degrees:
            if degree.lower() in text.lower():
                education.append(degree)

        years = re.findall(r"\b(?:19|20)\d{2}\b", text)

        return {
            "degrees": sorted(set(education)),
            "years": sorted(set(years))
        }