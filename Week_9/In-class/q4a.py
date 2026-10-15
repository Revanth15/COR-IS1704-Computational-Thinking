pin = input("Enter your new pin: ")
confirm_pin = input("Confirm your new pin: ")

while True:
    valid = True

    if pin != confirm_pin:
        valid = False

    if len(pin) != 6:
        valid = False

    for ch in pin:
        if not(ch.isdigit()):
            valid = False

    if valid:
        break
    else:
        print("Sorry! there is an error!", end="\n\n")
        pin = input("Enter your new pin: ")
        confirm_pin = input("Confirm your new pin: ")

print()
print("Thanks! Your new PIN has been set!")