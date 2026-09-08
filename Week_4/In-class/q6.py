# Part I

# Test argument
# message = "Hello!"
message = input("Enter a message : ")

for i in range(len(message)):
    for l in range(i+1):
        print(message[l], end="")
    print()

print()

# Part II
for i in range(len(message)+1,0,-1):
    for l in range(i-1):
        print(message[l], end="")
    print()