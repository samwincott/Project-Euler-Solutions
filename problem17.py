"""
This solves problem 17 of the project euler problems.
Found at https://projecteuler.net/problem=17
"""

ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def to_english(number):
    """Returns the british english wording of a given number."""
    if 0 <= number < 20:
        answer = ONES[number]
        return answer
    elif 20 <= number < 100:
        answer = TENS[number // 10]
        if number % 10 != 0:
            answer += ONES[number % 10]
        return answer
    elif 100 <= number < 1000:
        answer = ONES[number // 100] + "hundred"
        if number % 100 != 0:
            answer += "and" + to_english(number % 100)
        return answer
    elif 1000 <= number < 1000000:
        answer = ONES[number // 1000] + "thousand"
        if number % 1000 != 0:
            answer += "and" + to_english(number % 1000)
        return answer
    else:
        raise ValueError()

def main():
    """Calculates the sum of the lengths of the first 1000 numbers in word form."""
    answer = sum(len(to_english(i)) for i in range(1, 1001))
    print("The answer is %i" % (answer))

main()
