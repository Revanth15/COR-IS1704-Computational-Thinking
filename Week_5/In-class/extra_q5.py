def caesar_cipher(message, shift):
    characters = "abcdefghijklmnopqrstuvwxyz"
    cipher = ""
    for ch in message:
        if ch != " ":
            index = characters.index(ch)
            index = (index + shift) % 26
            cipher += characters[index]
        else: 
            cipher += " "
    return cipher

print(caesar_cipher("abcd xyz", 4))