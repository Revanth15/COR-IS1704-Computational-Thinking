def compute_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * compute_factorial(n -1 )

# print(compute_factorial(3))
# print(compute_factorial(5))


def get_num_digits(n):
    if n < 10:
        return 1
    else:
        return get_num_digits(n // 10) + 1
    
# print(get_num_digits(146))
# print(get_num_digits(354928502))

def display_fibonacci_numbers(n):
    if n < 1:
        return
    
    display_fibonacci_numbers(n-1)
    print(get_fib(n), end=" ")

def get_fib(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return get_fib(n - 1) + get_fib(n - 2)
    
display_fibonacci_numbers(4)
print()
display_fibonacci_numbers(10)
print()