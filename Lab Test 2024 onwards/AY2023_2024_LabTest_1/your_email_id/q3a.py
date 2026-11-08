# Name:
# Email ID:

def is_partially_compliant(table):
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

    for student in table:
        name, internship_year, school, languages_spoken, skills_practiced = student
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
