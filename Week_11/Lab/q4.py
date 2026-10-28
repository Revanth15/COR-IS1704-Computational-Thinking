## Q4 Students and Schools
# write your code below

def get_students_by_school(my_dict):
    reformatted_dict = {}

    for item in my_dict:
        if my_dict[item] not in reformatted_dict:
            reformatted_dict[my_dict[item]] = []
        reformatted_dict[my_dict[item]].append(item)

    return reformatted_dict