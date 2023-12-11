import random
import numpy as np
from numpy.linalg import inv
import lecturaGrafo as lg



tamanioSucecion = 40

SIZE = 10

S = [i for i in range(SIZE)]

 
A_0 = [random.uniform(0, 1) for _ in range(SIZE)]
suma_A = sum(A_0)
A = [A_0[x]/suma_A for x in range(SIZE-1)]
A.append(1-sum(A))


P = []
for i in range (SIZE):
    fila = [random.uniform(0, 1) for _ in range(SIZE)]
    sumaFila = sum(fila)
    filaNormal = [fila[x]/sumaFila for x in range(SIZE-1)]
    filaNormal.append(1-sum(filaNormal))

    P.append(filaNormal)


U = [random.uniform(0, 1) for _ in range(tamanioSucecion)]
X = [0 for _ in range(tamanioSucecion)]




def g (u: float) -> float:
    suma = 0
    for i in range(SIZE):

        inferior = 0
        for k in range(i):
            inferior += A[k]   
        superior = inferior + A[i]

        #print("(" + str(inferior) + "," + str(superior) + "]")

        if (u > inferior) and (u <= superior):
            suma += i

    return suma



def f (i: float, u:float):

    suma = 0
    for j in range(SIZE):

        inferior = 0
        for k in range(j):
            inferior += P[i][k]
        superior = inferior + P[i][j]

        #print("(" + str(inferior) + "," + str(superior) + "]")

        if (u > inferior) and (u <= superior):
            suma += j
    return suma




if __name__ == '__main__':

    X[0] = g(U[0])

    for n in range(tamanioSucecion -1):  
        X[n+1] = f(X[n], U[n+1])

    print(X)

    grafo = lg.cargar()


