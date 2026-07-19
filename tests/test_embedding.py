from resume_parser.resume_loader import ResumeParser
from embeddings.embedding_model import EmbeddingModel

# Resume
resume = ResumeParser.extract_text(
    "data/resumes/updated_resume.pdf"
)

# Job Description
with open(
    "data/job_descriptions/ai_ml_engineer.txt",
    "r",
    encoding="utf-8"
) as file:
    jd = file.read()

model = EmbeddingModel()

score = model.similarity(
    resume,
    jd
)

print("=" * 60)
print(f"Semantic Similarity : {score}%")
print("=" * 60)