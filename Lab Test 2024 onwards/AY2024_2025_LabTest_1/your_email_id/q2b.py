# Name:
# Email ID:

def get_longest_string(str_list):
    # Modify the code below.
    return_str = ""
    if str_list == []:
        return None
    for word in str_list:
        if len(word) >= len(return_str):
            return_str = word
    return (return_str, len(return_str))
