# Prepare code

with open("phone_book.txt", "r") as phone_book:
    for row in phone_book:
        name, number = row.rstrip().split("|")
        if "+65" in number or (len(number) == 8 and "+" not in number):
            print(f"{name}\t{number}")