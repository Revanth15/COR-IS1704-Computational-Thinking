# Name:
# Email ID:

def get_digits_of_even_index(my_str):
    # Modify the code below.
    numbers = ""
    for i in range(0,len(my_str),2):
        if my_str[i].isdigit():
            numbers += my_str[i]
    return numbers