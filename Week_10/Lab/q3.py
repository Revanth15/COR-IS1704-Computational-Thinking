with open("temperatures.txt", "r") as temp_list:
    for patient in temp_list:
        split_list = patient.strip().split("\t")
        name = split_list[0]
        split_list.remove(name)
        temperature_list = split_list
        print(f"{name}: {min(temperature_list)}, {max(temperature_list)}")