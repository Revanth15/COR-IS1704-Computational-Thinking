### Q2b: Universities 
# Write your code below:

def get_average_num_students(file_name,):
    with open(file_name, 'r') as university_list:
        university_pop_num = 0
        counter = 0
        for university in university_list:
            name_of_a_university, acronym, year_founded, number_of_undergraduate_students = university.split("\t")
            university_pop_num += int(number_of_undergraduate_students)
            counter += 1
        average_num_students = university_pop_num/ counter
    return average_num_students

