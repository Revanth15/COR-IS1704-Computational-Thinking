# a)
def get_day_of_week(num):
    if num < 0:
        return "Your number should be at least 0."
    elif num == 0:
        return "Sunday"
    elif num == 1:
        return "Monday"
    elif num == 2:
        return "Tuesday"
    elif num == 3:
        return "Wednesday"
    elif num == 4:
        return "Thursday"
    elif num == 5:
        return "Friday"
    elif num == 6:
        return "Saturday"
    else:
        return "Your number should be at most 6."
    

# b)
num = int(input("Enter a number indicating the dat of a week [0 to 6]: "))
print(get_day_of_week(num))