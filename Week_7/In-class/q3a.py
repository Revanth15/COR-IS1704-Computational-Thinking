def print_triangle(ch, num_rows):
    for i in range (1,num_rows+1):
        num_ch = i + i -1
        print((" " * (num_rows - i)) + ch * num_ch + (" " * (num_rows - i)))

print_triangle("*", 3)
print_triangle("#", 5)