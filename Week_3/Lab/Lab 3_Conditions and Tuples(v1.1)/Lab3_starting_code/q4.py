## Q4
# PART 1
# The following function is for you to implement.
def get_ticket_info(age):
    
    # Modify the code below to return the right value

    if age < 3:
        return (0, True)
    elif 3 <= age <= 12:
        return (22, True)
    elif age >= 60:
        return (15, True)
    else:
        return (33, False)
    
    
# ################################################################################
# The code below is to test your implementation of the function above. 
# DO NOT MODIFY THE CODE BELOW!

# The following line of code should display (33, False)
print(get_ticket_info(40))

# The following line of code should display (22, True)
print(get_ticket_info(10))


# PART 2
# Write your code below to prompt the user for age
# and print the expected output


age = int(input("How old are you? "))
fare, is_discount = get_ticket_info(age)
if is_discount:
    print("Congratulations! You qualify for a discount.")
print(f"You need to pay ${fare}")