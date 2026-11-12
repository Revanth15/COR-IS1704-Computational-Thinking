def count_high_temperatures(temperatures):
    # Modify the code below.
    counter = 0
    for temp in temperatures:
        if temp > 37.5:
            counter += 1
    return counter


