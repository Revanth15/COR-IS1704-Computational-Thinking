# Name:
# Email ID:

def sum_values_by_weights(lst_tups):
    # Replace the code below with your implementation.
    if len(lst_tups) == 0:
        return None
    total = 0
    for item in lst_tups:
        weight,cost = item
        if weight <= 10:
            total += cost
    return total


