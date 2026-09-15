# Name:
# Email ID:

def is_valid_username(username):
    if " " in username or username == "" or len(username) > 8 or len(username) < 0:
        return False

    username_validity = True
    for ch in username:
        if ch not in "abcdefghijklmnopqrstuvwxyz0123456789_.!#$%?":
            username_validity = False

    return username_validity