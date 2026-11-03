def get_reversed_list(num_list):
    # Modify the code below.
    reversed_list = []
    for i in range(len(num_list),0,-1):
        if num_list[i-1] != 0:
            reversed_list.append(num_list[i-1] * -1)
        else:
            reversed_list.append(num_list[i-1])

    return reversed_list