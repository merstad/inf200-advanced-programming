"""
Example solution for marking multiple word repetitions.

This code contains two different implementations of a mark_duplicates()
function for marking the consecutive occurrences of a word in a string.
"""

__author__ = 'Hans Ekkehard Plesser, NMBU'

import re


def mark_duplicates(text):
    """
    Marks consecutive duplicate words in a text.
    
    This implementation prints using concatenation of string.
    
    :param text: String to check for duplicates
    """

    print(text)
    last_end = 0  # index the last match ended
    duplicate_word_regex = re.compile(r'\b(\w+)\s+\1\b')
    for m in duplicate_word_regex.finditer(text):
        num_spaces = m.start() - last_end
        num_markers = m.end() - m.start()
        last_end = m.end()

        # Build part of line to next error to mark
        # end='' ensures that print() does not add any extra space
        print(' ' * num_spaces + '*' * num_markers, end='')

        # Alternative implementation with format string
        # print(f'{"*" * num_markers:>{num_spaces+num_markers}s}', end='')

    print()  # end the line


if __name__ == '__main__':
    txt = 'I saw the the red rose rose and the purple lilac lilac.'
    mark_duplicates(txt)
