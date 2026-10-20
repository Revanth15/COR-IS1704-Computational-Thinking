def create_num_file(output_file, n):
    number = 0
    with open(output_file, 'w') as file:
        while number <= n:
            if number % 2 == 0:
                file.write(str(number) + "\n")
            number += 1
    pass



# Test cases
print('Expected: ')
print('0\n2\n4\n6\n8\n10')
print('Actual: ')
create_num_file('q1-output.txt', 10)
with open('q1-output.txt') as f:
    print(f.read())