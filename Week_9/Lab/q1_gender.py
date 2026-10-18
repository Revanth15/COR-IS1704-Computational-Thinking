inp_gender = input("What's your gender? Please enter M or F: ")

while inp_gender not in ['M', 'F']:
    print("Wrong input!", end='\n\n')
    inp_gender = input("What's your gender? Please enter M or F: ")

gender = "male"
if inp_gender == "F":
    gender = "female"

print(f"\nThank's Your gender is {gender}.")