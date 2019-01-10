"""
This solves problem 15 of the project euler problems.
Found at https://projecteuler.net/problem=15
"""

def factorial(number):
    """This returns the factorial of a given number."""
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

def main():
    """Calculates and prints the answer."""
    answer = factorial(40) / (factorial(20) ** 2)
    print("The answer is %i" % (answer))

main()
