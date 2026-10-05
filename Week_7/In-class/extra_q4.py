def get_largest_numbers(my_list):
    first_10 = my_list[:10]
    rest = my_list[10:]
    for elem in rest:
        for i in range(len(first_10)):
            if elem > first_10[i]:
                first_10[i] = elem
                break

    first_10.sort()
    return first_10


print('Testcase 1')
print('-' * 10)
print('Expected: [8, 9, 10, 12, 22, 32, 40, 44, 51, 100]')
my_list = [12, 5, 100, -1, 8, 22, 9, 44, 51, 32, 7, 10, 2, 40]
result = get_largest_numbers(my_list)
print('Actual:   ' + str(result))

print('\nTestcase 2')
print('-' * 10)
print('Expected: [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]')
my_list = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 0, -1]
result = get_largest_numbers(my_list)
print('Actual:   ' + str(result))
