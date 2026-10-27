def display_all_gpas(dict):
    print("Student Name\tStudent GPA")
    print('_' * len("Student Name") + "\t" + '_' * len("Student GPA"))
    for student in dict.items():
        print(f"{student[0]}\t{student[1]}")

dict = {'George Leung':3.4, 'Eric Wong':3.9, 'Michelle Lee':3.1}

# display_all_gpas(dict)