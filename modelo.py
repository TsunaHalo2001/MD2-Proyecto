# -*- coding: cp1256 -*-

import networkx as nx
from collections import defaultdict

class Modelo:
    def __init__(self):
        self.G = nx.Graph()
        self.grafo = defaultdict(list)
        self.num_vertices = 0
        self.num_aristas = 0
        self.estado = 0

        self.V = 0
        self.T = 0
        self.S = 0
        self.P = 0

    def agregar_arista(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)  # Si el grafo es no dirigido

    def preparar_grafo(self):
        # A?adir vértices al grafo
        for i in range(self.num_vertices):
            self.G.add_node(i)

        # A?adir aristas al grafo
        for u in self.grafo:
            for v in self.grafo[u]:
                self.G.add_edge(u, v)

    def get_grafo(self):
        return self.grafo

    def get_num_vertices(self):
        return self.num_vertices

    def get_num_aristas(self):
        return self.num_aristas
    
    def get_grado_vertice(self, u):
        return len(self.grafo[u])
    
    def get_circuito_euleriano(self):
        # Verificar si el grafo tiene un circuito euleriano
        if nx.is_eulerian(self.G):
            return True

        for u in self.grafo:
            if self.get_grado_vertice(u) % 2 != 0 or len(self.grafo) == 0:
                return False

        return True
    
    def get_camino_euleriano(self):
        # Verificar si el grafo tiene un camino euleriano
        if nx.has_eulerian_path(self.G):
            return True

        contador = 0
        for u in self.grafo:
            if self.num_vertices > len(self.grafo):
                return False
            if self.get_grado_vertice(u) % 2 != 0:
                contador += 1

        return contador == 2

    def get_circuito_hamiltoniano(self):
        if self.num_vertices < 3:
            return False
        contador = 0
        if not nx.is_connected(self.G):
            return False
        for u in self.grafo:
            if self.get_grado_vertice(u) == 2:
                contador += 1

        if contador == self.num_vertices:
            return True
            
    def get_camino_hamiltoniano(self):
        if self.num_vertices < 2:
            return False
        contador = 0
        contador1 = 0
        if not nx.is_connected(self.G):
            return False
        for u in self.grafo:
            if self.get_grado_vertice(u) >= 2:
                contador += 1
            if self.get_grado_vertice(u) == 1:
                contador1 += 1

        if contador == self.num_vertices or (contador == self.num_vertices - 1 and contador1 == 1):
            return True
        
    def buscar_camino_mas_corto(self, u, v):
        # Buscar el camino m?s corto entre dos vértices
        try:
            camino = nx.shortest_path(self.G, source=u, target=v)
            return camino
        except nx.NetworkXNoPath:
            return False
        
    def generarCadena(self, cadena):
        if not cadena:
            return self.S == ''
        cadenas = []

        for i in range(len(self.P)):
            no_terminal = self.P[i][0]
            producciones = self.P[i][1:]
            if no_terminal in cadena:
                for produccion in producciones:
                    nueva_cadena = cadena.replace(no_terminal, produccion, 1)
                    cadenas.append(nueva_cadena)

        return cadenas
    
    def generarVocabulario(self, n):
        cadenas = [self.S]

        for i in range(n):
            for cadena in cadenas:
                for i in range(len(self.P)):
                    if self.P[i][0] in cadena:
                        cadenas.remove(cadena)
                cadenas_generadas = self.generarCadena(cadena)
            cadenas += cadenas_generadas

        return cadenas
    
    def perteneceLenguaje(self, cadena):
        # Se determina la cantidad de iteraciones que se necesita para la cadena ingresada
        iteraciones = 0

        for i in range(len(self.P)):
            for j in range(len(self.P[i])):
                if self.P[i][0] in self.P[i][j]:
                    continue
                iteraciones = len(self.P[i][j]) * len(cadena)

        # Se genera el vocabulario
        vocabulario = self.generarVocabulario(iteraciones)
        for i in vocabulario:
            if i == cadena:
                return True
        
        return False
    
    def reset(self):
        self.G.clear()
        self.grafo.clear()
        self.num_vertices = 0
        self.num_aristas = 0
        self.estado = 0

        self.V = 0
        self.T = 0
        self.S = 0
        self.P = 0
            