## Q1 Initials
# Write your code below:
##############################

num_pax = int(input("How many people will attend the meeting? "))
initials = []
for i in range(num_pax):
    participant_name = input(f"Participant {i+1}: ")
    initial = ""
    for name_part in participant_name.split(" "):
        initial += name_part[0].upper()
    initials.append(initial)

print()
print()
print("The initials of the participants are as follows:")
for initial in initials:
    print(initial)



