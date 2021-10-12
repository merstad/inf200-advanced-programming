"""
Example solution to INF200 Week 37 Task 3.

This program reads a poorly formatted text file to collect
the number of seats per election district.
"""

__author__ = "Hans Ekkehard Plesser, NMBU"

seats = {}
with open('seats_per_district.txt') as s_file:
    # skip first eight lines
    for _ in range(8):
        s_file.readline()

    while district := s_file.readline().strip():
        # skip lines with irrelevant information
        for _ in range(3):
            s_file.readline()
        seat_line = s_file.readline().strip()

        # drop information about changes in number of seats at end of line
        num_seats = seat_line.split()[0]

        seats[district] = seats.get(district, 0) + int(num_seats)

with open('seats_table.txt', 'w') as outfile:
    if len(seats) != 19:
        print(f"Reading error, got {len(seats)} districts instead of 19.", file=outfile)
    else:
        print(f"{'District':<20s}{'Seats':5s}", file=outfile)
        print("-" * 25, file=outfile)
        for district, num_seats in sorted(seats.items()):
            print(f"{district:<20s}{num_seats:5d}", file=outfile)
