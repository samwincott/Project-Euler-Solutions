"""
This solves problem 3 of the project euler problems.
Found at https://projecteuler.net/problem=3
"""

def prime_factors(n):
    """Computes and returns a list of prime factors of a certain number"""
    factor_list = []
    factor_test = 2

    while n >= (factor_test / 2):
        if n % factor_test == 0:
            factor_list.append(factor_test)
            n /= factor_test
        else:
            factor_test += 1
    return factor_list

def main(large_number):
    """Prints the biggest prime factor of the large number"""
    prime_factors_list = prime_factors(large_number)
    biggest_factor = prime_factors_list[-1]

    print("The highest prime factor of %i is %i" % (large_number, biggest_factor))

main(600851475143)
