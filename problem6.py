"""
This solves problem 6 of the project euler problems.
Found at https://projecteuler.net/problem=6
"""

def sum_of_squares(natural_number):
    """Returns the sum of the squares of the first n natural numbers."""
    total = 0
    for i in range(1, natural_number+1):
        total += i * i

    return total

def square_of_sum(natural_number):
    """Returns the square of the sum of the first n natural numbers."""
    total = sum(range(1, natural_number+1)) ** 2

    return total

def main():
    """
    Prints the difference between the sum of the squares of the first 10 natural numbers
    and the square of the sum of the first 10 natural numbers.
    """
    first_n_numbers = 10
    squares_summed = sum_of_squares(first_n_numbers)
    sum_squared = square_of_sum(first_n_numbers)
    difference = sum_squared - squares_summed

    print("The sum of the squares of the first %i natural numbers is %i\n"
          "The square of the sum of the first %i natural numbers is %i\n"
          "The sum of the squares of the first %i natural numbers is %i"
          % (first_n_numbers, squares_summed,
             first_n_numbers, sum_squared,
             first_n_numbers, difference))

main()
