# Name:
# Email ID:

def get_entry_count(filename, swimmer_name = None):
    # Replace the code below with your implementation.
    counter = 0
    with open(filename, 'r') as fle:
        for line in fle:
            name, event, s_time = line.strip().split(",")
            if swimmer_name == None:
                counter += 1
                continue
            elif name == swimmer_name:
                counter += 1
    return counter
	
