def add_new_email(email_dict, pair):
    name, email = pair
    if name in email_dict:
        old_email = email_dict[name]
        email_dict[name] = email
        return old_email
    
    email_dict[name] = email