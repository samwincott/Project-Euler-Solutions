"""
This solves problem 9 of the project euler problems.
Found at https://projecteuler.net/problem=9
"""

def compute():
    """Calculates a*b*c where a^2+b^2=c^2 and a+b+c=1000"""
    for a in range(1, 1000):
        for b in range(a, 1000):
            c = 1000 - a - b
            if c > 0:
                if c * c == a*a + b*b:
                    return a*b*c

def main():
    """Prints the answer."""
    answer = compute()
    print("Answer:", answer)

main()
