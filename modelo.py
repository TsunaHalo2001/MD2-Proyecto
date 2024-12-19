# -*- coding: cp1256 -*-

import networkx as nx
from collections import defaultdict

class Modelo:
    def __init__(self):
        self.G = nx.Graph()
        self.grafo = defaultdict(list)
        self.num_vertices = 0
        self.num_aristas = 0

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
            