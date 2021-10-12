"""
Example solution for text analysis task.

This code finds the name of friends in each sentence 
of a text with specified format.
"""

__author__ = 'Hans Ekkehard Plesser, NMBU'

import re


def find_friends(statements):
    """
    Finds name of friends in a text using regex.

    Assume that each sentence begins with a name, that each name
    begins with a capital letter, and that each name is at least
    two letters long.

    :param statements: List of statements to parse for friends.
    :return: List of friend-name tuples.
    """

    # The regex contains two groups, one for each name to match.
    friend_regex = re.compile(r'^([A-Z][a-z]+)\b.*\b([A-Z][a-z]+)\b.*')

    # findall() returns a list of matches. We expect one match per sentence
    # and extract that from the list.
    return [friend_regex.findall(s)[0] for s in statements]


if __name__ == '__main__':
    stmts = ['Ali and Per are friends.',
             'Kari and Joe know each other.',
             'James has know Peter since school days.']
    print(f'{"Friendships":^23s}')
    print('-' * 23)
    for a, b in find_friends(stmts):
        print(f'{a:>10s} - {b:10s}')
