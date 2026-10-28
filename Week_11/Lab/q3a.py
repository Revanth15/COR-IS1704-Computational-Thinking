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

search_bool = input("Do you want to search for a facility? [Y|N] :")

while search_bool != "N":
    school = input("Enter the school [LKCSB|SOE|SOL|SOA|SCIS] :")
    room = input("Enter the room number :")
    print(f"{school} {room} has a capacity of {room_mapping[school][room][0]} and {'has' if room_mapping[school][room][1] == 'yes' else 'does not have'} a projector.")

    search_bool = input("\nDo you want to continue the search? [Y|N] :")
print("Thanks for using our system!")


"""
Enter the school [LKCSB|SOE|SOL|SOA|SCIS] :
Enter the room number :
SOE SR-3.1 has a capacity of 50 and has a projector.
Do you want to continue the search? [Y|N] :
"""