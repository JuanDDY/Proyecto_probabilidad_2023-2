import numpy as np
from numpy.linalg import inv
import networkx as nx

import markovChain as mc
import lecturaGrafo


def opcion5():

    # Función para calcular el valor del corte
    def cut_value(G, partition):
        cut = 0
        for u, v in G.edges():
            if partition[u] != partition[v]:
                cut += 1
        return cut

    # Generar el grafo a partir de una matriz de adyacencia
    def generate_graph(adj_matrix):
        G = nx.from_numpy_matrix(adj_matrix)
        return G

    # Simular la cadena de Markov para MAX-CUT
    def max_cut_markov_chain(G, num_iterations, lambd):
        num_nodes = G.number_of_nodes()
        # Estado inicial: asignación aleatoria de -1 y 1 a los nodos
        state = np.random.choice([-1, 1], size=num_nodes)
        
        # Función f(σ) para calcular el valor del corte
        def f(state):
            return cut_value(G, state)
        
        # Generar la matriz de transición P
        def transition_matrix(num_nodes):
            P = np.zeros((num_nodes, num_nodes))
            for i in range(num_nodes):
                for j in range(num_nodes):
                    if i != j:
                        P[i, j] = 1 / num_nodes
            return P

        A = np.ones(num_nodes) / num_nodes  # Distribución inicial uniforme
        P = transition_matrix(num_nodes)  # Matriz de transición uniforme

        # Crear la cadena de Markov
        mc = MarkovChain(A, P)

        best_state = state.copy()
        best_cut = f(state)
        
        for _ in range(num_iterations):
            states = mc.simulate(num_nodes)
            state = np.array([states[i] for i in range(num_nodes)])
            current_cut = f(state)
            
            if current_cut > best_cut:
                best_cut = current_cut
                best_state = state.copy()
        
        return best_state, best_cut

    # Matriz de adyacencia del grafo (ejemplo)
    adj_matrix = np.zeros((60, 60))
    # Llenar la matriz de adyacencia con los datos del grafo de 60 nodos y 885 aristas

    # Generar el grafo
    G = generate_graph(adj_matrix)

    # Parámetros de la simulación
    num_iterations = 10000
    lambd = 1.0

    # Ejecutar la simulación
    best_partition, best_cut_value = max_cut_markov_chain(G, num_iterations, lambd)

    print("Mejor partición:", best_partition)
    print("Valor del mejor corte:", best_cut_value)



def iniciarPrograma():

    TAMANIO_SUCESION = 10
    grafo = []
    P = []
    A = []

    while True:
        print("0. probar cadena")
        print("1. Cargar grafo")
        print("2. Ingresar grafo")
        print("3. Generar grafo aleatorio")
        print("4. Ingresar etapas de cadena")
        print("5. Hallar corte maximo")
        opcion = input()


        if opcion == "0":

            np.random.seed(42)
            U = [np.random.uniform() for _ in range(TAMANIO_SUCESION)]
            print("U = ", U)

            X = np.zeros(TAMANIO_SUCESION, dtype=int)
            print("X = ",X)

            a = np.array([0.2, 0.5, 0.3])  # Asegúrate de que sume 1
            P = np.array([[0.5, 0.2, 0.3],
                        [0.3, 0.4, 0.3],
                        [0.2, 0.3, 0.5]])  # Cada fila debe sumar 1

            cadena = mc.MarkovChain(a, P, TAMANIO_SUCESION)
                   
            X[0] = cadena.g(U[0])

            for n in range(cadena.TAMANIO -1):  
                X[n+1] = cadena.f(X[n], U[n+1])

            print("X = ",X)
            

        elif opcion == "1":
            grafo = lecturaGrafo.cargar()
        
        elif opcion == "2":
            pass
        
        elif opcion == "3":
            #grafo = generarGrafo()
            pass
        
        elif opcion == "4":
            TAMANIO_SUCESION = int(input("ingrese el tamaño de la sucesion"))
            
        elif opcion == "5":

            opcion5()
    

    



if __name__ == '__main__':
    
    iniciarPrograma()

    


