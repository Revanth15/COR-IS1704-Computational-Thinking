def read_into_dict(file_name):
    dict = {}
    with open(file_name, 'r') as file:
        for row in file:
            acro, name = row.strip().split("\t")
            dict[acro] = name
    return dict

print(read_into_dict("acronyms.txt"))