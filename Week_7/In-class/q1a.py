def do_trick(a_list):
    a_list = a_list + a_list[1:3] + [a_list[3]]
    print(a_list)

my_list = ['a', 'b', 'c', 'd']
do_trick(my_list) # => [a, b, c, d, b, c ,d]
print(my_list) # => [a, b, c, d]
