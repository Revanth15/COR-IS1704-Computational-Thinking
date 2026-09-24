def get_matrix_transpose(lists):
    no_of_rows = len(lists)
    transposed_list = []
    for i in range(len(lists[0])):
        transposed_list.append([])
        for j in range(no_of_rows):
            transposed_list[i].append(lists[j][i])
    return transposed_list

# print('Testcase 1')
# print('-' * 10)

# print('Expected: [[1.0, 2.5, 4.5], [2.0, 3.0, 1.5], [1.5, 2.0, 2.5]]')

# matrix = [
#     [1.0, 2.0, 1.5],
#     [2.5, 3.0, 2.0],
#     [4.5, 1.5, 2.5]
# ]

# result = get_matrix_transpose(matrix)

# print('Actual:   ' + str(result))


# print('\nTestcase 2')
# print('-' * 10)

# print('Expected: [[1.0, 2.5, 4.5], [2.0, 3.0, 1.5]]')

# matrix = [
#     [1.0, 2.0],
#     [2.5, 3.0],
#     [4.5, 1.5]
# ]

# result = get_matrix_transpose(matrix)

# print('Actual:   ' + str(result))


# print('\nTestcase 3')
# print('-' * 10)

# print('Expected: [[1, 4], [2, 5], [3, 6]]')

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# result = get_matrix_transpose(matrix)

# print('Actual:   ' + str(result))


# print('\nTestcase 4')
# print('-' * 10)

# print('Expected: [[1, 2, 3, 4]]')

# matrix = [
#     [1],
#     [2],
#     [3],
#     [4]
# ]

# result = get_matrix_transpose(matrix)

# print('Actual:   ' + str(result))


# print('\nTestcase 5')
# print('-' * 10)

# print('Expected: [[1], [2], [3], [4]]')

# matrix = [
#     [1, 2, 3, 4]
# ]

# result = get_matrix_transpose(matrix)

# print('Actual:   ' + str(result))


# print('\nTestcase 6')
# print('-' * 10)

# print('Expected: [[5]]')

# matrix = [
#     [5]
# ]

# result = get_matrix_transpose(matrix)

# print('Actual:   ' + str(result))


# print('\nTestcase 7')
# print('-' * 10)

# print("Expected: [['a', 'c'], ['b', 'd']]")

# matrix = [
#     ['a', 'b'],
#     ['c', 'd']
# ]

# result = get_matrix_transpose(matrix)

# print('Actual:   ' + str(result))


# print('\nTestcase 8')
# print('-' * 10)

# print('Expected: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]')

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]

# result = get_matrix_transpose(matrix)

# print('Actual:   ' + str(result))