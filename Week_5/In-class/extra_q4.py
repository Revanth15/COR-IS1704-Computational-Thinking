def sum_of_neighbors(input_list):
    new_list = []
    for i in range(len(input_list)):
        prev = i - 1
        next = i + 1
        total = input_list[i]
        if prev >= 0:
            total += input_list[prev]
        if next <= len(input_list) - 1:
            total+= input_list[next]
        new_list.append(total)
    return new_list

print(sum_of_neighbors([10,20,30,40,50])) # ==> [30, 60, 90, 120, 90]
print(sum_of_neighbors([23])) # ==> [23]
print(sum_of_neighbors([56,-10,25,-32])) # ==> [46, 71, -17, -7]