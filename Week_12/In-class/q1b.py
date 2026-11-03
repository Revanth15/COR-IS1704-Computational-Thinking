def create_email_dict(email_list):
    email_dict = {}
    for i in range(0,len(email_list)-1,2):
        email_dict[email_list[i]] = email_list[i+1]

    return email_dict