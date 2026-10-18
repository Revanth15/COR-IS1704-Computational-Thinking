import random
random_no = random.randint(1,100)
guess = int(input("Enter your guess (between 1 and 100) :"))

while random_no != guess:
    if random_no > guess:
        print("Your guess is too low!")
    elif random_no < guess:
        print("Your guess is too high!")
    guess = int(input("\nEnter your guess (between 1 and 100) :"))

print("\nBingo!")