"""
Compute number of mandates for each party based on the modified Sainte-Laguë rule.

This  solution stores the number of mandates outside the ScoringEntry class.

The rule works as follows:
1. Each party receives a score equal to the number of votes received divided by 1.4.
2. All parties are sorted in descending order of scores.
3. The party with the largest score is then
   a. assigned a seat
   b. receives a new score, which is its number of votes divided by 3.
4. The process continues with point 2, successively using divisors 3, 5, 7, ..., until
   all seats have been assigned.

Note that divisors are increased independently for each party.

Expected results from this code are:

    A, H: 5 mandates each
    FRP, SP: 2 mandates each
    MDG, RØDT, SV, V: 1 mandate each

Høyre has six mandates from Akershus in total in the current Storting because they were allocated
the utjevningsmandat for Akershus.
"""

import pandas as pd
import random


class ScoringEntry:
    def __init__(self, name, votes):
        self.party = name
        self.votes = votes
        self.score = votes / 1.4
        self.next_div = 3

    def update(self):
        self.score = self.votes / self.next_div
        self.next_div += 2


def district_mandates(voting_data, num_mandates):

    num_district_mandates = num_mandates - 1

    scoring_data = [ScoringEntry(row.Party, row.Votes) for row in voting_data.itertuples()]

    # Distribute mandates, counting how many mandates are assigned to each party
    mandates = {}
    while sum(mandates.values()) < num_district_mandates:
        # Ensure data is sorted in descending order of scores
        scoring_data.sort(key=lambda r: r.score, reverse=True)

        # First entry in sorted list wins the mandate
        winner = scoring_data[0]

        # Check for tie with next
        contender = scoring_data[1]
        if winner.score == contender.score:
            if winner.votes < contender.score:
                winner = contender
            elif winner.votes == contender.votes:
                winner = random.sample([winner, contender])

        # Register mandate won
        mandates[winner.party] = mandates.get(winner.party, 0) + 1

        # Update winner entry with new score and divisor for next round
        winner.update()

    return mandates


if __name__ == "__main__":
    results_akershus = pd.read_csv('result_akershus_2021.csv')
    mandates_akershus = district_mandates(results_akershus, 19)

    for party, seats in mandates_akershus.items():
        print(f'{party:<4s}: {seats:2d} mandates')
