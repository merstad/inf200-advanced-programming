"""
Example solution for converting lists to records.

This module provide several functions that convert dictionaries
containing lists of equal lengths to a list of records with data
from corresponding list positions.

Example:

    {'name': ['Joe', 'Pia', 'Even', 'Abdul'],
     'age': [22, 24, 21, 23],
     'phone': ['12345678', '23456789', '34567890', '45678901']}

    is converted to

    [{'name': 'Joe', 'age': 22, 'phone': '12345678'},
     {'name': 'Pia', 'age': 24, 'phone': '23456789'},
     {'name': 'Even', 'age': 21, 'phone': '34567890'},
     {'name': 'Abdul', 'age': 23, 'phone': '45678901'}]
"""

__author__ = "Hans Ekkehard Plesser, NMBU"


def to_records_loop(data):
    """
    Implementation using explicit loops.

    :param data: dictionary of equal-length lists
    :return: list of dictionaries
    """

    if not data:
        return []
    # From here on, we know that data is not empty.

    # Check if all lists have the same length
    keys = list(data.keys())
    num_fields = len(keys)            # number of different lists we have
    num_records = len(data[keys[0]])  # number of entries in first list
    for n in range(1, num_fields):    # compare to all other lists
        assert len(data[keys[n]]) == num_records, "Lists must have same length"

    # Now build list of records
    records = []
    for record_number in range(num_records):
        record = {}
        for key in keys:
            record[key] = data[key][record_number]
        records.append(record)

    return records


def to_records_loop_compact(data):
    """
    Implementation using explicit loop but more compact than above.
    """

    if not data:
        return []

    # Get all list lengths and compare them to first list length
    num_records_all = [len(vals) for vals in data.values()]
    assert all(nr == num_records_all[0] for nr in num_records_all), "Lists must have same length"
    num_records = num_records_all[0]

    # Build list, using dictionary comprehension to build individual records
    records = []
    for record_number in range(num_records):
        record = {key: data[key][record_number] for key in data.keys()}
        records.append(record)

    return records


def to_records_comprehesion(data):
    """
    Implemenation using list comprehesion-dictionary comprehension combo to build list.
    """

    if not data:
        return []

    # Create set of list lengths, must have only a single element
    num_records_set = set(len(vals) for vals in data.values())
    assert len(num_records_set) == 1, "Lists must have same length"

    # Get the one element of the set
    num_records = num_records_set.pop()

    # The list comprehension goes through the entries in the lists, building
    # a dictionary for each by dictionary comprehesion.
    recs = [{key: data[key][record_number] for key in data.keys()}
            for record_number in range(num_records)]

    return recs


def to_records_zip(data):
    """
    Compact implementation based on using the zip() function twice.

    Using zip() avoids the need for a record_number counter variable and is
    thus the most Pythonic way of solving the problem.
    """

    # Same test for equal list length as above, but on single line
    assert len(set(len(vals) for vals in data.values())) == 1, "Lists must have same length"

    # The (outer) list comprehension runs over all lists in parallel. For the example
    # data above, value_row will take on the following values in turn:
    #
    #   ('Joe', 22, '12345678')
    #   ('Pia', 24, '23456789')
    #   ('Even', 21, '34567890')
    #   ('Abdul', 23, '45678901')
    #
    # The (inner) dictionary comprehension then uses zip to pair the elements
    # in value_row with the corresponding list names, in case of the example
    # ('name', 'age', 'phone') to build the record.
    return [{key: value for key, value in zip(data.keys(), value_row)}
            for value_row in zip(*data.values())]


def pretty_print(list_of_dicts):
    """
    Print list of dictionaries with each dictionary one line.
    """

    # The following line works as follows:
    #
    # - repr(list_of_dicts) returns a string representation of list_of_dicts
    # - repr(list_of_dicts).replace(...) adds a line shift after each end of
    #   a dictionary in the middle of the list (the last } is followed by ],
    #   not comma.
    print(repr(list_of_dicts).replace('},', '},\n'))


if __name__ == '__main__':

    data = {'name': ['Joe', 'Pia', 'Even', 'Abdul'],
            'age': [22, 24, 21, 23],
            'phone': ['12345678', '23456789', '34567890', '45678901']}

    for converter in [to_records_loop, to_records_loop_compact,
                      to_records_comprehesion, to_records_zip]:
        print(50 * '-')
        print(f'Converter function: {converter.__name__}')
        print()
        pretty_print(converter(data))
        print()

