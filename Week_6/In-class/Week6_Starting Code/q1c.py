# Name: Revanth
# Email ID: revanth.rs.2026

def check_numbers(int_list_1 ,int_list_2):
    # Replace the code below with your implementation.
    valid = True
    for num1 in int_list_1:
        # Prevent unnecessary loops.
        if not valid:
            break

        for num2 in int_list_2:
            # Loops through each number and checks if its divisible, if
            # it is, then it stops and goes to the next number
            if num1 % num2 == 0:
                valid = True
                break
            else:
                valid = False
    return valid