# Exercise 4:
    # Write a python script to print a right-angle triangle composed of alternating 0s
    # and 1s..
    # For example:
        # >>> Input number of rows: 5
        # 1
        # 01
        # 101
        # 0101
        # 10101

def print_triangle():
    n = int(input("Input number of rows: "))
    if n < 0:
        return print_triangle()
    prevChar = 0
    for i in range(1, n + 1):
        line = ""
        for i in range(1, i + 1):
            char = 0 if prevChar == 1 else 1
            line += str(char)
            prevChar = char
        print(line)