import random
import numpy as np
from numpy.linalg import inv 
from numpy.polynomial.polynomial import Polynomial 

SIZE = 5
S = [i for i in range(SIZE)]
A = [random.uniform(0, 1) for _ in range(SIZE)]
U = [random.uniform(0, 1) for _ in range(SIZE)]

print(S)
print(U)

for k in range(-1):
    print(A[k])

print("CAca")

def g(u: float) -> float:
    suma = 0
    for i in range(SIZE):

        inferior = 0
        for k in range(i-1):
            inferior += A[k]
            
        superior = inferior + A[i]

        if (u > inferior) and (u <= superior):
            suma += i

    return suma



if __name__ == '__main__':

    h = random.uniform(0, 1)
    print(h)