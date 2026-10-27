
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
        print(f"The birthdate of this student is {dict[search_email][1]}")
    else:
        print("This is not a valid email ID.")

    loop = input("\nDo you want to continue? [Y|N] :").upper()
    print()
