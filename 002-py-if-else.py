#!/usr/bin/env python3
# HackerRank Python
# 002. Python If-Else
# task: Given an integer, n, perform the following conditional actions:
#   > if n is odd, print 'Weird'
#   > if n is even and in the inclusive range of 2 to 5, print 'Not Weird'
#   > if n is even and in the inclusive range of 6 to 20, print 'Weird'
#   > if n is even and greater than 20, print 'Not Weird'
# input: A single line containing a positive integer, n.
# constraints: 1 <= n <= 100
# output: Print 'Weird' if the number is weird, otherwise print 'Not Weird'.
# sample_input: 3
# sample_output: Weird


N = int(input())
if N % 2 == 1:
    # N is odd
    print('Weird')
else:
    # N is even
    if N >= 2 and N <= 5:
        print('Not Weird')
    elif N >= 6 and N <= 20:
        print('Weird')
    elif N > 20:
        print('Not Weird')
