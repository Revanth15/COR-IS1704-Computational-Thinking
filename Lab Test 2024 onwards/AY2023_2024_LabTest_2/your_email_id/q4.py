# Name:
# Email ID:

# 37
#3m
def calculate_actual_delays(list_cars, traffic_lights):
    # Replace the code below with your implementation.
    green, red = traffic_lights
    return_list = []
    lane_time_list = []
    for lane in list_cars:
        traffic_light_duration = green
        lane_delay = 0
        lane_cars = []
        for car in lane:
            no, delay = car
            traffic_light_duration = traffic_light_duration - delay
            if traffic_light_duration >= 0:
                lane_delay += delay
                lane_cars.append((no,lane_delay))
            else:
                traffic_light_duration += delay
                lane_delay += (red + delay + max(0, traffic_light_duration))
                lane_cars.append((no,lane_delay))
                if delay == green:
                    lane_delay += red
                traffic_light_duration = green
            lane_time_list.append(lane_delay)
        return_list.append(lane_cars)
    return (return_list, max(lane_time_list) // green)