### Q2c: Universities 
# Write your code below:

def search_with_keyword(file_name, keyword):
    with open(file_name, 'r') as university_list:
        matched_list = []
        for university in university_list:
            name_of_a_university, acronym, year_founded, number_of_undergraduate_students = university.split("\t")
            if keyword.lower() in name_of_a_university.lower():
                matched_list.append(acronym)
    return matched_list