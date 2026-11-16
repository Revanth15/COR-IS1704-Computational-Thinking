# Name:
# Email ID:

def manage_inventory(filename):
    # Replace the code below with your implementation.

    inventory = {}
    with open(filename, 'r') as i_file:
        for line in i_file:
            product_name, category, price_per_unit, cost_per_unit, quantity_in_stock = line.strip().split(",")
            cost_per_unit = float(cost_per_unit.strip("$"))
            price_per_unit = float(price_per_unit.strip("$"))

            min_qty = 0

            profit_margin = (price_per_unit - cost_per_unit) / cost_per_unit

            if profit_margin >= 0.5:
                min_qty = 3
            elif 0.2 <= profit_margin < 0.5:
                min_qty = 8
            elif profit_margin < 0.2:
                min_qty = 15

            inventory[product_name] = [int(quantity_in_stock), min_qty]

            
    return inventory
