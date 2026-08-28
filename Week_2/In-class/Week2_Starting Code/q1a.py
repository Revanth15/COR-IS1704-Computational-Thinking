# ################################################################################
# The following code is given to you.
def compute_average(a, b, c):
    """ 
    This function returns the average of the three numbers a, b and c.
    """
    return (a + b + c)/3

# ################################################################################    
# Write your code below:

number_1 = float(input("Enter 1st number: "))
number_2 = float(input("Enter 2nd number: "))
number_3 = float(input("Enter 3rd number: "))
avg = compute_average(number_1, number_2, number_3)
print(f"Average: {avg}")
