def process_numbers(input_filename, output_filename):
    # Modify the code below.
    graph = {}
    line_counter = 1
    group_counter = 0
    max_avg = -999999999999999

    with open(input_filename, 'r') as input_file:
        for line in input_file:
            groups = line.strip().split("#")
            group_avg_list = []

            for group in groups:
                group_counter += 1
                nums = group.split(" ")
                sum = 0

                for num in nums:
                    sum += float(num)

                avg = round(sum/len(nums),1)

                if avg > max_avg:
                    max_avg = avg

                group_avg_list.append(str(avg))

            graph[line_counter] = (group_avg_list)
            line_counter += 1


    with open(output_filename, 'w') as output_file:
        for item in graph:
            output_file.write(f"{len(graph[item])}: {"#".join(graph[item])}\n")
        output_file.write(f"Total number of groups: {group_counter}\n")
        output_file.write(f"Maximum average: {max_avg}\n")





