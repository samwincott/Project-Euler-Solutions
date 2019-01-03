"""
This solves problem 2 of the project euler problems.
Found at https://projecteuler.net/problem=2
"""

def fibonacci(n):
    """Computes the nth fibonacci number."""
    a = 1
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for _ in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b

def main():
    """
    Gets all fibonacci numbers less than 4,000,000
    and computes the sum of all even ones.
    """
    temp_answer = 0
    counter = 1
    total = 0
    while temp_answer <= 4000000:
        temp_answer = fibonacci(counter)
        if temp_answer % 2 == 0:
            total += temp_answer
        counter += 1

    print("Answer:", total)

main()
