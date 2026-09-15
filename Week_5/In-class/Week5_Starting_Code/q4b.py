# Name:
# Email ID:

def get_longest_str(str_list):
    longest_word = ""

    for word in str_list:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word
