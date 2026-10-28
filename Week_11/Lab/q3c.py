def file_to_dict(file_name):
    graph = {}
    with open(file_name, 'r') as file:
        for line in file:
            school, room_number, capacity, has_projector = line.strip().split("\t")
            if school not in graph:
                graph[school] = {}
            graph[school][room_number] = (capacity, has_projector)

    return graph

room_mapping = file_to_dict("facilities.txt")

search_bool = input("Do you want to search for the facilities within a school? [Y|N] :")

while search_bool != "N":
    school = input("Enter the school [LKCSB|SOE|SOL|SOA|SCIS] :")
    min_capacity = int(input("Enter the minimum capacity you need:"))
    print(f"The following facilities with a capacity of {min_capacity} or above are found in {school}:")
    print("\tRoom #\tCap\tProjector?")
    print('\t' + "_" * len("Room #") + "\t" + "_" * len("Cap") + "\t" + "_" * len("Projector?"))
    for room in room_mapping[school]:
        if int(room_mapping[school][room][0]) >= min_capacity:
            print(f"\t{room}\t{room_mapping[school][room][0]}\t{room_mapping[school][room][1]}")
        
    search_bool = input("\nDo you want to search for the facilities within a school? [Y|N] :")
print("Thanks for using our system!")