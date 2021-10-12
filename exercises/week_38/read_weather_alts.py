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
    with open(filename, encoding='latin-1') as wfile:
        wfile.readline()  # skip header
        line = wfile.readline()
        while line:
            tokens = line.split(';')
            day, month, year = tokens[0].split('.')
            record = {'Date': f'{int(year):04d}-{int(month):02d}-{int(day):02d}',
                      'T_avg': float(tokens[1]),
                      'T_min': float(tokens[2]),
                      'T_max': float(tokens[3]),
                      'Glob': float(tokens[4]),
                      'UV_rel': float(tokens[5])}
            data.append(record)
            line = wfile.readline()
    return data


# same as above, but with assignment operator
def read_weather2(filename):
    data = []
    with open(filename, encoding='latin-1') as wfile:
        wfile.readline()  # skip header
        while line := wfile.readline():
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


# more compact record construction
def read_weather3(filename):
    data = []
    DATA_COLUMNS = ('T_avg', 'T_min', 'T_max', 'Glob', 'UV_rel')
    with open(filename, encoding='latin-1') as wfile:
        wfile.readline()  # skip header
        while line := wfile.readline():
            tokens = line.split(';')
            day, month, year = tokens[0].split('.')
            record = {'Date': f'{int(year):04d}-{int(month):02d}-{int(day):02d}'}
            record.update({c: float(v) for c, v in zip(DATA_COLUMNS, tokens[1:])})
            data.append(record)
    return data


if __name__ == '__main__':
    d = read_weather3('weather_umb_2012.csv')
    print(len(d))
    for r in d[::23]:
        print(r)
