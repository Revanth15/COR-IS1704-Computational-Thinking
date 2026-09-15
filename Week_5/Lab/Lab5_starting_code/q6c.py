### Q6 More on Lists
## c)
# Write your code below:
##############################################################
def get_non_common_strings(str_list1, str_list2):
    new_list1 = []
    new_list2 = []
    for str1 in str_list1:
        duplicate = False
        for str2 in str_list2:
            if str1 == str2:
                duplicate = True
        if not duplicate:
            new_list1.append(str1)
            new_list2.append(str2)
    return new_list1 + new_list2







##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

r_list = get_non_common_strings(["a", "b", "c", "d"], ["b", "d", "e", "f"])
print("Expected: ['a', 'c', 'e', 'f']")
print("Actual  : " + str(r_list))
print()