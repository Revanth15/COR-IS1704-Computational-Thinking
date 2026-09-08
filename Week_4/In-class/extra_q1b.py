def print_square_2(n):
    middle_row = (n // 2)
    total_space = n - 2
    for i in range(n):
        spacing = abs(total_space - (i * 2))
        gap = (total_space - spacing - 2) // 2
        if i == 0 or i == n-1:
            print('*' * n)
        elif i == middle_row:
            print('*' + " " * (middle_row - 1) + "*" + " " * (middle_row - 1) + "*")
        elif i < middle_row:
            print('*' + (" " * gap) + "*" + (" " * spacing) + "*" + (" " * gap) + "*")
        else:
            print('*' + " " * (gap + 1) + "*" + " " * (spacing - 2) + "*" + " " * (gap + 1) + "*")

# print_square_2(5)
print_square_2(9) 