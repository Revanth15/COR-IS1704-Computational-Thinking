# lab2_Q1
# ###########################################
# The code below is given. Guess the output.

def perform_magic_1(x):
    x = x + 1
    
def perform_magic_2(x):
    x = x + 10
    return x
    
def perform_magic_3(y):
    return (y + 3)

def perform_magic_4(z):
    z = z + 1
    z = perform_magic_2(z)
    return (z + 1)

x = 0
print(x)
# Answer: 0

perform_magic_1(x)
print(x)
# Answer: 0

perform_magic_2(x)
print(x)
# Answer: 0

x = perform_magic_3(x)
print(x)
# Answer: 3

x = perform_magic_4(x)
print(x)
# Answer: 15