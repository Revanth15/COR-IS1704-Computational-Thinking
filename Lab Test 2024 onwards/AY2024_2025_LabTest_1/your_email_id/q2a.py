# Name:
# Email ID:

def count_short_strings(str_list, n):
    # Modify the code below.
    counter = 0
    for word in str_list:
        if len(word) < n:
            counter += 1
    return counter