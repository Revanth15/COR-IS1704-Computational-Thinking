def display_numbers(m,n):
    for i in range(m,n+1):
        if i % 3 == 0 and i % 5 != 0:
            print("-", end=" ")
        elif i % 3 != 0 and i % 5 == 0:
            print("*", end=" ")
        elif i % 3 == 0 and i % 5 == 0:
            print("#", end=" ")
        else:
            print(i, end=" ")

display_numbers(4,16)