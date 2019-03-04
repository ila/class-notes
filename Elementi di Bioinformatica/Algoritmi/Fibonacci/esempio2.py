#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='Fibonacci.')
parser.add_argument('limit', metavar='N', type=int, nargs=1, help='How many fibonacci numbers to compute')
args = parser.parse_args()

def fib():
    a,b = 1,1 # i primi due numeri sono 1
    while True:
        yield a # questo iteratore deve buttare il valore di a e aggiornare i valori di a e b
        print((str) (a) + ',' + (str) (b))
        a,b = b, a + b # a diventa b, e b diventa a+b

# con yield python capisce che a è un "iteratore"

# enumerate prende il generatore e me lo enumera. Prende una lista e restituisce le coppie indice - valore
for index, f in enumerate(fib()):
    if index == args.limit[0] -1:
        break