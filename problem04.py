"""
This solves problem 4 of the project euler problems.
Found at https://projecteuler.net/problem=4
"""

def is_palindrome(input_string):
    """Checks if a given input is a palindrome or not."""
    input_string = str(input_string)
    return bool(input_string == input_string[ : : -1])

def main():
    """Finds the biggest palindrome that is the product of two 3-digit numbers."""
    palindrome_list = []

    for x in range(100, 1000):
        for y in range(100, 1000):
            product = x * y
            if is_palindrome(product):
                palindrome_list.append(product)

    print(max(palindrome_list))

main()
