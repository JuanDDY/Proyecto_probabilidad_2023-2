import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigsh
import lecturaGrafo as lg

def goemans_williamson_max_cut(G, num_rounds=100):
    best_cut_size = -1
    best_partition = None

    for _ in range(num_rounds):
        # Form the Laplacian matrix
        L = nx.laplacian_matrix(G)
        n = L.shape[0]

        # Compute the eigenvalues and eigenvectors of the Laplacian matrix
        eigenvalues, eigenvectors = eigsh(L.asfptype(), k=2, which='SM')
        second_eigenvector = eigenvectors[:, 1]

        # Generate a random partition based on the sign of the second eigenvector
        partition = [1 if x >= 0 else -1 for x in second_eigenvector]

        # Compute the cut size based on the generated partition
        cut_size = 0
        for u, v in G.edges():
            if partition[u] != partition[v]:
                cut_size += 1

        # Update the best cut found so far
        if cut_size > best_cut_size:
            best_cut_size = cut_size
            best_partition = partition

    return best_partition, best_cut_size

# Ejemplo de uso
# Crear un grafo aleatorio usando NetworkX
G = lg.cargar()

# Calcular la partición y el tamaño del corte usando el algoritmo de Goemans-Williamson
partition, cut_size = goemans_williamson_max_cut(G)
print("Tamaño del corte:", cut_size)
print("Partición:", partition)