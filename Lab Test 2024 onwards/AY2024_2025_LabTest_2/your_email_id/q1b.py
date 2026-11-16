# Name:
# Email ID:

def alternate_and_reverse(s1, s2):
    # Replace the code below with your implementation.
    l1 = len(s1)
    l2 = len(s2)
    min_len = min(l1, l2)
    remaining_chars = ""

    if l1 == 0:
        remaining_chars = s2
    elif l2 == 0:
        remaining_chars = s1
    elif abs(l1 - l2) != 0:
        if l1 > l2:
            remaining_chars = s1[l1-l2 + 1:]
        else:
            remaining_chars = s2[l2-l1 + 1:]
    remaining_chars = remaining_chars[::-1]
    return_str = ''

    for i in range(min_len):
        return_str += s1[i] + s2[i]
    return return_str + remaining_chars

