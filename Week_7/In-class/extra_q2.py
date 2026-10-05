def find_smallest_diff(my_list):
    smallest_diff = 1000000000000

    for i in range(len(my_list)):
        for j in range(len(my_list)):
            if i != j:
                diff = abs(my_list[i] - my_list[j])
                if diff < smallest_diff:
                    smallest_diff = diff
    return smallest_diff

# Complexity is O(n^2)
# where n is the number of list items

print('Testcase 1')
print('-' * 10)
print('Expected: 1')
my_list = [1, 2, 3, 4]
result = find_smallest_diff(my_list)
print('Actual:   ' + str(result))

print('\nTestcase 2')
print('-' * 10)
print('Expected: 0')
my_list = [1, 3, 1, 4]
result = find_smallest_diff(my_list)
print('Actual:   ' + str(result))

print('\nTestcase 3')
print('-' * 10)
print('Expected: 2')
my_list = [4, 7, 1, 9, 33, 77, 55, 44, 22, 49, 88]
result = find_smallest_diff(my_list)
print('Actual:   ' + str(result))
