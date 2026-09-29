def do_trick(a_list):
    a_list.append(a_list[1:3] + [a_list[3]])
    print(a_list)

my_list = ['a', 'b', 'c', 'd']
do_trick(my_list) # => [a, b, c, d, [b, c ,d]], this appends a list hence why there is a list inside the list.
print(my_list) # => [a, b, c, d, [b, c ,d]] , it modifies the original list hence why this list is affected too