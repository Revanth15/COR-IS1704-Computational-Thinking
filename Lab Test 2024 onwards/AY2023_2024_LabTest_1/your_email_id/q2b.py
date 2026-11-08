# Name:
# Email ID:

def count_non_digits(str_list):
    # Modify the code below.
    non_digit_list = []

    for i in range(len(str_list)):
        word = str_list[i]
        non_digit_list.append(0)
        for ch in word:
            if not ch.isdigit():
                non_digit_list[i] += 1
    return non_digit_list