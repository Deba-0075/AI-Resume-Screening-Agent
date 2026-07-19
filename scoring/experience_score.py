class ExperienceScorer:

    @staticmethod
    def score(candidate_years, required_years):

        if required_years == 0:
            return 100

        if candidate_years >= required_years:
            return 100

        return round((candidate_years / required_years) * 100, 2)