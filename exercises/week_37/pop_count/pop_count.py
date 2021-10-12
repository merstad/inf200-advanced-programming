"""
Example solution to INF200 Week 37 Task 1.

This program reads a CSV file with population data for Norwegian
municipalities and prints a table of district populations in
descending order.
"""

__author__ = "Hans Ekkehard Plesser, NMBU"

# Part 1: Collect data from file
district_population = {}
with open('norway_municipalities_2017.csv', 'r') as infile:
    header = infile.readline().strip().split(',')
    for line in infile:
        _, district, population = line.split(',')
        district_population[district] = district_population.get(district, 0) + int(population)

# Part 2: Print table
print(f'{header[1]:20s}{header[2]:>10s}')
print(30 * '-')
for district, population in sorted(district_population.items(),
                                   key=lambda s: s[1],
                                   reverse=True):
    print(f'{district:20s}{population:10d}')
