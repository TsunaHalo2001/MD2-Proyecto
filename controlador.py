# -*- coding: cp1256 -*-

class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.estado = 0

    def menu(self):
        self.vista.mostrar_mensaje("1. Ingresar grafo\n2. Salir")
        opcion = self.vista.pedir_entrada("Ingrese una opci?n: ")
        if opcion == "1":
            self.estado = 1
        elif opcion == "2":
            self.estado = -1
        else:
            self.vista.mostrar_mensaje("Opci?n inv?lida.")

    def set_grafo(self):
        try:
            self.modelo.num_vertices = int(self.vista.pedir_entrada("Ingrese el n?mero de vértices: "))
            self.modelo.num_aristas = int(self.vista.pedir_entrada("Ingrese el n?mero de aristas: "))

            self.vista.mostrar_mensaje("Ingrese las aristas en el formato u v (u y v son vértices conectados por una arista):")
            for _ in range(self.modelo.num_aristas):
                u, v = map(int, self.vista.pedir_entrada("").split())
                if u >= self.modelo.num_vertices or v >= self.modelo.num_vertices:
                    self.vista.mostrar_mensaje("Vértices inv?lidos.")
                    return
                self.modelo.agregar_arista(u, v)
            
            self.estado = 2
        except ValueError:
            self.vista.mostrar_mensaje("N?mero inv?lido.")
            return

    def check_grafo(self):
        self.vista.mostrar_mensaje("Grafo ingresado correctamente.")
        if self.modelo.get_circuito_euleriano():
            self.vista.mostrar_mensaje("El grafo tiene un circuito euleriano.")
        elif self.modelo.get_camino_euleriano() or self.modelo.get_circuito_euleriano():
            self.vista.mostrar_mensaje("El grafo tiene un camino euleriano.")
        self.mostrar_grafo()
        self.estado = 0

    def mostrar_grafo(self):
        self.modelo.preparar_grafo()
        self.vista.dibujar_grafo(self.modelo.G)

    def main(self):
        if self.estado == 0:
            self.menu()
        if self.estado == 1:
            self.set_grafo()
        if self.estado == 2:
            self.check_grafo()