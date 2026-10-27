phone_book = {}

with open("phone_numbers.txt", 'r') as file:
    for row in file:
        name, number = row.strip().split("|")
        if name not in phone_book:
            phone_book[name] = [number]
        else:
            phone_book[name].append(number)

name = input("Enter a person's name: ")
if name in phone_book:
    numbers = phone_book[name]
    print(f"{name} has {len(numbers)} number (s):")
    for number in numbers:
        print("\t" + number)
else:
    print(f"{name} cannot be found in our database.")
