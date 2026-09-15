def compute_avg_height(heights):
    total_heights = 0
    persons = heights.split(",")
    num_pax = heights.split(":")
    for person in persons:
        if len(person.split(":")) == 2:
            total_heights += float(person.split(":")[1].replace("m", ""))
            
    return total_heights / (len(num_pax) - 1)

print(compute_avg_height("Jonathan Li:1.75m, Lim, Josepheine : 1.59m, George Khoo:   1.7m"))