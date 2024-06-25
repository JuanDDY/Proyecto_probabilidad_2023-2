"""
Este codigo carga el archivo del grafo y lo vuelve un grafo con matriz de abyacencia
@author Juan David Duarte
"""

def cargar():
    archivo = open("max-cut\grafo60.txt", "r")
  
    cantidadNodos, cantidadVertices = archivo.readline().split()
    grafo = [[0 for _ in range(int(cantidadNodos))] for _ in range(int(cantidadNodos))]

    for _ in range(int(cantidadVertices)):
        vertice = archivo.readline().split()
        grafo[int(vertice[0])-1][int(vertice[1])-1] = 1
        
    archivo.close()
    return grafo