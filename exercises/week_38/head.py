"""
Example solution for "head" task.

This code contains several different implementations of a head()
function printing the first n lines of a file.
"""

__author__ = 'Hans Ekkehard Plesser, NMBU'


def head_read(filename, n=5):
    """
    Print first lines of a file.

    This implementation reads the entire file at once.

    :param filename: Name of file to display
    :param n: Number of lines to show, default 5
    """

    text = open(filename).read()
    lines = text.split('\n')
    num_to_show = min(n, len(lines))  # avoid problem if fewer than n lines
    for line in lines[:num_to_show]:
        print(line)


def head_readlines(filename, n=5):
    """
    Print first lines of a file.

    This implementation reads the entire file using readlines().

    :param filename: Name of file to display
    :param n: Number of lines to show, default 5
    """

    lines = open(filename).readlines()
    num_to_show = min(n, len(lines))
    for line in lines[:num_to_show]:
        # strip only LF, otherwise we would remove indentation
        print(line.rstrip('\n'))


def head_read_by_line(filename, n=5):
    """
    Print first lines of a file.

    This implementation reads the file one at a time.

    :param filename: Name of file to display
    :param n: Number of lines to show, default 5
    """
    with open(filename) as infile:
        # It is important not to strip() here, otherwise we would
        # stop at the first empty line in the file:
        # - When reading and empty line, readline() returns '\n',
        #   which is not an empty string and thus converts to True.
        # - At the very end of the file, readline() returns '',
        #   which converts to False.
        line = infile.readline()
        while n > 0 and line:
            print(line.rstrip('\n'))
            line = infile.readline()
            n -= 1


def head_read_by_line_compact(filename, n=5):
    """
    Print first lines of a file.

    This is almost identical to head_read_by_line(), but
    using the assignment (walrus) operator leads to more
    compact code.

    :param filename: Name of file to display
    :param n: Number of lines to show, default 5
    """

    with open(filename) as infile:
        while n > 0 and (line := infile.readline()):
            print(line.strip('\n'))
            n -= 1


if __name__ == '__main__':
    # Run all variants, printing the first four lines of this code
    for head in [head_read, head_readlines, head_read_by_line, head_read_by_line_compact]:
        print(42 * '-')
        print('Implementation:', head.__name__)
        print(42 * '-')
        head('head.py', 4)
