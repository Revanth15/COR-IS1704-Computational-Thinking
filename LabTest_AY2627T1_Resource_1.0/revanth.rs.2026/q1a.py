# Name: Revanth
# Email ID: revanth.rs.2026

def count_problematic_trips(trips):
    """
    Return the number of problematic bus trips.

    Args:
        trips (list[tuple]): A list or tuples representnig bus trips. Each tuple 
        contains 3 elements: (route_number, number_of_passengers, delay_minutes)
    Returns:
        int: The number of problematic bus trips.
    """
    counter = 0

    for trip in trips:
        route_number, num_passengers, delay_mins = trip

        if num_passengers > 40 or delay_mins >= 10:
            counter += 1

    return counter

