def check_age(student_list):
    # Modify the code below.
    for stu in student_list:
        name, gender, age = stu
        if gender == "M" and int(age) <= 20:
            return False
    return True
   
