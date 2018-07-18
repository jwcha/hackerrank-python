#!/usr/bin/env python3
# HackerRank: Python
# Python: Division
# task: Read two integers and print two lines. The first line should contain
#       integer division, a // b. The second line should contain float
#       division, a / b. You don't need to perform any rounding or formatting
#       operations.
# input_format: The first line contains the first integer, a. The second line
#               the second integer, b.
# output_format: Print the two lines as described above.
# sample_input_0: "4\n3"
# sample_output_0: "1\n1.333333333"


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(int(a / b))
    print(float(a) / b)
