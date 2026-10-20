# Prepare code

with open("phone_book.txt", "r") as phone_book:
    phone_book_name_list = []
    phone_book_numbers = []
    for row in phone_book:
        name, number = row.rstrip().split("|")
        if name not in phone_book_name_list:
            phone_book_name_list.append(name)
            phone_book_numbers.append([number])
        else:
            index = phone_book_name_list.index(name)
            phone_book_numbers[index].append(number)

    with open("phone_book_reorganized.txt", 'w') as reorg_book:
        for i in range(len(phone_book_name_list)):
            reorg_book.write(f"{phone_book_name_list[i]}\n{("\n").join(phone_book_numbers[i])}\n\n")



# Test cases
# Test code to check the output file
print()
expected='\nGeorge Leung\n98987676\n\nEric Wong\n+60 4123\n+65 91234567\n\nMichelle Lee\n(+65)67894321\n(+65)88776655\n'
print('Expected: '+expected)
output_file = 'phone_book_reorganized.txt'
print('Actual: ' )
with open(output_file) as f:
    print(f.read())