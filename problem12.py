"""
This solves problem 12 of the project euler problems.
Found at https://projecteuler.net/problem=12
This solution is adapted from the solution found at:
http://code.jasonbhill.com/sage/project-euler-problem-12/
"""

def number_of_divisors(number):
    """Returns the number of even divisors for a given number."""
    if number % 2 == 0:
        number = number/2
    divisors = 1
    count = 0
    while number % 2 == 0:
        count += 1
        number = number/2
    divisors = divisors * (count + 1)
    factor = 3
    while number != 1:
        count = 0
        while number % factor == 0:
            count += 1
            number = number/factor
        divisors = divisors * (count + 1)
        factor += 2
    return divisors

def triangular_index(factor_limit):
    """Finds the index of a triangular number given the number of divisors it should have."""
    index = 1
    lnum, rnum = number_of_divisors(index), number_of_divisors(index+1)
    while lnum * rnum < factor_limit:
        index += 1
        lnum, rnum = rnum, number_of_divisors(index+1)
    return index

def main():
    """Finds and prints the first triangle number with over 500 divisors."""
    index = triangular_index(500)
    triangle = (index * (index + 1)) / 2
    print("The answer is %i" % (triangle))

main()
