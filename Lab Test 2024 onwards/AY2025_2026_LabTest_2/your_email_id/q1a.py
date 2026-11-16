# Name:
# Email ID:

def get_specific_tuples(tup_list, num):
    # Modify the code below.
    return_lst = []
    for t in tup_list:
        if t[0] + t[-1] >= num:
            return_lst.append(t)
    return return_lst
