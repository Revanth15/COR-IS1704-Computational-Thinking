first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

while True:
    valid = True
    if first_number < 1 or second_number < 1:
        valid = False

    if first_number + second_number > 100 :
        valid = False

    if not valid:
        print("Conditions not satisfied!", end="\n\n")
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
    else:
        break

print("\nThanks!")