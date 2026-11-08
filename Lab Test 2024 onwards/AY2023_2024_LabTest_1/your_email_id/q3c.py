# Name:
# Email ID:

from q3b import is_fully_compliant

def make_tables_fully_compliant(t1, t2):
    # Replace the code below with your implementation.

    # Loop through and check each possibility
    for i in range(len(t1)):
        for j in range(len(t2)):
            t1_student = t1[i]
            t2_student = t2[j]

            new_table1 = t1[:]
            new_table2 = t2[:]

            new_table1[i] = t2_student
            new_table2[j] = t1_student

            compliant1_bool = is_fully_compliant(new_table1)
            compliant2_bool = is_fully_compliant(new_table2)

            if compliant1_bool and compliant2_bool:
                return ((t1_student[0], t2_student[0]), new_table1, new_table2)

    return "not possible"




# import json

# def make_tables_fully_compliant(t1, t2):
#     # Replace the code below with your implementation.
#     school_mapping = {
#         "scis" : 0,
#         "bus" : 0,
#         "sosc" : 0,
#         "law" : 0,
#         "acc" : 0,
#         "eco" : 0,
#     }
#     internship_years = []
#     internship_baseline = []

#     empty_mapping = {
#         "internship_baseline" : [],
#         "odd_student" : []
#     }

#     mapping = {}
#     counter = 1
#     for table in [t1,t2]:
#         previous_student = table[-1]
#         mapping[counter] = empty_mapping.copy()

#         for student in table:
#             _, internship_year, school, languages_spoken, skills_practiced = student
#             _, _, _, prev_stud_languages_spoken, prev_stud_skills_practiced = previous_student

#             common_languages = set(languages_spoken).intersection(set(prev_stud_languages_spoken))
#             common_skills = set(skills_practiced).intersection(set(prev_stud_skills_practiced))
#             if len(common_languages) == 0 or len(common_skills) > 2:
#                 mapping[counter]["odd_student"].append(student)

#             previous_student = student

#             if school in school_mapping:
#                 if school_mapping[school] == 2:
#                     mapping[counter]["odd_student"].append(student)
#                 else:   
#                     school_mapping[school] += 1

#             if len(mapping[counter]["internship_baseline"]) == 0:
#                 mapping[counter]["internship_baseline"].append(internship_year)
#                 mapping[counter]["internship_baseline"].append(internship_year-1)
#                 mapping[counter]["internship_baseline"].append(internship_year+1)

#             if internship_year not in mapping[counter]["internship_baseline"]:
#                 mapping[counter]["odd_student"].append(student)
#         counter += 1
#         school_mapping = {
#             "scis" : 0,
#             "bus" : 0,
#             "sosc" : 0,
#             "law" : 0,
#             "acc" : 0,
#             "eco" : 0,
#         }

#     # if len(mapping[counter - 1]["odd_student"]) > 1:
#     #     return "not possible"
    
#     print(json.dumps(mapping, indent=5))
        
#     return (0,t1,t2)
    