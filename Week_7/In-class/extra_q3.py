def find_students(names):
    last_names = []
    students = []
    for student in names:
        if student[1] not in last_names:
            students.append(student)
            last_names.append(student[1])
    return students

# Complexity is O(1)


print('Testcase 1')
print('-' * 10)
print('Expected: [(\'James\', \'Wong\'), (\'Lily\', \'Khoo\'), (\'George\', \'Lim\')]')
names = [('James', 'Wong'), ('Lily', 'Khoo'), ('Peter', 'Wong'), ('George', 'Lim')]
result = find_students(names)
print('Actual:   ' + str(result))

print('\nTestcase 2')
print('-' * 10)
print('Expected: [(\'James\', \'Wong\'), (\'George\', \'Lim\')]')
names = [('James', 'Wong'), ('Lily', 'Wong'), ('Peter', 'Wong'), ('George', 'Lim')]
result = find_students(names)
print('Actual:   ' + str(result))

print('\nTestcase 3')
print('-' * 10)
print('Expected: []')
names = []
result = find_students(names)
print('Actual:   ' + str(result))
