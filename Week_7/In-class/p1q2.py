
def find_students(students, criteria, criteria_indices):
    students_list = []
    for student in students:
        valid = True
        for i in range(len(criteria_indices)):
            if student[criteria_indices[i]] != criteria[i]:
                valid = False
                break
        if valid:
            students_list.append(student)
    return students_list


students = [
["Alice", 20, "A"],
["Bob", 22, "B"],
["Charlie", 20, "A"],
["David", 23, "C"]
]
criteria = ["A", 20]
criteria_indices = [2, 1]
print(find_students(students, criteria, criteria_indices))
print([['Alice', 20,'A'], ['Charlie', 20, 'A']])

criteria = [20]
criteria_indices = [1] # Index corresponding to age
print(find_students(students, criteria, criteria_indices))
print([['Alice', 20,'A'], ['Charlie', 20, 'A']])