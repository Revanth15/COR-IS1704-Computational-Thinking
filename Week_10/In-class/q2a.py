def get_books_cheaper_than(input_file, price_limit, output_file):
    with open(input_file, 'r') as input_file:
        with open(output_file, 'w') as output_file:
            for book in input_file:
                stripped_book = book.rstrip("\n")
                name, author, price = stripped_book.split("\t")
                if float(price.strip("$")) < price_limit:
                    output_file.write(f"{name}\t{author}\t${price}\n")
    pass


# Test cases used to test your function
print('\nTestcase 1')
print('-' * 10)
print("Expected: " + '\nTurtles All the Way Down\tJohn Green\t$11.99\n' + 'Animal Farm and 1984\tGeorge Orwell\t$7.50\n' + 'Inception: A Dark Paranormal Romance (The Marked Book 1)\tBianca Scardoni\t$13.09\n')
input_file = 'books-1.txt'
output_file = 'books-1-output.txt'
price_limit = 15.0
get_books_cheaper_than(input_file, price_limit, output_file)
print('Actual: ' )
with open(output_file) as f:
    print(f.read())

print('\nTestcase 2')
print('-' * 10)
print("Expected:\n")
input_file = 'books-2.txt'
output_file = 'books-2-output.txt'
price_limit = 7.0
get_books_cheaper_than(input_file, price_limit, output_file)
print('Actual: ' )
with open(output_file) as f:
    print(f.read())