# !/usr/bin/env python3

# implementazione in Python dell'algoritmo di Fibonacci

fib = [1, 1]
# gli array sono dinamici
# primi 10 numeri della sequenza

for x in range(2, 10)
	fib.append(fib[-1] + fib[-2])
	# append aggiunge a una lista
	# -1 e -2 rappresentano l'ultimo e il penultimo elemento

print(fib)


# variante con argomento in linea di comando

import argparse
# libreria standard di Python per la gestione degli argomenti in linea di comando

parser = argparse.ArgumentParser(descrption = "Fibonacci")
parser.addArgument('limit', metavar = 'N', type = int, nargs = 1, help = "How many Fibonacci numbers to compute")
args = parser.parse_args()

for x in range(2, 10)
	fib.append(fib[-1] + fib[-2])

print(fib)


# variante con funzione

parser = argparse.ArgumentParser(descrption = "Fibonacci")
parser.addArgument('limit', metavar = 'N', type = int, nargs = 1, help = "How many Fibonacci numbers to compute ")
args = parser.parse_args()

def fib(n):
	if n <= 1:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)

print(fib(args.limit[0] - 1))


# variante con iteratore
# gli iteratori sono utili per gestire liste molto grandi di cui interessa un elemento solo alla volta

parser = argparse.ArgumentParser(descrption = "Fibonacci")
parser.addArgument('limit', metavar = 'N', type = int, nargs = 1, help = "How many Fibonacci numbers to compute ")
args = parser.parse_args()

# definizione di funzione
def fib():
	a, b = 1, 1
	while True:
		yeld a
		# yeld ritorna il valore di a senza uscire dalla funzione
		# yeld viene usata con i generatori
		# funzione che potenzialmente genera un numero infinito di valori
		a, b = b, a + b

# enumerate restituisce le coppie indice-valore da una lista

for index, f in enumerate(fib()):
	print(f)
	if index == args.limit[0] - 1:
		break


# variante con apertura da file

with open('limit.txt') as f:
	contents = f.readLines()
	# legge l'intero contenuto e lo salva in memoria
	# with open apre una parte limitata di codice e all'uscita della with il file viene automaticamente chiuso
	# in caso lancia un'eccezione

limit = int(contents[0].split()[0])
print(limit)
print(contents)








