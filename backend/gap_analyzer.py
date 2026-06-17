def analyze_gap(resume_skills, job_skills):

    resume_set = set(skill.lower() for skill in resume_skills)
    job_set = set(skill.lower() for skill in job_skills)

    matching_skills = list(resume_set & job_set)
    missing_skills = list(job_set - resume_set)

    match_percentage = (
        len(matching_skills) / len(job_set) * 100
        if job_set else 0
    )

    return {
        "match_percentage": round(match_percentage, 2),
        "matching_skills": matching_skills,
        "missing_skills": missing_skills
    }


if __name__ == "__main__":

    resume_skills = [
        "Python",
        "Java",
        "Git"
    ]

    job_skills = [
        "Python",
        "Git",
        "SQL",
        "Docker"
    ]

    result = analyze_gap(resume_skills, job_skills)

    print(result)