# Name:
# Email ID:

def get_avg_len(str_list):
    total_ch_count = 0
    length = len(str_list)

    if length == 0:
        return 0

    for word in str_list:
        total_ch_count += len(word)

    return total_ch_count / length
