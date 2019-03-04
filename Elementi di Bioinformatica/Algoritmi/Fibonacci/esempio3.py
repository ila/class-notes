#!/usr/bin/env python3 

with open('limit.txt') as f:
    contents = f.readlines()

limit = int(contents[0].split()[0])
print(limit)
print(contents)

fib = [1,1]
for x in range(2, limit):
    fib.append(fib[-1] + fib[-2])

print(fib)