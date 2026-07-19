class EducationScorer:

    @staticmethod
    def score(candidate_degrees, jd_degrees):

        candidate = {d.lower() for d in candidate_degrees}
        required = {d.lower() for d in jd_degrees}

        if not required:
            return 100

        return 100 if candidate & required else 0