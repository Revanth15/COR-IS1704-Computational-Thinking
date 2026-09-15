# Name:
# Email ID:

def extract_email_id(email_address):
    # Replace the code below with your implementation.
    if "@" in email_address:
        email = email_address.split("@")
        return email[0]
    else:
        return ""
