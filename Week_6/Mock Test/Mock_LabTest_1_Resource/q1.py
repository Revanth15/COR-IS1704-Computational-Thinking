# =====
# q1.py
# =====
# Name: Revanth Ravi
# Email ID: revanth.rs.2026

def get_hashtags(post_list):
    # modify the code below
    hash_list = []
    for str in post_list:
        split = str.split(" ")
        for word in split:
            if word[0] == "#":
                hash_list.append(word)

    return hash_list
