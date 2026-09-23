# =====
# q3.py
# =====
# Name: Revanth Ravi
# Email ID: revanth.rs.2026

def pad_strings(str_list, ch):
    # modify the code below
    longest_word_length = 0
    number_of_words = len(str_list)
    updated_list = []

    for str in str_list:
        if len(str) > longest_word_length:
            longest_word_length = len(str)

    for str in str_list:
        word_length = len(str)
        number_of_words -= 1
        new_string = (" " * (number_of_words)) + str + ((longest_word_length - word_length) * ch)
        updated_list.append(new_string)

    return updated_list
