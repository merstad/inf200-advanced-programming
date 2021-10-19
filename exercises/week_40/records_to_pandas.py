"""
Example solution for converting records to a Pandas dataframe.
"""

__author__ = "Hans Ekkehard Plesser, NMBU"

import pandas as pd

student_records = [{'name': 'Joe', 'age': 22, 'phone': '12345678'},
                   {'name': 'Pia', 'age': 24, 'phone': '23456789'},
                   {'name': 'Even', 'age': 21, 'phone': '34567890'},
                   {'name': 'Abdul', 'age': 23, 'phone': '45678901'}]

students = pd.DataFrame.from_records(student_records)

print(23 * '-')
print('Student DataFrame')
print(23 * '-')
print(students)
print(23 * '-')

print()
print('Mean age of students is', students.age.mean(), 'years.')
