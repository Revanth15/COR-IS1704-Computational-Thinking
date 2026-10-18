import random

practice_choice = input("Do you want to practice multiplication table? Please enter Y or N :")

while practice_choice != "N":
    num_1 = random.randint(1,9)
    num_2 = random.randint(1,9)
    answer = num_1 * num_2
    user_answer = int(input(f"\nWhat's the result of {num_1} times {num_2}? "))
    while user_answer != answer:
        user_answer = int(input("Wrong answer! Please try again :"))

    print("You are right!")
    practice_choice = input("\nDo you want to practice multiplication table? Please enter Y or N :")


print("\nGood-bye!")