class SkillMatcher:

    @staticmethod
    def score(resume_skills, jd_skills):

        if not jd_skills:
            return 100

        matched = set(skill.lower() for skill in resume_skills) & \
                  set(skill.lower() for skill in jd_skills)

        return round((len(matched) / len(jd_skills)) * 100, 2)