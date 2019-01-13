"""
This solves problem 17 of the project euler problems.
Found at https://projecteuler.net/problem=17
"""

import datetime

def main():
    """
    Calculates and prints the number of sundays that fell on the first
    of the month between 01/01/1900 and 31/12/2000.
    """
    sundays = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            date = datetime.date(year, month, 1)
            if date.weekday() == 6:
                sundays = sundays + 1
    print("The answer is %i sundays" % (sundays))

main()
