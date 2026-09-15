### Q2 List of Numbers
## e)
# Write your code below:
##############################################################
def calculate_sums(num_list):
    new_list = []
    for i in range(len(num_list)):
        num = 0
        for j in range(i+1,0, -1):
            num += num_list[j - 1]
        new_list.append(num)
    return new_list






##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

print('Test Case 1')
print('-' * 11)
print('Expected: [2, 5, 11, 12, 17]')
print('Actual:   ' + str(calculate_sums([2, 3, 6, 1, 5])))

print('\nTest Case 2')
print('-' * 11)
print('Expected: []')
print('Actual:   ' + str(calculate_sums([])))