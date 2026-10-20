with open("grades.txt", "r") as grade_list:
    student_name_list = []
    course_term_name_list = []
    for row in grade_list:
        name, course, year, grade = row.rstrip().split("#")
        if name not in student_name_list:
            student_name_list.append(name)
            course_term_name_list.append([course+year])
        else:
            index = student_name_list.index(name)
            course_term_name_list[index].append(course+year)

    student_pairs = set()
    # Set comparision
    for i in range(len(student_name_list)):
        for j in range(i + 1, len(student_name_list)):
            if len(list(set(course_term_name_list[i]) & set(course_term_name_list[j]))) != 0:
                student_pairs.add((student_name_list[i], student_name_list[j]))

    for pair in student_pairs:
        print(pair)