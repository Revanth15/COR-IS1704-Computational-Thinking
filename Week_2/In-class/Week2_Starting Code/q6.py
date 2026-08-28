from week2_utility import get_insurance_premium

age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").capitalize()

print(get_insurance_premium(age, gender))