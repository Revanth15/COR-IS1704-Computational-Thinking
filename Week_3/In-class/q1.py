# Write down what i think the outcome will be

# a) Answer: a >= b a <= b
a = 20
b = 20
if a >= b:
    print("a >= b")
if a <= b:
    print("a <= b")

# b) Answer: a >= b a <= b
a = 30
b = 30
if a >= b:
    print("a >= b")
elif a <= b:
    print("a <= b")

# c) Answer: False True
c = "IS1704"
d = "is1704"
e = "IS" + "1704"

print(c == d)
print(c == e)

# d) Answer: Good! True
def test_if_else(condition1, condition2):
    if (condition1):
        print("Great!")
        return True
    elif(condition2):
        print("Good!")
        return True
    else:
        print("Okay")
        return False

result = test_if_else(4 % 2 != 0, 3 // 2 == 1)
print(result)