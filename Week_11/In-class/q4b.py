
def read_to_dict(file_name):
    dict = {}
    with open(file_name, 'r') as file:
        for row in file:
            name, email, birthdate, gender = row.strip().split("\t")
            dict[email] = (name, birthdate, gender)
    return dict

dict = read_to_dict("students.txt")
loop = "Y"

while loop != "N":
    search_email = input("Please enter an email ID: ")
    if search_email in dict:
        name, bithdate, gender = dict[search_email]
        if gender == "M":
            gender = "male"
        else:
            gender = "female"
        print(f"The student {name}, {gender}, born on {bithdate}")
    else:
        print("This is not a valid email ID.")

    loop = input("\nDo you want to continue? [Y|N] :").upper()
    
    if loop == "Y":
        print()
    else:
        break

print("Good-bye!")