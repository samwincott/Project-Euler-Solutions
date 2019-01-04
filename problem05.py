"""
This solves problem 5 of the project euler problems.
Found at https://projecteuler.net/problem=5
"""

def greatest_common_denominator(a, b):
    """Returns the greatest common denominator of a and b."""
    while b:
        a, b = b, a % b

    return a

def lowest_common_multiple(a, b):
    """Returns the lowest common multiple of a and b."""
    gcd = greatest_common_denominator(a, b)
    lcm = (a * b) / gcd

    return lcm

def main():
    """Determines the smallest number that is divisible by all numbers from 1 to 20."""
    answer = 1
    for i in range(1, 21):
        answer = lowest_common_multiple(answer, i)

    print("The answer is %i" % (answer))

main()
