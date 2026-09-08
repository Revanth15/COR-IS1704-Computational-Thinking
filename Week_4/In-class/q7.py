password = "ThisIsAStrongPassword123!"
# password = "ThisIsAStrongPassword"
# password = input("Input a password: ")

# lower_characters = 0
# upper_characters = 0
# numbers = 0
# special_characters = 0
# is_strong_password = False

# for ch in password:
#     if ch in "abcdefghijklmnopqrstuvwxyz":
#         lower_characters += 1
#     if ch in "abcdefghijklmnopqrstuvwxyz".upper():
#         upper_characters += 1
#     if ch in "0123456789":
#         numbers += 1
#     if ch in "!@#$":
#         special_characters += 1

# if len(password) >= 8 and lower_characters > 0 and upper_characters > 0 and numbers > 0 and special_characters > 0:
#     is_strong_password = True

# print(is_strong_password)


# Shorter implementation after using google to check for syntax
lower_characters = False
upper_characters = False
numbers = False
special_characters = False
is_strong_password = False

for ch in password:
    if ch.islower():
        lower_characters = True
    if ch.isupper():
        upper_characters = True
    if ch.isdigit():
        numbers = True
    if ch.isalnum():
        special_characters = True

if len(password) >= 8 and lower_characters and upper_characters and numbers and special_characters:
    is_strong_password = True

print(is_strong_password)