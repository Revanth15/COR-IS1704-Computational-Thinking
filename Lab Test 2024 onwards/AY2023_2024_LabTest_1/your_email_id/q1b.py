# Name:
# Email ID:

def compute_rebate(is_singaporean_household, flat_type, month):
    # Replace the code below with your implementation.
    if not is_singaporean_household:
        return 0.0

    if month not in [1,4,7,10]:
        return 0.0

    if flat_type in ["1", "2"]:
        if month == 1:
            return 0.5
        elif month == 4:
            return 1.0
        elif month == 7:
            return 1.0
        elif month == 10:
            return 1.0
    elif flat_type in ["3", "4"]:
        if month == 1:
            return 0.5
        elif month == 4:
            return 1.0
        elif month == 7:
            return 0.5
        elif month == 10:
            return 0.5
    elif flat_type == "5":
        if month == 1:
            return 0.5
        elif month == 4:
            return 0.5
        elif month == 7:
            return 0.5
        elif month == 10:
            return 0.5
    elif flat_type == "E":
        if month == 1:
            return 0.0
        elif month == 4:
            return 0.5
        elif month == 7:
            return 0.5
        elif month == 10:
            return 0.5
    return None