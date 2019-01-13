"""
This solves problem 20 of the project euler problems.
Found at https://projecteuler.net/problem=20
"""

def factorial(number):
    """Returns the factorial of a number."""
    total = 1
    for factor in range(2, number + 1):
        total *= factor
    return total

def main():
    """Calculates and prints the sum of the digits of 100 factorial."""
    result = factorial(100)
    answer = sum(int(digit) for digit in str(result))
    print("The answer is %i" % (answer))

main()
