### Q1b Reading Files
# Write your code below:

def print_alternate_columns(file_name):
    with open(file_name, 'r') as file:
        for row in file:
            words = row.strip().split("&")
            counter = 0
            words_list = []
            for word in words:
                if counter % 2 == 0:
                    words_list.append(word)
                counter += 1
            print("&".join(words_list))
