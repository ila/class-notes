import numpy as np


def f(x):
    if int(x) % 5 == 0:
        return 1
    elif int(x) % 3 == 0:
        return 2
    return 3


s1 = [5, 6, 8, 10, 4, 3, 11]
s2 = [5, 6, 4, 1, 8, 10, 2]

c = np.zeros((len(s1), len(s2)), int)

for i in range(0, len(s1)):
    c[i, 0] = 0

for j in range(0, len(s2)):
    c[0, j] = 0


m = 0
for i in range(0, len(s1)):
    for j in range(0, len(s2)):
        if s1[i] != s2[j]:
            c[i, j] = 0
        else:  # lettera uguale
            temp = 0
            for h in range(0, i):
                for k in range(0, j):
                    if (s1[i] > s1[h]) and (f(s1[i]) < f(s1[h])) and (c[h, k] > temp):
                        temp = c[h, k]

            c[i, j] = 1 + temp
        if c[i, j] > m:
            m = c[i, j]

print(c)
print('\nMassimo: ', m)