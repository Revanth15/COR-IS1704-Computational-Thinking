## Q1b Substitution Cipher
# write your code below

def decrypt(my_dict, encrypted_msg):
    decrypted_string = ""

    reversed_dict = {v: k for k, v in my_dict.items()}

    for ch in encrypted_msg:
        if ch in reversed_dict:
            decrypted_string += reversed_dict[ch]
        else:
            decrypted_string += ch

    return decrypted_string