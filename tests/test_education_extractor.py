from resume_parser.resume_loader import ResumeParser
from extractor.education_extractor import EducationExtractor

resume = ResumeParser.extract_text(
    "data/resumes/updated_resume.pdf"
)

extractor = EducationExtractor()

education = extractor.extract(resume)

print("=" * 60)
print(education)
print("=" * 60)