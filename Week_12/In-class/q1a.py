def retrieve_email(email_dict, name):
    if name in email_dict.keys():
        return email_dict[name]
    return None
