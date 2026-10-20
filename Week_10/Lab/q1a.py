## Q1 Reading Files
# Write your code below:
##############################

def print_alternate_lines(file_name):
    with open(file_name, 'r') as file:
        counter = 1
        for row in file:
            if counter % 2 != 0:
                print(row, end="")
            counter += 1