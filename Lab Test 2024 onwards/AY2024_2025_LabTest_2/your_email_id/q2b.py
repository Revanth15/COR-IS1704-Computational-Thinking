# Name:
# Email ID:


def get_swim_report(filename, swimmer_name, event_name):
    # Replace the code below with your implementation.
    counter = 0
    swimmer_avg = 0
    with open(filename, 'r') as fle:
        for line in fle:
            name, event, s_time = line.strip().split(",")
            if swimmer_name == name and event == event_name:
                counter += 1
                swimmer_avg += int(s_time)
    if counter != 0:
        swimmer_avg = round(swimmer_avg/counter)
    return (counter, swimmer_avg)
        
        

