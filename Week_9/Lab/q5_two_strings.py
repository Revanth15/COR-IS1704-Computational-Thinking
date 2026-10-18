string_1 = input("Enter the first string : ")
string_2 = input("Enter the second string : ")

while True:
    valid = True
    if " " in string_1 or " " in string_2:
        valid = False

    if len(string_2) <= len(string_1):
        valid = False

    for ch in string_1:
        if ch not in string_2:
            valid = False

    if not valid:
        print("Conditions not satisfied!")
        string_1 = input("\nEnter the first string : ")
        string_2 = input("Enter the second string : ")
    else:
        break

print("\nBingo!")