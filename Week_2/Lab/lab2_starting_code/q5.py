# Lab2_Q5
# ########################################
# # lab2_Q5_part1: Write your code below:

def calculate_price_after_discount(unit_price, quantity, discount):
    total = (unit_price * quantity) * (100 - discount)/100
    return total

# # Test case # # 
# print(calculate_price_after_discount(1.5,5,10)) 



# ########################################
# lab2_Q5_part2: Write your code below:

cost_of_milk = calculate_price_after_discount(5.95, 2, 10)
cost_of_rice = calculate_price_after_discount(6.5, 1, 5)
cost_of_eggs = calculate_price_after_discount(2.4, 2, 0)
cost_of_kaya = calculate_price_after_discount(3.95, 3, 15)

total = round((cost_of_milk + cost_of_eggs + cost_of_rice + cost_of_kaya), 2)
print(f"The total of your shopping cart after discount is ${total}")