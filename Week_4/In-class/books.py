books = int(input("How many books do you have in your basket? "))



total_cost = 0
least_expensive_book_cost = 999999999
most_expensive_book_cost = 0
number_of_books_below_10 = 0
for i in range(books):
    book_cost = float(input(f"What is the price of the book number {i+1}? :$"))
    total_cost += book_cost
    if most_expensive_book_cost <= book_cost:
        most_expensive_book_cost = book_cost
    if least_expensive_book_cost >= book_cost:
        least_expensive_book_cost = book_cost
    if book_cost < 10:
        number_of_books_below_10 += 1

percentage_of_books_below_10 = round((number_of_books_below_10/books) * 100, 2)
    
print(f"a) Total price: ${total_cost}")
print(f"b) Average price: ${round(total_cost / books,2)}")
print(f"c) Price of the least expensive book: ${least_expensive_book_cost}")
print(f"d) Price of the most expensive book: ${most_expensive_book_cost}")
print(f"e) Number of books cheaper than $10 : {number_of_books_below_10}")
print(f"f) Percentage of books cheaper than $10 : {percentage_of_books_below_10}%")