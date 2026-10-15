student_bool = input('Are you a student?: ')

while True:
    if student_bool in ['YES', 'Yes', 'yes', 'NO', 'No', 'no']:
        print("Got it!")
        break
    else:
        print("Please enter a valid answer (YES, Yes, yes, NO, No, no)")
        student_bool = input('Are you a student?: ')