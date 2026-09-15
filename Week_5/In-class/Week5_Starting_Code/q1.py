def modify_list(my_list):
    for index in range(len(my_list)):
        x = my_list[index]
        if len(x) > 5:
            my_list[index] = x[0:5]

str_list = ["COR-IS1704", "Python", "Programming", "List"]
modify_list(str_list)
print(str_list)

# Answer
# ['COR-I', 'Pytho', 'Progr', 'List']

def modify_list(my_list):
    for element in my_list:
        if len(element) > 5:
            element = element[0:5]

str_list = ["COR-IS1704", "Python", "Programming", "List"]
modify_list(str_list)
print(str_list)

# Answer
# ["COR-IS1704", "Python", "Programming", "List"]

# The difference is that for the 1st function, it assigns the value back into the original list
# but for the second funciton, it does not do that so the elements never get assigned to the list.