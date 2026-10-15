book_cost = float(input("Please pick a book. How much is it (in $)? "))
VOUCHER_BALANCE = 100
total_cost = 0

while total_cost <= VOUCHER_BALANCE:
    total_cost += book_cost
    if VOUCHER_BALANCE - total_cost < 0:
        break
    print(f"You still have ${VOUCHER_BALANCE - total_cost} left.")
    book_cost = float(input("Please pick a book. How much is it (in $)? "))

print()
print("You are done!")
print(f"The total price is ${total_cost}")