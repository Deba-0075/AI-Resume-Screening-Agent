from resume_parser.resume_loader import ResumeParser
from extractor.contact_extractor import ContactExtractor

resume_text = ResumeParser.extract_text(
    "data/resumes/updated_resume.pdf"
)

contact = ContactExtractor.extract(resume_text)

print("=" * 50)
for key, value in contact.items():
    print(f"{key:10}: {value}")
print("=" * 50)