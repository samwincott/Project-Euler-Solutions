"""
This solves problem 16 of the project euler problems.
Found at https://projecteuler.net/problem=16
"""

def main():
    """Computes 2^1000 and sums the individual digits."""
    number = 2**1000
    answer = sum(int(digit) for digit in str(number))
    print("The answer is %i" % (answer))

main()
