## Q8
# ################################################################################
# The function below is for you to implement! 
def display_fibonacci(n):
    """
    This function takes in an integer n (greater or equal to 3). It prints out the 
    first n Fibonacci numbers, starting from 1. The function doesn't return anything.
    """
    # Modify the code below to print the first n Fibonacci numbers
    i = 0
    j = 1
    k = 0
    for x in range(n-1):
        k = i + j
        print(k, end=" ")
        
        i = j
        j = k

    print()

# i + j = k
# 0 + 1 = 1
# 1 + 1 = 2
# 1 + 2 = 3
# 2 + 3 = 5
# 3 + 5 = 8
# 5 + 8 = 13
# 8 + 13 = 21

# k -> i + j
# j -> i
# k -> j