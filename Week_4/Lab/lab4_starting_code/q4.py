# Part I

message = "This is the original message used."

encrypted_message = ""
for ch in message:
    if ch == 'a':
        encrypted_message += 'e'
    elif ch == 'e':
        encrypted_message += 'i'
    elif ch == 'i':
        encrypted_message += 'o'
    elif ch == 'o':
        encrypted_message += 'u'
    elif ch == 'u':
        encrypted_message += 'a'
    else:
        encrypted_message += ch

print(encrypted_message)

# Part II

encrypted_message = ""
for ch in message:
    if ch == 'a':
        encrypted_message += 'e'
    elif ch == 'e':
        encrypted_message += 'i'
    elif ch == 'i':
        encrypted_message += 'o'
    elif ch == 'o':
        encrypted_message += 'u'
    elif ch == 'u':
        encrypted_message += 'a'
    else:
        encrypted_message += ch

reversed_string = encrypted_message[::-1]
print(reversed_string)