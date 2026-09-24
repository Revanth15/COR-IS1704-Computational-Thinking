from extra_q2a import get_matrix_transpose

"""
For example
matrix1 = [
    [1.0, 2.0, -1.0],
    [2.5, 1.5, 0.5]
]
matrix2 = [
    [2.0, 2.0],
    [1.5, 1.0],
    [0.5, 2.0]
]

Matrix 1 is 2 rows of 3 columns.
Matrix 2 is 3 rows of 2 columns.

Take each value of Matrix 1 row 1 and multiply them by the values in Matrix 2 column 1. (We can transpose to modify them)
so it should look like this
1.0 x 2.0 + 2.0 x 1.5 + -1.0 x 0.5 == 4.5
1.0 x 2.0 + 2.0 x 1.0 + -1.0 x 2 == 2.0

so row 1 of the calculated matrix is [4.5, 2.0]

transposed_matrix2 = [
    [2.0, 1.5, 0.5],
    [2.0, 1.0, 2.0]
]

"""

def multiply_matrices(matrix1, matrix2):
    # Write your solution here.
    transposed_matrix2 = get_matrix_transpose(matrix2)
    calculated_matrix = []
    for row_index in range(len(matrix1)):
        calculated_matrix.append([])
        for column_index in range(len(transposed_matrix2)):
            tally = 0
            for element_index in range(len(transposed_matrix2[0])):
                tally += matrix1[row_index][element_index] * transposed_matrix2[column_index][element_index]
            calculated_matrix[row_index].append(tally)
    return calculated_matrix

print('Testcase 1 - example from the question')
print('-' * 10)

matrix1 = [
    [1.0, 2.0, -1.0],
    [2.5, 1.5, 0.5]
]
matrix2 = [
    [2.0, 2.0],
    [1.5, 1.0],
    [0.5, 2.0]
]

print('Expected: [[4.5, 2.0], [7.5, 7.5]]')
print('Actual:   ' + str(multiply_matrices(matrix1, matrix2)))


print('\nTestcase 2 - rectangular matrices')
print('-' * 10)

matrix1 = [
    [1, 2],
    [3, 4],
    [5, 6]
]
matrix2 = [
    [7, 8, 9, 10],
    [11, 12, 13, 14]
]

print('Expected: [[29, 32, 35, 38], [65, 72, 79, 86], [101, 112, 123, 134]]')
print('Actual:   ' + str(multiply_matrices(matrix1, matrix2)))


print('\nTestcase 3 - multiplying by an identity matrix')
print('-' * 10)

matrix1 = [
    [1, 2],
    [3, 4]
]
matrix2 = [
    [1, 0],
    [0, 1]
]

print('Expected: [[1, 2], [3, 4]]')
print('Actual:   ' + str(multiply_matrices(matrix1, matrix2)))


print('\nTestcase 4 - one row multiplied by one column')
print('-' * 10)

matrix1 = [[-2, 0, 3]]
matrix2 = [
    [4],
    [5],
    [-1]
]

print('Expected: [[-11]]')
print('Actual:   ' + str(multiply_matrices(matrix1, matrix2)))
