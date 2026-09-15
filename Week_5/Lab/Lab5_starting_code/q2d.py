### Q2 List of Numbers
## d)
# Write your code below:
##############################################################
def get_prime_numbers(num_list, sep):
    list = []
    for num in num_list:
        if num <= 1:
            pass
        else:
            prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    prime = False
                    break
            if prime:
                list.append(str(num))
    return f"{sep}".join(list)






##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

print('Test Case 1')
print('-' * 11)
print('Expected: 2-7-11-19')
print('Actual:   ' + str(get_prime_numbers([2, 4, 7, 9, 11, 16, 19, 21], '-')))

print('\nTest Case 2')
print('-' * 11)
print('Expected: 3')
print('Actual:   ' + str(get_prime_numbers([3, 4, 8, 9, 12, 16], '*')))
