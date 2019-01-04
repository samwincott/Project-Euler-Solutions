"""
This solves problem 10 of the project euler problems.
Found at https://projecteuler.net/problem=10
"""

def prime_eratosthenes(limit):
    """
    This is an implementation of the sieve of eratosthenes.
    It returns a list of primes beneath the limit.
    """
    primes_list = []
    all_numbers = [True] * limit
    all_numbers[0] = all_numbers[1] = False

    for (number, isprime) in enumerate(all_numbers):
        if isprime:
            primes_list.append(number)
            for factor in range(number * number, limit, number):
                all_numbers[factor] = False
    return primes_list

def main():
    """Sums and prints all primes beneath 2 million."""
    primes_list = prime_eratosthenes(2000000)
    total = sum(primes_list)
    print("The sum of all prime numbers beneath 2 million is %i" % (total))

main()
