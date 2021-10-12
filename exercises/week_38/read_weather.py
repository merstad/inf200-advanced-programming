"""
Example solution for the weather data task.

This code reads weather data from a CSV file.
"""

__author__ = 'Hans Ekkehard Plesser, NMBU'


def read_weather(filename):
    """
    Load weather data from CSV file.

    :param filename: CSV file to read.
    :return: List with one dictionary per data entry.
    """

    data = []
    with open(filename, encoding='latin-1') as w_file:
        w_file.readline()  # skip header of CSV file
        while line := w_file.readline():
            # extract information from one line and turn into dictionary
            tokens = line.split(';')
            day, month, year = tokens[0].split('.')
            record = {'Date': f'{int(year):04d}-{int(month):02d}-{int(day):02d}',
                      'T_avg': float(tokens[1]),
                      'T_min': float(tokens[2]),
                      'T_max': float(tokens[3]),
                      'Glob': float(tokens[4]),
                      'UV_rel': float(tokens[5])}
            data.append(record)
    return data


def _parse_weather_record(line):
    """
    Parse single line of weather-data CSV-file.

    This is a helper function for read_weather_comprehension().

    :param line: One line of the CSV file, not header line.
    :return: Dictionary with data from line.
    """

    tokens = line.split(';')
    day, month, year = tokens[0].split('.')
    return {'Date': f'{int(year):04d}-{int(month):02d}-{int(day):02d}',
            'T_avg': float(tokens[1]),
            'T_min': float(tokens[2]),
            'T_max': float(tokens[3]),
            'Glob': float(tokens[4]),
            'UV_rel': float(tokens[5])}


def read_weather_comprehension(filename):
    """
    Load weather data from CSV file.

    :param filename: CSV file to read.
    :return: List with one dictionary per data entry.
    """

    # With the helper from above, we can solve the problem with a single list comprehension
    return [_parse_weather_record(line)
            for line in open(filename, encoding='latin-1')
            if not line.strip().startswith('#')   # Skip comment lines in CSV file
            ]


if __name__ == '__main__':
    # Read data using both functions and compare results
    weather_a = read_weather('weather_umb_2012.csv')
    weather_b = read_weather_comprehension('weather_umb_2012.csv')

    # Check that we got the same data in both cases
    assert weather_a == weather_b, "The two functions returned different data"

    # Print a few records
    for rec in weather_a[::53]:
        print(rec)
