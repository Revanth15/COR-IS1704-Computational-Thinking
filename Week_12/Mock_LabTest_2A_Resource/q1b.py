def find_second_letter(my_str):
    # Write your code below
    alpha_found = False
    for i in range(len(my_str)):
        if my_str[i].isalpha():
            if alpha_found:
                return i
            alpha_found = True
    return -1

