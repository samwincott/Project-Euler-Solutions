"""
This solves problem 14 of the project euler problems.
Found at https://projecteuler.net/problem=14
"""

def main():
    """This is an improvement on my previous solution."""
    n_to_one_dist = {1: 1}
    longest_starting = 1
    longest_length = 1

    for starting in range(1, 1000001):
        number = starting
        length = 1
        while number not in n_to_one_dist:
            if number % 2 == 0:
                number /= 2
            else:
                number = (3 * number) + 1
            if number in n_to_one_dist:
                length += n_to_one_dist[number]
                n_to_one_dist[starting] = length
                if length > longest_length:
                    longest_starting = starting
                    longest_length = length
                break
            length += 1
    print("The answer is %i" % (longest_starting))

main()
