# Exercise 3:
    # Write a function to_base10(binary) that take a binary number (base 2),
    # convert it into a decimal number (base 10) and return the base 10 value
    # The binary number 10001011 represents the number 139, whereas the number
    # 11111111 represents 255.

def to_base10(binary:str) -> int:
    res = 0
    for index, x in enumerate(binary[::-1]):
        res = res + int(x) * pow(2, index)
    return res