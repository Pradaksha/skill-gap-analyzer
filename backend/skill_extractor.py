import pandas as pd

def extract_skills(text, skills_file="data/skills.csv"):
    skills_df = pd.read_csv(skills_file, header=None)

    skills_list = skills_df[0].str.lower().tolist()

    text = text.lower()

    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills


if __name__ == "__main__":
    sample_text = """
    Python Java Machine Learning Git HTML CSS
    """

    skills = extract_skills(sample_text)

    print("Extracted Skills:")
    print(skills)