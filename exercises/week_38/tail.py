"""
Example solution for "tail" task.

This code contains several different implementations of a tail()
function printing the last n lines of a file.
"""

__author__ = 'Hans Ekkehard Plesser, NMBU'


def tail_read(filename, n=5):
    """
    Print last lines of a file.

    This implementation reads the entire file at once.

    :param filename: Name of file to display
    :param n: Number of lines to show, default 5
    """

    # Nothing to do if n < 1
    if n < 1:
        return

    text = open(filename).read()
    lines = text.rstrip('\n').split('\n')

    # We use Python's negative indexing logic:
    # lines[-2:] gives the last two lines.
    # It is important that we do not get here if n < 1,
    # because then num_to_show would be >= 0 and we would
    # index from the beginning instead of the end.
    # The if n < 1: return above ensures this.
    num_to_show = max(-n, -len(lines))
    for line in lines[num_to_show:]:
        print(line)


# Keep last n lines in list
def tail_by_line(filename, n=5):
    """
    Print last lines of a file.

    This implementation reads the file line by line.

    :param filename: Name of file to display
    :param n: Number of lines to show, default 5
    """

    # We do not know in advance which line is the n-th last line.
    # Therefore, we buffer the last n lines in a list.
    lines = []
    with open(filename) as infile:
        while line := infile.readline():
            lines.append(line)    # append at end
            if len(lines) > n:
                lines.pop(0)      # drop at beginning of list if more than n

    # We now have the final n lines of the file in lines and can print
    for line in lines:
        print(line.rstrip('\n'))


if __name__ == '__main__':
    # Run both variants, printing the last six lines of this code
    for tail in [tail_read, tail_by_line]:
        print(42 * '-')
        print('Implementation:', tail.__name__)
        print(42 * '-')
        tail('tail.py', 6)
