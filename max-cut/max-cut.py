import numpy as np
import cvxpy as cp
import lecturaGrafo as lg
import time


def deltaTime(end, start):
    """
    Devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed


def getTime():
    """
    Devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


start_time = getTime()

ITERACIONES = 1000000
print("iteraciones = " + str(ITERACIONES))

def goemans_williamson_max_cut(adjacency_matrix):
    n = len(adjacency_matrix)

    X = cp.Variable((n, n), symmetric=True)
    constraints = [X >> 0, cp.diag(X) == 1]
    objective = cp.Maximize(0.25 * cp.trace(adjacency_matrix @ X))
    problem = cp.Problem(objective, constraints)
    problem.solve(solver=cp.SCS)

    best_cut_size = 0
    bestcut = None

    # Repeat the rounding process multiple times
    for _ in range(ITERACIONES):
        # Se genera un vector aleatorio de tamaño n*1 con valores dados por una distribucion Normal(0,1), con n el numero de nodos
        random_vector = np.random.randn(n, 1)

        # Se retiran los ejes de longitud 1 del vector aleatorio
        # Crea una matriz que en la diagonal tiene el vector aleatorio
        diagonal_matrix = np.diag(np.squeeze(random_vector))

        # Se calcula el signo {-1, 1} que se usa para calcular el tamaño del corte
        rounded_solution = np.sign(diagonal_matrix @ X.value @ diagonal_matrix)

        # Calcula el tamaño del corte 
        cut_size = np.sum(adjacency_matrix * rounded_solution)

        # Actualiza el numero de corte maximo si encuentra uno mayor
        if cut_size > best_cut_size:
            best_cut_size = cut_size
            best_cut = rounded_solution

    return best_cut, best_cut_size


adjacency_matrix = np.array(lg.cargar())

cut, cut_size = goemans_williamson_max_cut(adjacency_matrix)
print("Best cut:", cut)
print("Best cut size:", cut_size)


end_time = getTime()

print()
print("Tiempo : " + str(deltaTime(end_time, start_time)))