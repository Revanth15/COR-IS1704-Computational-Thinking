# Name: Revanth
# Email ID: revanth.rs.2026

def get_larger_values(num_list):
    # Replace the code below with your implementation.
    total = 0
    bigger_num_list = []
    for num in num_list:
        total+=num
    for num in num_list:
        if num > total/len(num_list):
            bigger_num_list.append(num)
    return bigger_num_list

