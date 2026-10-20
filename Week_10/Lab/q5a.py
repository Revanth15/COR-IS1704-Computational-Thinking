### Q5a: Matrix

# Write your code below:

def get_matrix(file_name):
    with open(file_name, "r") as matrix_file:
        matrix_list = []
        for row in matrix_file:
            nums = row.strip().split(" ")
            matrix_list.append([])
            for i in range(len(nums)):
                matrix_list[-1].append(float(nums[i]))
    return matrix_list