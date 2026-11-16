# Name:
# Email ID:

from q3a import manage_inventory

def process_orders(filename, list_of_orders):
    # Replace the code below with your implementation.
    inventory = manage_inventory(filename)

    if list_of_orders == []:
        return {}
    
    compiled_orders = {}
    for order in list_of_orders:
        order_id, buyer, name, qty = order

        if buyer not in compiled_orders:
            compiled_orders[buyer] = []

        qty_available = 0
        if name in inventory.keys():
            qty_available = inventory[name][0]
        else:
            compiled_orders[buyer].append((order_id, name, qty, 0))
            continue

        if qty_available >= qty:
            compiled_orders[buyer].append((order_id, name, qty, qty))
            qty_available -= qty
        else:
            compiled_orders[buyer].append((order_id, name, qty, qty_available))
            qty_available = 0
        inventory[name][0] = qty_available
        
    return compiled_orders
