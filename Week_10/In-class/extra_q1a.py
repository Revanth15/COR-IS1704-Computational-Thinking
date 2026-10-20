with open("grades.txt", "r") as grade_list:
    coursename_list = []
    student_name_list = []
    for row in grade_list:
        name, course, year, grade = row.rstrip().split("#")
        if course not in coursename_list:
            coursename_list.append(course)
            if grade == "A":
                student_name_list.append([name])
            else:
                student_name_list.append([])
        else:
            index = coursename_list.index(course)
            if grade == "A":
                student_name_list[index].append(name)

    with open("course_info.txt", 'w') as reorg_grades:
        for i in range(len(coursename_list)):
            if student_name_list[i] != []:
                reorg_grades.write(f"{coursename_list[i]}\n{("\n").join(student_name_list[i])}\n\n")
