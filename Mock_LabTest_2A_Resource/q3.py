def process_numbers(input_filename, output_filename):
    # Modify the code below.
    dict_map = {}
    line_counter = 1
    group_counter = 0
    max_avg = -999999
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            groups = line.strip().split("#")
            curated_list = []
            for group in groups:
                group_counter += 1
                nums = group.split(" ")
                sum = 0
                for num in nums:
                    sum += float(num)
                avg = round(sum/len(nums),1)
                if avg > max_avg:
                    max_avg = avg
                curated_list.append(str(avg))
            dict_map[line_counter] = (curated_list)
            line_counter += 1
        print(dict_map)
    with open(output_filename, 'w') as output_file:
        for item in dict_map:
            output_file.write(f"{len(dict_map[item])}: {"#".join(dict_map[item])}\n")
        output_file.write(f"Total number of groups: {group_counter}\n")
        output_file.write(f"Maximum average: {max_avg}\n")
    pass





