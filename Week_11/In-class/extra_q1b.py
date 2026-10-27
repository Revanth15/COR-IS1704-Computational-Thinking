seating_plan = {}

with open("seating_plan.txt", 'r') as file:
    for line in file:
        row, seat, name = line.strip().split(",")
        if row not in seating_plan:
            seating_plan[row] = {}
        seating_plan[row][seat] = name

row = input("Enter a letter (from A to E) :")
seat = input("Enter a seat number (from 1 to 25) :")
print()

if not seating_plan[row]:
    print("Seat not taken")
else: 
    if seat in seating_plan[row]:
        print(f"The person seated at the seat {row}{seat} is {seating_plan[row][seat]}")
        if str(int(seat) - 1) not in seating_plan[row]:
            print("Seat not taken on the left side")
        else:
            print(f"The person seating on the left side of that person is {seating_plan[row][str(int(seat) - 1)]}")

        if str(int(seat) + 1) not in seating_plan[row]:
            print("Seat not taken on the right side")
        else:
            print(f"The person seating on the right side of that person is {seating_plan[row][str(int(seat) + 1)]}")
    else:
        print("Seat not taken")