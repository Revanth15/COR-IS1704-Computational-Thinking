book_author_dict = {"Harry Potter and the Sorcerer's Stone":'J.K. Rowling',
"Turtles All the Way Down":'John Green',
"Animal Farm and 1984":'George Orwell',
"The Da Vinci Code":'Dan Brown',
"Harry Potter and the Goblet of Fire":'J.K. Rowling',
"Origin":'Dan Brown'}

search_bool = input("Do you want to search for the author of a book? [Y|N]").upper()

while search_bool != "N":
    book_title = input("Please enter a book title :")
    if book_title in book_author_dict:
        print(f"The author of the book is {book_author_dict[book_title]}")
    else:
        print("Not found!")

    search_bool = input("\nDo you want to continue? [Y|N]").upper()

print("Good-bye!")