month_int = int(input("Enter month: "))

if 1 < month_int < 12:
    if month_int == 2:
        print("There are 28 days in this month.")
    else:
        print("There are 30 days in this month.")
else:
    print("Enter a number between 1 and 12 only!")

