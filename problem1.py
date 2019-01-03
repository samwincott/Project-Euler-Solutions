"""
This solves problem 1 of the project euler problems.
Found at https://projecteuler.net/problem=1
"""

def sum_of_multiples(multiples_of, target):
    """
    Computes the sum of all the multiples of certain numbers less than a target
    For example the sum of all multiples of 3 and 5 beneath 1000
    """
    total = 0
    for counter in range(target):
        for multiple in multiples_of:
            if counter % multiple == 0:
                total += counter
                break
    return total

print("Answer:", sum_of_multiples([3, 5], 1000))
