from ranking.candidate_ranker import CandidateRanker

with open(
    "data/job_descriptions/ai_ml_engineer.txt",
    "r",
    encoding="utf-8"
) as file:
    jd = file.read()

ranker = CandidateRanker()

results = ranker.rank_all(
    "data/resumes",
    jd
)

for candidate in results:
    print(candidate)