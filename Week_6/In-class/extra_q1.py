def sort_strings(inp_list):
    sorted_list = []
    for str in inp_list:
        inserted = False
        for i in range(len(sorted_list)):
            if len(sorted_list[i]) > len(str):
                sorted_list = sorted_list[0:i] + [str] + sorted_list[i:]
                inserted = True
                break
        if not inserted:
            sorted_list.append(str)
    return sorted_list

print('Testcase 1')
print('-' * 10)

print("Expected: ['a', 'x', 'xy', '12', 'abc']")
str_list = ['abc', 'a', 'xy', '12', 'x']

result = sort_strings(str_list)

print('Actual:   ' + str(result))


print('\nTestcase 2')
print('-' * 10)

print("Expected: ['a', 'bb', 'ccc', 'dddd']")
str_list = ['dddd', 'ccc', 'bb', 'a']

result = sort_strings(str_list)

print('Actual:   ' + str(result))


print('\nTestcase 3')
print('-' * 10)

print("Expected: ['ab', 'cd', 'ef', 'gh']")
str_list = ['ab', 'cd', 'ef', 'gh']

result = sort_strings(str_list)

print('Actual:   ' + str(result))


print('\nTestcase 4')
print('-' * 10)

print("Expected: ['b', 'e', 'dd', 'ff', 'aaa', 'ccc']")
str_list = ['aaa', 'b', 'ccc', 'dd', 'e', 'ff']

result = sort_strings(str_list)

print('Actual:   ' + str(result))


print('\nTestcase 5')
print('-' * 10)

print("Expected: ['hello']")
str_list = ['hello']

result = sort_strings(str_list)

print('Actual:   ' + str(result))


print('\nTestcase 6')
print('-' * 10)

print("Expected: []")
str_list = []

result = sort_strings(str_list)

print('Actual:   ' + str(result))


print('\nTestcase 7')
print('-' * 10)

print("Expected: ['a', 'bb', 'ccc', 'dddd', 'eeeee']")
str_list = ['a', 'bb', 'ccc', 'dddd', 'eeeee']

result = sort_strings(str_list)

print('Actual:   ' + str(result))


print('\nTestcase 8')
print('-' * 10)

print("Expected: ['x', 'a', 'yy', 'bb', 'ccc', 'ddd']")
str_list = ['ccc', 'x', 'yy', 'a', 'ddd', 'bb']

result = sort_strings(str_list)

print('Actual:   ' + str(result))