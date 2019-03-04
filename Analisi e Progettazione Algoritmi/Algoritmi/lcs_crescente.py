import sys
import numpy as np

X = [3,4,9,1]
Y = [5,3,8,9,10,2,1]

C = np.zeros(shape=(len(X), len(Y)))

# Risposta: [3,9], length = 2

for i in range(len(X)):
    for j in range(len(Y)):
        if(X[i] != Y[j]):
            C[i][j] = 0
        else:
            max = 0
            for h in range(i - 1):
                for k in range(j - 1):
                    if (C[h][k] > max and X[k] < X[i]):
                        max = C[h][k]
            C[i][j] = max + 1

maxtot = 0
for i in range(len(X)):
    for j in range(len(Y)):
        if (C[i][j] > maxtot):
            maxtot = C[i][j]

print(maxtot)