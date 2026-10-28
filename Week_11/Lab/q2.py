## Q2 Prime Numbers
# write your code below
import math

def create_prime_dict(integer_list):
    prime_dict = {}
    for num in integer_list:
        if num < 1:
            prime_dict[num] = False
            continue
        if num == 2:
            prime_dict[num] = True
            continue
        if num % 2 == 0:
            prime_dict[num] = False
            continue

        boundry = int(math.sqrt(num))
        for i in range(3, boundry + 1, 2):
            if num % i == 0:
                prime_dict[num] = False
                continue

        prime_dict[num] = True
    return prime_dict
        