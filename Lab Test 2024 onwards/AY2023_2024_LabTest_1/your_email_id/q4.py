# Name:
# Email ID:

# ###############################################################################
# The function : sort_by_latest_delivery_time() is GIVEN.
# DO NOT remove or modify the function sort_by_latest_delivery_time().
# You MUST use this function in your solution.
# ###############################################################################

def sort_by_latest_delivery_time(items):
    """
    Sorts a list of items in an increasing order of their latest_delivery_time.

    This function takes in a list of items, where each item is a tuple containing
    the item_name, destination, latest_delivery_time, travel_time of item, and sorts 
    them in ascending order of their latest_delivery_time.
    The latest_delivery_time is assumed to be the third element in each item.
	If there is more than one item with the same latest_delivery_time, this function 
    will keep them in the same order as specified in the initial list of items.

    Parameter:
        items (list): A list of items to be sorted.

    Returns: None
        Note that This function sorts the given list items and DOES NOT return a new list.

    """
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        while j >= 0 and key[2] < items[j][2]:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key

# ###############################################################################
# Check how to make them ints while unpacking
def time_difference(time_1, time_2):
    hour_1, minute_1 = time_1.strip().split(":")
    hour_2, minute_2 = time_2.strip().split(":")
    mins_gap = (int(hour_1) * 60 + int(minute_1)) -  (int(hour_2) * 60 + int(minute_2))
    return mins_gap

def update_time(time,adjustment,add_bool):
    hour, minute = time.strip().split(":")
    if add_bool:
        minute = int(minute) + adjustment
    else:
        minute = int(minute) - adjustment
    hour = int(hour)
    if minute >= 60:
        minute -= 60
        if add_bool:
            hour += 1
        else:
            hour -= 1
    if minute < 10:
        minute = "0" + str(minute)
    return f"{hour}:{minute}"

def schedule_delivery(items):
    # Replace the code below with your implementation.
    sort_by_latest_delivery_time(items)
    return_list = []
    current_time = ""
    for item in items:
        item_name, destination, latest_delivery_time, travel_time = item
        if len(return_list) == 0:
            current_time = update_time(latest_delivery_time, 30, False)
            return_list.append((item_name, destination, latest_delivery_time, current_time))
            current_time = update_time(current_time, travel_time, True)
        else:
            mins_gap = time_difference(latest_delivery_time, current_time)
            if mins_gap > 30:
                mins_gap = 30
                current_time = update_time(current_time, mins_gap, True)
            else:
                current_time = update_time(current_time, travel_time, True)

            if time_difference(latest_delivery_time,current_time) <= 0:
                current_time += "*"

            return_list.append((item_name, destination, latest_delivery_time, current_time))
            current_time = update_time(current_time.strip("*"), travel_time, True)
    return return_list
    