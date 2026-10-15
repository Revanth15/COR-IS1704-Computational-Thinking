def count_no_of_digits(str):
    no_of_digits = 0
    for ch in str:
        if ch.isdigit():
            no_of_digits += 1
    return no_of_digits

def get_strings_with_digits(str_list, t):
    max_no_strings = len(str_list)
    counter = 0
    no_of_digits = 0
    return_list = []
    while counter < max_no_strings:
        if no_of_digits > t:
            return return_list
        no_of_digits += count_no_of_digits(str_list[counter])
        return_list.append(str_list[counter])

        counter += 1
    return str_list

print(get_strings_with_digits(['ab12', 'IS111', '9', 'X7Z', 'k', 'lmn'], 5))