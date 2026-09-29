def print_frame(ch, num_rows, num_cols):
    for i in range(0, num_rows):
        if i == 0:
            print(ch * num_cols)
        elif i == (num_rows-1):
            print(ch * num_cols)
        else:
            print(ch + " " * (num_cols - 2) + ch)

print_frame("#", 5, 6)
print_frame("#", 2, 2)