# message = "Hello!"
# message = "Python is fun!"
# message = input("Enter a message :")

# Part I
# for ch in message:
#     print(ch, end=" ")

# Part II
# for i in range(len(message)):
#     if i != len(message) - 1:
#         print(message[i], end="-")
#     else:
#         print(message[i])

# Part III
def print_message_with_seperators(message, seperator):
    for i in range(len(message)):
        if i != len(message) - 1:
            print(message[i], end=seperator)
        else:
            print(message[i])

message = input("Enter a message :")
seperator = input("Enter a seperator :")
print_message_with_seperators(message, seperator)

