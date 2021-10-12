"""
Example solution to INF200 Week 37 Task 2.

This program reads a CSV file with voting data for Norwegian
parliamentary elections, computes the total number of votes
received by each party and tabulates them in descending order
of votes.
"""

__author__ = "Hans Ekkehard Plesser, NMBU"


def tabulate_party_votes(data_file_name, num_display=None):
    """
    Display total number of votes per party.

    The function also marks those parties that crossed the 4% limit.

    :param data_file_name: File containing voting data per district
    :param num_display: Number of parties to tabulate, default all
    """

    party_votes = {}
    with open(data_file_name, 'r') as v_file:
        v_file.readline()  # skip header line
        for line in v_file:
            # Find information in line
            tokens = line.split(';')
            party = tokens[6]
            votes = tokens[12]

            # Add to votes for party counted already, or add new counter.
            # votes is a string, so we need to convert it to int for counting.
            party_votes[party] = party_votes.get(party, 0) + int(votes)

    total_votes = sum(party_votes.values())
    four_percent_votes = 4 * total_votes / 100

    if num_display is None:
        num_display = len(party_votes)

    print(f'{"Party":20s}{"Votes":>10s}{"Share":>10s}')
    print(40 * '-')
    for p, v in sorted(party_votes.items(), key=lambda s: s[1], reverse=True)[:num_display]:
        # We need to multiply by 100 to get the share of votes in percent
        # In the last part we exploit that a Boolean expression that is False converts to 0
        # and one that is True to 1 when used in arithmetic expressions.
        print(f'{p:20s}{v:10d}{v/total_votes*100:9.2f}% {"***"*(v >= four_percent_votes)}')

# Now do the tabulation, first with three, then seven and finally all parties
tabulate_party_votes('2021-09-14_party distribution_1_st_2021.csv', 3)
print()

tabulate_party_votes('2021-09-14_party distribution_1_st_2021.csv', 7)
print()

tabulate_party_votes('2021-09-14_party distribution_1_st_2021.csv')
