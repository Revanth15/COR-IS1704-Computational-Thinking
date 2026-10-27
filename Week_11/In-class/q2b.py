from q2a import display_all_gpas

dict = {'George Leung':3.4, 'Eric Wong':3.9, 'Michelle Lee':3.1}

print("Current GPA information:\n")
display_all_gpas(dict)

while True:
    check_gpa_name = input("Whose GPA do you want to change? ")

    if check_gpa_name in dict:
        new_gpa = float(input("What's the new GPA? "))
        dict[check_gpa_name] = new_gpa
        print("Thanks! GPA has changed.")

        print("The new GPA information:\n")
        display_all_gpas(dict)
    else:
        print("Sorry! This student doesn't exist.\n")


