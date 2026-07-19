from pathlib import Path

# ===================================
# Project Paths
# ===================================

PROJECT_ROOT = Path(__file__).resolve().parent

DATA_DIR = PROJECT_ROOT / "data"

RESUME_DIR = DATA_DIR / "resumes"

JD_DIR = DATA_DIR / "job_descriptions"

SKILL_DIR = DATA_DIR / "skills"

OUTPUT_DIR = DATA_DIR / "output"

# ===================================
# AI Model
# ===================================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ===================================
# Supported Formats
# ===================================

SUPPORTED_RESUME_FORMATS = [
    ".pdf",
    ".docx",
    ".txt"
]