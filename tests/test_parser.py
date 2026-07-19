from resume_parser.resume_loader import ResumeParser

resume = ResumeParser.extract_text(
    r"data\resumes\updated_resume.pdf"
)

print("=" * 80)
print(resume[:3000])
print("=" * 80)