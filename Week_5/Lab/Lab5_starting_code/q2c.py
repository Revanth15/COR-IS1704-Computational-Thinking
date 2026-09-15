### Q2 List of Numbers
## c)
# Write your code below:
##############################################################
def get_sum_of_multiples(int_list, n):
    sum = 0
    for int in int_list:
        if int % n == 0:
            sum += int
    return sum



##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

print('Test Case 1')
print('-' * 11)
print('Expected: 24')
print('Actual:   ' + str(get_sum_of_multiples([2, 4, 5, 9, 13, 15], 3)))

print('\nTest Case 2')
print('-' * 11)
print('Expected: 20')
print('Actual:   ' + str(get_sum_of_multiples([2, 4, 5, 9, 13, 15], 5)))
