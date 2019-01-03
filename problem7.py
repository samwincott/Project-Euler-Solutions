"""
This solves problem 7 of the project euler problems.
Found at https://projecteuler.net/problem=7
"""

def is_prime(number):
    """Returns a boolean representing whether a number is prime or not."""
    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True

def first_n_primes(number):
    """Returns a list of the first n prime numbers."""
    primes_list = []
    counter = 2
    while len(primes_list) < number:
        if is_prime(counter):
            primes_list.append(counter)
        counter += 1

    return primes_list

def main():
    """Prints the 10001st prime number."""
    nth_prime_index = 10001
    first_n_primes_list = first_n_primes(nth_prime_index)
    nth_prime_value = first_n_primes_list[-1]

    print("The number %ist prime number is %i"
          % (nth_prime_index, nth_prime_value))

main()
