# q3a.py
# Name: 
# Email ID:

def read_weather_data(filename):
    """
    Reads weather data from a file and organizes it into a dictionary.

    Args:
        filename (str): The name of the file to read.

    Returns:
        dict: A dictionary where keys are city names and values are lists of 
              weather record tuples. Each tuple is in the format:
              ((year, month, day), max_temp, min_temp, precipitation).
    """
    # Modify the code below.
    weather_mapping = {}
    with open(filename, 'r') as weather_data:
        for line in weather_data:
            date, city, max_temp, min_temp, percipitation = line.strip().split("|")
            max_temp = float(max_temp)
            min_temp = float(min_temp)
            percipitation = float(percipitation)
            year, month, date = date.split("-")
            year = int(year)
            month = int(month)
            date = int(date)
            if city not in weather_mapping.keys():
                weather_mapping[city] = []
            weather_mapping[city].append(((year, month, date), max_temp, min_temp, percipitation))

    return weather_mapping
