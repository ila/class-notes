# intestazione

# LCS con vocali e consonanti alternate

import numpy as np


def f(n):
    if n % 2 == 1:
        return 'a'
    return 'b'


s1 = [1, 4, 5, 3, 9, 11, 6, 8]
s2 = [2, 4, 5, 14, 8, 6, 6]

c = np.zeros((len(s1), len(s2)), int)
m = 0

for i in range(0, len(s1)):
    temp = 0
    for j in range(0, len(s2)):
        if (s1[i] == s2[j]) and ((f(s1[i]) != 'a' and f(c[i - 1, j - 1]) != 'b') or f(s1[i]) != 'b' and f(c[i - 1, j - 1]) != 'a'):
            c[i, j] = c[i - 1, j - 1] + 1
        else:
            c[i, j] = max(c[i - 1, j], c[i, j - 1])
        if c[i, j] > temp:
            temp = c[i, j]

    if temp > m:
       m = temp

print(c)
print("\nMassimo: ", m)

