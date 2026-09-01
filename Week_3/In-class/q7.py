def get_discount_rate(num_boxes):
    if num_boxes >= 5:
        return 0.2
    elif 2 <= num_boxes <= 4:
        return 0.1
    else:
        return 0.0

def calculate_total_amount(brand, num_boxes):
    price = 0
    if brand == "Man Fu Yuan":
        price = 59.60
    elif brand == "Tung Lok":
        price = 55.40

    total_cost = (price * (1 - get_discount_rate(num_boxes))) * num_boxes
    return total_cost

brand = input("Which brand do you want to buy? ")
num_boxes = int(input("How many bxes do you want to buy? "))
total = calculate_total_amount(brand, num_boxes)
print(f"You need to pay ${total}")