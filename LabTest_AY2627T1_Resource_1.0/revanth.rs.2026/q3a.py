# Name: Revanth
# Email ID: revanth.rs.2026

def bike_usage(filename):
    """
    Return a dict mapping bike_id -> [number_of_trips, total_duration_min]

    Args:
        filename (str): The name of the trip file to read
    
    Returns:
        dict mapping bike_id (str) -> list[int] of the form
        [number_of_trips, total_duration_min] for that bike.
        An empty dict is returned if the file contains no trips.
    """
    # Modify the code below.
    trp_dict = {}
    with open(filename, 'r') as b_trps:
        line_counter = 1
        for line in b_trps:
            if line_counter != 1 and line.strip() != "":
                trip_id, bike_id, from_station, to_station, depart_time, duration_min = line.strip().split(",")

                if bike_id not in trp_dict.keys():
                    trp_dict[bike_id] = [0, 0]

                trp_dict[bike_id][0] += 1
                trp_dict[bike_id][1] += int(duration_min)
            line_counter += 1
    return trp_dict
