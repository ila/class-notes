# compitino 13 novembre 2017, versione A

# due sequenze di numeri interi
# funzione f che associa a ogni numero un colore R, G, B
# trovare la più lunga sottosequenza decrescente senza numeri con lo stesso colore adiacenti

import numpy as np


def f(n):
    if n == 0:
        return 'R'
    elif n % 2 == 1:
        return 'G'
    return 'B'


# s1 = [3, 6, 4, 7, 4, 7, 9, 10, 8, 2, 0]
s1 = [0, 2, 8, 10, 9, 7, 4, 7, 4, 6, 3]

# s2 = [11, 7, 7, 4, 2, 1, 4, 0]
s2 = [0, 4, 1, 2, 4, 7, 7, 11]

# s1 = [2, 4, 7, 11, 21, 14, 1]
# s2 = [2, 7, 4, 23, 21, 14, 1, 8]

c = np.zeros((len(s1), len(s2)), int)
# inizializzazione della matrice

m = 0  # massimo
for i in range(0, len(s1)):
    for j in range(0, len(s2)):
        if s1[i] != s2[j]:
            c[i, j] = 0
        else:
            temp = 0
            for h in range(0, i):
                for k in range(0, j):
                    if (s1[h] < s1[i]) and (f(s1[h]) != f(s1[i])) and (c[h, k] > temp):
                        temp = c[h, k]
            c[i, j] = 1 + temp
        if c[i, j] > m:
            m = c[i, j]

print(c)
print("\nMassimo: ", m)
