### Q5b: Matrix
from q5a import get_matrix
# Write your code below:

def get_matrix_transpose(file_name):
    matrix = get_matrix(file_name)
    transposed_list = []
    for i in range(len(matrix[0])):
        transposed_list.append([])
        for j in range(len(matrix)):
            transposed_list[i].append(matrix[j][i])
    return transposed_list
