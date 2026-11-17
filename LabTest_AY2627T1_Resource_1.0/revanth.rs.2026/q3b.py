# Name: Revanth
# Email ID: revanth.rs.2026

def time_int(time):
    hr, min = time.split(":")
    return int(hr) * 60 * 60 + int(min) * 60

def station_balance(filename, window_start, window_end):
    """
    Return a dict mapping station -> (departures, arrivals, net)

    Args:
        filename (str): The name of the trip file to read
        window_start (str): Start of the window, 'HH:MM' (inclusive)
        window_end (str): End of the window, 'HH:MM' (inclusive)
    
    Returns:
        dict mapping station (str) -> tuple(int, int, int), where the tuple is
        (departures, arrivals, net) with net = arrivals - departures.
        Only stations with at least one departure or arrival in the window
        are included. An empty dict is returned if there are none.
    """
    # Modify the code below.
    s_bal = {}
    with open(filename, 'r') as b_trps:
        line_counter = 1
        for line in b_trps:
            if line_counter != 1 and line.strip() != "":
                trip_id, bike_id, from_station, to_station, depart_time, duration_min = line.strip().split(",")
                depart_ts = time_int(depart_time)
                start_ts = time_int(window_start)
                end_ts = time_int(window_end)
                arrival_ts = depart_ts + (int(duration_min) * 60)
                if from_station not in s_bal.keys():
                    s_bal[from_station] = [0,0,0]

                if to_station not in s_bal.keys():
                    s_bal[to_station] = [0,0,0]

                if start_ts <= depart_ts <= end_ts:
                    s_bal[from_station][0] += 1

                if start_ts <= arrival_ts <= end_ts:
                    s_bal[to_station][1] += 1

                s_bal[to_station][2] = s_bal[to_station][1] - s_bal[to_station][0]
                s_bal[from_station][2] = s_bal[from_station][1] - s_bal[from_station][0]
            line_counter += 1

    to_remove = []
    for key in s_bal.keys():
        if s_bal[key] == [0,0,0]:
            to_remove.append(key)
        else:
            s_bal[key] = tuple(s_bal[key])

    for key in to_remove:
        s_bal.pop(key)


    return s_bal
