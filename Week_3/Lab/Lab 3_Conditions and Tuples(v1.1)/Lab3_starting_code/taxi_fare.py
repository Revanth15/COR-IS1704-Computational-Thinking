import math

## Test arguments
# flag_down_fare = 3.50
# rate_400m = 0.22
# rate_350m = 0.22
# distance_travelled = 11400
# peak_period = False
# between_12and6 = True
# location_surcharge_bool = True
# location_surcharge_cost = 3.00
flag_down_fare = float(input("What's the flag-downfare? $"))
rate_400m = float(input("What's the rate per 400 meters within 9.8km? $"))
rate_350m = float(input("What's the rate per 350 meters beyond 9.8km? $"))
distance_travelled = int(input("What's the distance travelled (in meters)? "))
peak_period = input("Is this ride during a peak period? [yes/no] ") == "yes"

# Consts
location_surcharge_cost = 0

total_fare = flag_down_fare
if distance_travelled < 9800:
    total_fare += math.ceil((distance_travelled - 1000) / 400) * rate_400m
else:
    total_fare += (22 * rate_400m) + (math.ceil((distance_travelled - 9800) / 350) * rate_350m)

surcharge_modifier = 1
if peak_period:
    surcharge_modifier = 1.25
else:
    between_12and6 = input("Is this ride between midnight and 6am? [yes/no] ") == "yes"
    if between_12and6:
        surcharge_modifier = 1.5

location_surcharge_bool = input("Is there any location surcharge? [yes/no] ") == "yes"
if location_surcharge_bool:
    location_surcharge_cost = float(input("What's the amount of location surcharge? $"))

total_fare = round((total_fare * surcharge_modifier) + location_surcharge_cost, 2)

print(f"The total fare is ${total_fare}")