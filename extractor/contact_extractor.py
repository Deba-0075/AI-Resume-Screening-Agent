import re


class ContactExtractor:
    """
    Extract contact information from resume text.
    """

    EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    PHONE_PATTERN = r"(?:\+91[\s-]?)?[6-9]\d{9}"
    LINKEDIN_PATTERN = r"(https?://)?(www\.)?linkedin\.com/in/[^\s|]+"
    GITHUB_PATTERN = r"(https?://)?(www\.)?github\.com/[^\s|]+"

    @staticmethod
    def extract(text: str) -> dict:

        lines = [line.strip() for line in text.split("\n") if line.strip()]

        name = lines[0] if lines else ""

        email = ""
        phone = ""
        linkedin = ""
        github = ""

        email_match = re.search(ContactExtractor.EMAIL_PATTERN, text)
        if email_match:
            email = email_match.group()

        phone_match = re.search(ContactExtractor.PHONE_PATTERN, text)
        if phone_match:
            phone = phone_match.group()

        linkedin_match = re.search(ContactExtractor.LINKEDIN_PATTERN, text, re.IGNORECASE)
        if linkedin_match:
            linkedin = linkedin_match.group()

        github_match = re.search(ContactExtractor.GITHUB_PATTERN, text, re.IGNORECASE)
        if github_match:
            github = github_match.group()

        return {
            "name": name,
            "email": email,
            "phone": phone,
            "linkedin": linkedin,
            "github": github,
        }