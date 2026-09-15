# Name:
# Email ID:

def concatenate_emails(str_list):
    valid_emails = ""

    for word in str_list:
        if " " in word or word.count("@") != 1:
            pass
        else:
            valid_emails += word + ";"

    return valid_emails