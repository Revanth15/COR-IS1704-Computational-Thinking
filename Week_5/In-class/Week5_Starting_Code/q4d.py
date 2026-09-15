# Name:
# Email ID:

def check_hashtags(str_list):
    valid = True
    if len(str_list) == 0:
        return False
    
    for word in str_list:
        if word[0] != "#" or " " in word:
            return False

    return valid