def find_last_letter(my_str):
    # Modify the code below.
    last_index = -1
    for i in range(len(my_str)):
        if my_str[i].isalpha():
            last_index = i
    return last_index
    