# ################################################################################
# Implement the function below:
import math
def compute_geometric_mean(x, y, z):
    """
    This function returns the geometric mean of the three numbers x, y and z.
    """
    # Write your code here:
    return math.cbrt(x*y*z)


# ################################################################################    
# The code below is to test your implementation above.
# DO NOT MODIFY THE CODE BELOW!

print("The geometric mean of 2, 4 and 6 is:", compute_geometric_mean(2, 4, 6))
