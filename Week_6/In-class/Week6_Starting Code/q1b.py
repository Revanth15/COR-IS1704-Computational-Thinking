# Name: Revanth
# Email ID: revanth.rs.2026

def merge_list(list1,list2):
    # Replace the code below with your implementation.
    merged_list = []
    len_l1 = len(list1)
    len_l2 = len(list2)
    lowest_len = len_l1
    
    if len_l2 < len_l1:
        lowest_len = len_l2

    for i in range(lowest_len):
        merged_list.append(list1[i])
        merged_list.append(list2[i])
    remaining_nums_l1 = list1[lowest_len:]
    remaining_nums_l2 = list2[lowest_len:]

    return merged_list + remaining_nums_l1 + remaining_nums_l2