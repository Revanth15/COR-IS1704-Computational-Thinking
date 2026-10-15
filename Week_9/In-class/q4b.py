pin = input("Enter your new pin: ")
confirm_pin = input("Confirm your new pin: ")

while True:
    valid = True
    reasons = [] 

    if pin != confirm_pin:
        valid = False
        reasons.append("The second PIN doesn't match the first PIN.")

    if len(pin) > 6:
        valid = False
        reasons.append("The PIN number is too long.")

    if len(pin) < 6:
            valid = False
            reasons.append("The PIN number is too short.")

    for ch in pin:
        if not(ch.isdigit()):
            valid = False
            reasons.append("The PIN number contains a non-digit character.")

    if valid:
        break
    else:
        print("Sorry! The following errors are detected:")
        for reason in reasons:
            print(f"\t- {reason}")
        print()
        pin = input("Enter your new pin: ")
        confirm_pin = input("Confirm your new pin: ")

print()
print("Thanks! Your new PIN has been set!")