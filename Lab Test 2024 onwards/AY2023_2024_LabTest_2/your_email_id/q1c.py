# Name:
# Email ID:

from q1a import compute_coe_rebate
from q1b import compute_parf_rebate
#18m
def get_highest_value(car_info_list):
    # Modify the code below.

    car_value_list = []

    for car in car_info_list:
        coe_rebate = compute_coe_rebate(car)
        parf = compute_parf_rebate(car)

        car_value_list.append(coe_rebate + parf)

    max_value = max(car_value_list)
    index = car_value_list.index(max_value)
    car_name = car_info_list[index][0]
    return car_name
