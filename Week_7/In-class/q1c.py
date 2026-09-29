my_str = '123'

for index in range(0, len(my_str)-1):
    n = int(my_str[index] + my_str[index+1])
    print(n)
    m = int(my_str[index:index+2])
    print(m)

# 12
# 12
# 23
# 23