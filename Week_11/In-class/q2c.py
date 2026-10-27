from q2a import display_all_gpas

dict = {'George Leung':3.4, 'Eric Wong':3.9, 'Michelle Lee':3.1}

print("Current GPA information:\n")
display_all_gpas(dict)

while True:
    check_gpa_name = input("Whose GPA do you want to add? ")

    if check_gpa_name in dict:
        print("Sorry! This student already exists.\n")
    else:
        new_gpa = float(input(f"What's the GPA of {check_gpa_name}? "))
        dict[check_gpa_name] = new_gpa
        print("Thanks! GPA has been added.")

        print("The new GPA information:\n")
        display_all_gpas(dict)