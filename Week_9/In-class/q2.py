num = int(input("Enter an integer: "))
odd_nums = []

while num >= 0:
    if num % 2 != 0:
        odd_nums.append(str(num))
    num = int(input("Enter an integer: "))

print("Thanks!")
print("The odd positive integers you have entered are the following:")
print(", ".join(odd_nums))