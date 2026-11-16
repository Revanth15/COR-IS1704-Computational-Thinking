# Name:
# Email ID:
    
def is_food_safe(temp, holding_time):
    # Modify the code below.
    if 75 <= temp <= 100:
        return True
    if 60 < temp < 75 and holding_time >= 2:
        return True
    return False
