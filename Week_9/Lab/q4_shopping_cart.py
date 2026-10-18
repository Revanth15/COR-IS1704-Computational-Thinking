# Part I

# items_left = input("Do you have any item left in your shopping cart? Please enter Y or N: ").upper()

# total = 0

# while items_left != "N":
#     name = input("Please enter the name of the item : ")
#     price = float(input("Please enter the price of the item : $"))
#     quantity = int(input("Please enter the quantity of the item : "))
#     total += price * quantity

#     items_left = input("\nDo you have any item left in your shopping cart? Please enter Y or N: ").upper()

# print(f"\nTotal price: ${total}")

# Part II

items_left = input("Do you have any item left in your shopping cart? Please enter Y or N: ").upper()

total = 0
grocery_list = []

while items_left != "N":
    name = input("Please enter the name of the item : ")
    price = float(input("Please enter the price of the item : $"))
    quantity = int(input("Please enter the quantity of the item : "))
    total += price * quantity
    grocery_list.append((name,price,quantity))

    items_left = input("\nDo you have any item left in your shopping cart? Please enter Y or N: ").upper()

print("You've entered the following items:")
for item in grocery_list:
    print(f"\t{item[0]}\t${item[1]}\t{item[2]}")

print(f"\nTotal price: ${total}")