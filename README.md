# 🤖 AI Resume Screening Agent

An AI-powered Resume Screening Agent that automates the recruitment process by analyzing multiple resumes, comparing them with a Job Description (JD), and ranking candidates using Natural Language Processing (NLP), semantic similarity, and hybrid scoring techniques.

The system supports multiple resume formats and generates ranked candidate reports in CSV and JSON formats.

---

# 🚀 Features

### 📄 Resume Parsing
- PDF (.pdf)
- Microsoft Word (.docx)
- Plain Text (.txt)

### 👤 Candidate Information Extraction
- Name
- Email
- Phone Number

### 🧠 Resume Analysis
- Skill Extraction
- Education Extraction
- Experience Extraction

### 📋 Job Description Analysis
- Required Skills
- Required Education
- Required Experience

### 🤖 AI-Based Matching
- Sentence Transformer Embeddings
- Semantic Similarity
- Hybrid Candidate Scoring

### 📊 Candidate Ranking
- Multi-Resume Screening
- Automatic Ranking
- CSV Export
- JSON Export

---

# 🛠 Technology Stack

### Programming Language
- Python 3.10

### AI / Machine Learning
- Sentence Transformers
- PyTorch
- spaCy
- Scikit-learn

### Data Processing
- Pandas
- NumPy

### Resume Parsing
- PyMuPDF
- python-docx

---

# 📂 Project Structure

```
Resume_Screening_Agent/
│
├── data/
│   ├── resumes/
│   ├── job_descriptions/
│   ├── skills/
│   └── output/
│
├── resume_parser/
├── extractor/
├── embeddings/
├── scoring/
├── ranking/
├── tests/
│
├── config.py
├── requirements.txt
└── README.md
```

---

# 🔄 Workflow

```
                  Job Description
                         │
                         ▼
                 Parse Job Description
                         │
                         ▼
                Load Candidate Resume
                         │
                         ▼
            Extract Candidate Information
                         │
                         ▼
              Generate Text Embeddings
                         │
                         ▼
              Calculate Similarity Score
                         │
                         ▼
              Compute Hybrid Score
                         │
                         ▼
             Rank All Candidates
                         │
                         ▼
            Export CSV & JSON Reports
```

---

# 📊 Scoring Strategy

The final candidate score is calculated using a weighted hybrid approach.

| Component | Weight |
|-----------|-------:|
| Semantic Similarity | 50% |
| Skill Matching | 30% |
| Education Matching | 10% |
| Experience Matching | 10% |

---

# 📥 Input

### Resume Formats
- PDF (.pdf)
- DOCX (.docx)
- TXT (.txt)

### Job Description
- TXT (.txt)

---

# 📤 Output

The system generates:

- Ranked Candidate List
- CSV Report
- JSON Report

### Sample Output

| Rank | Candidate | Final Score |
|------|-----------|------------:|
| 1 | Candidate A | 91.45 |
| 2 | Candidate B | 87.32 |
| 3 | Candidate C | 79.18 |

---

# ▶️ Installation

## Clone Repository

```bash
git clone https://github.com/Deba-0075/AI-Resume-Screening-Agent.git
```

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate Environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

```bash
python -m tests.test_ranker
```

---

# 📈 Future Enhancements

- Streamlit Dashboard
- OCR Support for Scanned Resumes
- LLM-powered Resume Analysis
- Recommendation Labels
- Interview Question Generation
- Candidate Analytics Dashboard
- Database Integration

---

# 👨‍💻 Author

**Debabrata Sahu**

Computer Science Engineer | AI/ML & Computer Vision Enthusiast

GitHub: https://github.com/Deba-0075

LinkedIn: https://www.linkedin.com/in/debabrata-sahu-293ba0304