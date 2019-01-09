"""
This solves problem 14 of the project euler problems.
Found at https://projecteuler.net/problem=14
"""

def collatz_sequence(number):
    """This returns the collatz sequence of a given number."""
    sequence = []
    sequence.append(number)
    while number != 1:
        if number % 2 == 0:
            number /= 2
            sequence.append(int(number))
        else:
            number = (3 * number) + 1
            sequence.append(int(number))
    return sequence

def longest_chain():
    """
    Will return the longest collatz sequence with a starting point under 1 million.
    Will also return the starting point and the length.
    """
    longest_chain_number = 1
    longest_chain_sequence = []
    longest_chain_length = 1
    for starting_number in range(1, 1000001):
        temp_chain = collatz_sequence(starting_number)
        temp_chain_length = len(temp_chain)
        if temp_chain_length >= longest_chain_length:
            longest_chain_sequence = temp_chain
            longest_chain_number = starting_number
            longest_chain_length = temp_chain_length
    return longest_chain_sequence, longest_chain_number, longest_chain_length

def main():
    """Prints the answer to the problem."""
    longest_chain_sequence, longest_chain_number, longest_chain_length = longest_chain()
    print("""The longest chain starts at %i and is %i integers long.
             \nHere is the chain:\n%s"""
          % (longest_chain_number, longest_chain_length, longest_chain_sequence))

main()
