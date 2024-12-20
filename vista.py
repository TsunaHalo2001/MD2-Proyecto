# -*- coding: cp1256 -*-

import networkx as nx
import matplotlib.pyplot as plt

class Vista:
    @staticmethod
    def mostrar_mensaje(mensaje):
        print(mensaje)

    @staticmethod
    def pedir_entrada(mensaje):
        return input(mensaje)
    
    @staticmethod
    def dibujar_grafo(G):
        # Dibujar el grafo
        print(G)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", edge_color="gray")
        plt.show()