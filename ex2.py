# Exercise 2:
    # Write a function pairwise_digits(number_a, number_b) that takes two
    # integers as parameters and returns a binary string where a character 1 is used if
    # the digits at the same index are the same, a 0 otherwise. Examples are given in
    # the table below.
        # Input A   Input B     Output
        # 1213      2113        ‘0011’
        # 1213      10435       ‘10010’
        # 1213      121         ‘1110’

def pairwise_digits(number_a:int, number_b:int) -> str:
    output = ""
    number_a = str(number_a)
    number_b = str(number_b)
    smaller = number_a if len(number_a) < len(number_b) else number_b
    bigger = number_b if int(smaller) == int(number_a) else number_a
    for i in range(len(smaller)):
        if smaller[i] == bigger[i]:
            output += '1'
        else:
            output += '0'
    output += '0' * (len(bigger) - len(smaller))
    return output