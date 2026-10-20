### Q2a: Universities 
# Write your code below:

def get_universities_founded_before(file_name, year):
    with open(file_name, 'r') as university_list:
        filtered_university_list = []
        for university in university_list:
            name_of_a_university, acronym, year_founded, number_of_undergraduate_students = university.split("\t")
            if int(year_founded) < year:
                filtered_university_list.append(name_of_a_university)

    return filtered_university_list
