#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='Fibonacci.')
parser.add_argument('limit', metavar='N', type=int, nargs=1, help='How many fibonacci numbers to compute')
args = parser.parse_args()

def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(args.limit[0] - 1))