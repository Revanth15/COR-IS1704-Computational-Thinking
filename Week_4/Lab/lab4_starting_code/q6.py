## Q6
######################################################################################
# This code is provided to you. DO NOT MODIFY THE CODE!
def calculate_price_after_discount(unit_price, quantity, discount_rate):
    """
    This function takes in the unit price, quantity and discount rate of an item.
    It returns the total price after discount for the item.
    Parameters:
        - unit_price (float): The unit price of the item.
        - quantity (int): The quantity of the item being purchased.
        - discount_rate (float): The percentage of discount. E.g., if there's a 
          10% discount, then discount_rate is set to 10.
    Return:
        - The total price of the item with the specified quantity after discount.
    """
    return (unit_price * quantity * (1 - discount_rate/100))

######################################################################################
# Write your solution below for Part A:
# items = int(input("How many items do you want to check out? "))
# total = 0
# for i in range(items):
#     print("Enter the details for Item ", i + 1)
#     item_discount_amt = 0
#     item_name = input("         What's this item? ")
#     item_price = float(input("          What's the unit price of this item? "))
#     item_quantity = int(input("         What's the quantity of this item? "))
#     is_item_discount = input("          Does this item have any discount? [yes|no] ")
#     if is_item_discount == "yes":
#         item_discount_amt = int(input("         What's the percentage of discount (%)? "))
#     total += calculate_price_after_discount(item_price,item_quantity, item_discount_amt)

# print(f"The total amount you have to pay is ${round(total,2)}")

######################################################################################
# Write your solution below for Part B:

def calculate_price_after_discount2(unit_price, quantity, discount_rate):
    """
    This function takes in the unit price, quantity and discount rate of an item.
    It returns the total price after discount for the item.
    Parameters:
        - unit_price (float): The unit price of the item.
        - quantity (int): The quantity of the item being purchased.
        - discount_rate (float): The percentage of discount. E.g., if there's a 
          10% discount, then discount_rate is set to 10.
    Return:
        - The total price of the item with the specified quantity after discount.
    """
    amt_after_discount = (unit_price * quantity * (1 - discount_rate/100))
    return amt_after_discount, (unit_price * quantity) - amt_after_discount

items = int(input("How many items do you want to check out? "))
total = 0
discount_total = 0
for i in range(items):
    print("Enter the details for Item ", i + 1)
    item_discount_amt = 0
    item_name = input("         What's this item? ")
    item_price = float(input("         What's the unit price of this item? "))
    item_quantity = int(input("         What's the quantity of this item? "))
    is_item_discount = input("         Does this item have any discount? [yes|no] ")
    if is_item_discount == "yes":
        item_discount_amt = int(input("         What's the percentage of discount (%)? "))
    item_total, discount = calculate_price_after_discount2(item_price,item_quantity, item_discount_amt)
    total += item_total
    discount_total += discount

print(f"The total amount you have to pay is ${round(total, 2)}")
print(f"You have saved ${round(discount_total, 2)}")