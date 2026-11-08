# Name:
# Email ID:

def compute_parf_rebate(car_info):
    # Modify the code below.

    _, no_of_days, list = car_info
    arf = int(list[1].strip("$"))

    years_owned = no_of_days / 365
    rebate_percentile = 0.75
    if 5 < years_owned <= 6:
        rebate_percentile = 0.70
    elif 6 < years_owned <= 7:
        rebate_percentile = 0.65
    elif 7 < years_owned <= 8:
        rebate_percentile = 0.60
    elif 8 < years_owned <= 9:
        rebate_percentile = 0.55
    elif 9 < years_owned <= 10:
        rebate_percentile = 0.50

    return int(arf * rebate_percentile)

