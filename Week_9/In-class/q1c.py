# Check if a string is a valid name
# def is_valid_name(name):
#     return any(not (char.isalnum() or char.isspace()) for char in name)

def is_valid_name(name):
    if not name.strip():
        return False
    for ch in name:
        if not(ch.isalpha()) and not(ch.isspace()):
            return False
    return True

name = input('Enter your name:  ')

while True:
    valid = is_valid_name(name)
    if valid:
        print("Thank you!")
        break
    else:
        print("Please enter a valid name!")
        name = input('Enter your name: ')
