## Q1a Substitution Cipher
# write your code below

def encrypt(my_dict, msg):
    new_string = ""
    for ch in msg:
        if ch in my_dict:
            new_string += my_dict[ch]
        else:
            new_string += ch
    return new_string