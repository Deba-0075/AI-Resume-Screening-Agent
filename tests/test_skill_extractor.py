from resume_parser.resume_loader import ResumeParser
from extractor.skill_extractor import SkillExtractor

resume = ResumeParser.extract_text(
    "data/resumes/updated_resume.pdf"
)

extractor = SkillExtractor()

skills = extractor.extract(resume)

print("=" * 60)

print("Detected Skills")

print("=" * 60)

for skill in skills:
    print(skill)

print("=" * 60)