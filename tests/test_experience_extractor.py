from resume_parser.resume_loader import ResumeParser
from extractor.experience_extractor import ExperienceExtractor

resume = ResumeParser.extract_text(
    "data/resumes/updated_resume.pdf"
)

experience = ExperienceExtractor.extract(resume)

print("=" * 60)
print(experience)
print("=" * 60)