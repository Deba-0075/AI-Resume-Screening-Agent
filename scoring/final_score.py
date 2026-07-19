class FinalScorer:

    @staticmethod
    def calculate(
        semantic_score,
        skill_score,
        experience_score,
        education_score
    ):

        final_score = (
            semantic_score * 0.50 +
            skill_score * 0.30 +
            experience_score * 0.10 +
            education_score * 0.10
        )

        return round(final_score, 2)