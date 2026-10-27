def convert_to_dict(tuple_list):
    dict = {}
    for item in tuple_list:
        dict[item[0]] = item[1]

    return dict


list_of_tuples = [(1, 'apple'), (2, 'banana'), (4, 'durian'), (8, 'orange'), (3, 'peach')]

# print(convert_to_dict(list_of_tuples))