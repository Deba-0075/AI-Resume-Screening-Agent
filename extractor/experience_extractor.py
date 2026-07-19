import re


class ExperienceExtractor:
    """
    Extract years of experience and experience-related keywords.
    """

    EXPERIENCE_PATTERNS = [
        r"(\d+)\+?\s+years?",
        r"(\d+)\+?\s+yrs?",
        r"(\d+)\+?\s+year",
        r"(\d+)\+?\s+yr"
    ]

    EXPERIENCE_KEYWORDS = [
        "intern",
        "internship",
        "fresher",
        "developer",
        "engineer",
        "software engineer",
        "ai engineer",
        "ml engineer",
        "data scientist",
        "research assistant",
        "project"
    ]

    @staticmethod
    def extract(text: str):

        text_lower = text.lower()

        years = []

        for pattern in ExperienceExtractor.EXPERIENCE_PATTERNS:
            matches = re.findall(pattern, text_lower)
            years.extend(matches)

        keywords = []

        for keyword in ExperienceExtractor.EXPERIENCE_KEYWORDS:
            if keyword in text_lower:
                keywords.append(keyword)

        max_years = max(map(int, years)) if years else 0

        return {
            "years_of_experience": max_years,
            "keywords": sorted(set(keywords))
        }