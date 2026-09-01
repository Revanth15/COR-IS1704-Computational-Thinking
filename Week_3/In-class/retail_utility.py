def calculate_max_quantity_and_change(unit_price, amount):
    num_jars = amount // unit_price
    change = amount % unit_price
    return (num_jars, change)