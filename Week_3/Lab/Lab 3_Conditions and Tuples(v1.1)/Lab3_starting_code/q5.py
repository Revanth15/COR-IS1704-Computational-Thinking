# Q5
# The following function is provided to you.
# Do not modify the function definition!
def get_user_info():
    """
    This function prompts the user for his/her name, gender, age and whether
    or not he/she is a student.
    The function returns a tuple that contains all the information entered
    by the user.
    """
    name = input("What's your name? ")
    gender = input("What's your gender? [M|F] ")
    age = int(input("What's your age? "))
    is_student = input("Are you a student? [yes|no] ")
    return (name, gender, age, is_student == 'yes')

# Write your code below:

name, gender, age, is_student = get_user_info()

salutation = "Mr."
if gender == "F":
    salutation = "Ms."

if age <= 6:
    print(f"{name}, you can travel for free.")
elif 6 < age < 60:
    if is_student:
        print(f"{salutation} {name}, you can get concessionary fare for student.")
    else:
        print(f"{salutation} {name}, you need to pay full fare.")
elif age >= 60:
    print(f"{salutation} {name}, you can get consessionary fare for senior citizens.")