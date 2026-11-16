# Name:
# Email ID:
    
def calculate_bmr(weight, height, age, gender):
    # Modify the code below.
    modifier = {"M" : 5, "F" : -161}
    BMR = (10 * weight) + (6.25 * height) - (5 * age) + modifier[gender]
    return int(BMR)
