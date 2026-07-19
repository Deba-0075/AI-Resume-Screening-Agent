from resume_parser.jd_loader import JDParser

with open(
    "data/job_descriptions/ai_ml_engineer.txt",
    "r",
    encoding="utf-8"
) as file:
    jd_text = file.read()

parser = JDParser()

result = parser.parse(jd_text)

print("=" * 60)
print(result)
print("=" * 60)