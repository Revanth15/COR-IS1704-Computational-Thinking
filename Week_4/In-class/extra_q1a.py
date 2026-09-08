def print_square_1(n):
    middle_row = (n // 2)
    gap = middle_row - 1
    for i in range(n):
        if i == middle_row or i == 0 or i == n-1:
            print('*' * n)
        else:
            print('*' + " " * gap + "*" + " " * gap + "*")

print_square_1(5)
print_square_1(9)