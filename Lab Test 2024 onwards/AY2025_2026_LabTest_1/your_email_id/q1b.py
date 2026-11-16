# Name:
# Email ID:

def compute_plan_cost(plan, data_used):
    # Modify the code below.
    cost = 0
    if plan == "Lite":
        cost += 10 + round(max(0,data_used - 100) * 5, 2)
    elif plan == "Standard":
        cost += 20 + round(max(0,data_used - 300) * 3, 2)
    elif plan == "Pro":
        cost += 50 + round(max(0,data_used - 900) * 1, 2)
    else:
        return "Invalid plan selected"
    return cost
