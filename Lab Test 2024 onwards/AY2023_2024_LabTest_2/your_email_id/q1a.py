# Name:
# Email ID:


def compute_coe_rebate(car_info):
    # Modify the code below.
    car_type, no_of_days, list = car_info
    coe = int(list[0].strip("$"))
    arf = int(list[1].strip("$"))

    years_10 = 10 * 365

    coe_rebate = coe *  ((years_10 - no_of_days) / years_10)
    
    return int(coe_rebate)
