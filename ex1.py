# Exercise 1:
    # Write a function sum_digits(number) to calculate and return the sum of the
    # digits of a given whole number (int) given as parameter. For example,
        # >>> print(sum_digits(1234))
        # 10

def sum_digits(number:int) -> int:
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum