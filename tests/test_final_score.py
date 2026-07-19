from scoring.final_score import FinalScorer

score = FinalScorer.calculate(
    semantic_score=40,
    skill_score=85,
    experience_score=100,
    education_score=100
)

print("=" * 60)
print("Final Score:", score)
print("=" * 60)