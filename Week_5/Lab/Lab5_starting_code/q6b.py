### Q6 More on Lists
## b)
# Write your code below:
##############################################################
def get_larger_numbers(num_list1, num_list2):
    new_list = []
    for num1 in num_list1:
        less_than = False
        for num2 in num_list2:
            if num1 < num2:
                less_than = True
        if not less_than:
            new_list.append(num1)
    return new_list







##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

r_list = get_larger_numbers([4, 6, 10], [1, 3, 5])
print("Expected: [6, 10]")
print("Actual  : " + str(r_list))
print()
