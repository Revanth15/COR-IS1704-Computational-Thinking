# Name:
# Email ID:

from q3a import is_partially_compliant

def is_fully_compliant(table):
    # Replace the code below with your implementation.
    school_mapping = {
        "scis" : 0,
        "bus" : 0,
        "sosc" : 0,
        "law" : 0,
        "acc" : 0,
        "eco" : 0,
    }

    internship_years = []
    internship_baseline = []
    previous_student = table[-1]
    for student in table:
        name, internship_year, school, languages_spoken, skills_practiced = student
        prev_stud_name, prev_stud_internship_year, prev_stud_school, prev_stud_languages_spoken, prev_stud_skills_practiced = previous_student

        common_languages = set(languages_spoken).intersection(set(prev_stud_languages_spoken))
        common_skills = set(skills_practiced).intersection(set(prev_stud_skills_practiced))
        if len(common_languages) == 0 or len(common_skills) > 2:
            return False

        previous_student = student

        if school in school_mapping:
            school_mapping[school] += 1

        internship_years.append(internship_year)
        if len(internship_baseline) == 0:
            internship_baseline.append(internship_year)
            internship_baseline.append(internship_year-1)
            internship_baseline.append(internship_year+1)

        if internship_year not in internship_baseline:
            return False
        

    if max(school_mapping.values()) > 2:
        return False

    # print(school_mapping)
    # print(internship_years)
    return True