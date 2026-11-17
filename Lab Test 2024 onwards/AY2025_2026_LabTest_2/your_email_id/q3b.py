# q3b.py
# Name: 
# Email ID: 

from q3a import read_weather_data

def compare_date(start_date, end_date, check_date):
    return start_date <= check_date <= end_date

def analyze_weather_patterns(filename, start_date, end_date):
    """
    Analyzes weather data for a specific period to calculate average max 
    temperature and total precipitation.

    Args:
        filename (str): The name of the file containing weather data.
        start_date (tuple): A tuple (year, month, day) for the start of the period.
        end_date (tuple): A tuple (year, month, day) for the end of the period.

    Returns:
        dict: A dictionary where keys are city names and values are tuples:
              (number_of_records, avg_max_temp, total_precipitation).
    """
    weather_data = read_weather_data(filename)
    computed_dict = {}
    for city in weather_data:
        city_weather_readings = weather_data[city]
        total_temp = 0
        total_preciptation = 0

        no_of_reading = 0
        for reading in city_weather_readings:
            valid = compare_date(start_date,end_date, reading[0])
            if valid:
                total_temp += reading[1]
                total_preciptation += reading[3]
                no_of_reading += 1

        if no_of_reading != 0:
            computed_dict[city] = (no_of_reading, total_temp/no_of_reading, round(total_preciptation,1))
    # Modify the code below.
    return computed_dict
