# Name:
# Email ID:

def extract_multiple_email_ids(email_addesses):
    # Replace the code below with your implementation.
    email_ids = email_addesses.split(";")
    for email in email_ids:
        if "@" in email:
            email_id = email.split("@")
            print(email_id[0])
            # return email_id[0]
        else:
            print("")
            # return ""
