def flatten(my_list):
    # Write your solution here.
    computed_list = []
    for i in range(len(my_list)):
        obj = my_list[i]
        if isinstance(obj, list):
            val = flatten(obj)
            computed_list += val
        else:
            computed_list.append(obj)
    return computed_list


print('Testcase 1 - example from the question')
print('-' * 10)

my_list = [4, 39, [35, 12, [45], 32], 4, [35, [4, [6]]]]

print('Expected: [4, 39, 35, 12, 45, 32, 4, 35, 4, 6]')
print('Actual:   ' + str(flatten(my_list)))


print('\nTestcase 2 - a list with no nested lists')
print('-' * 10)

my_list = [3, -2, 0, 5.5]

print('Expected: [3, -2, 0, 5.5]')
print('Actual:   ' + str(flatten(my_list)))


print('\nTestcase 3 - empty lists at different depths')
print('-' * 10)

my_list = [[], [1, [], [2, []]], []]

print('Expected: [1, 2]')
print('Actual:   ' + str(flatten(my_list)))


print('\nTestcase 4 - an empty input list')
print('-' * 10)

my_list = []

print('Expected: []')
print('Actual:   ' + str(flatten(my_list)))


print('\nTestcase 5 - deeply nested single values')
print('-' * 10)

my_list = [[[[7]]], [[-3]], 2]

print('Expected: [7, -3, 2]')
print('Actual:   ' + str(flatten(my_list)))
