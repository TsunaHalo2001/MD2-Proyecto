# -*- coding: cp1256 -*-

class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def menu(self):
        self.vista.mostrar_mensaje("1. Ingresar grafo\n2. Ingresar gramatica\n3. Salir")
        opcion = self.vista.pedir_entrada("Ingrese una opci?n: ")
        if opcion == "1":
            self.modelo.estado = 1
        elif opcion == "2":
            self.modelo.estado = 4
        elif opcion == "3":
            self.modelo.estado = -1
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
            
            self.modelo.estado = 2
        except ValueError:
            self.vista.mostrar_mensaje("N?mero inv?lido.")
            return

    def check_grafo(self):
        self.mostrar_grafo()
        
        self.vista.mostrar_mensaje("Grafo ingresado correctamente.")
        if self.modelo.get_circuito_euleriano():
            self.vista.mostrar_mensaje("El grafo tiene un circuito euleriano.")
        elif self.modelo.get_camino_euleriano() or self.modelo.get_circuito_euleriano():
            self.vista.mostrar_mensaje("El grafo tiene un camino euleriano.")
        if self.modelo.get_circuito_hamiltoniano():
            self.vista.mostrar_mensaje("El grafo tiene un circuito hamiltoniano.")
        elif self.modelo.get_camino_hamiltoniano():
            self.vista.mostrar_mensaje("El grafo tiene un camino hamiltoniano.")

        self.modelo.estado = 3

    def elegir2vertices(self):
        self.vista.mostrar_mensaje("Para buscar el camino mas corto\nDigite -1 para salir\ningrese los vertices u y v:")
        aux = self.vista.pedir_entrada("")
        if aux == "-1":
            self.modelo.reset()
            return
        u, v = map(int, aux.split())
        if u >= self.modelo.num_vertices or v >= self.modelo.num_vertices:
            self.vista.mostrar_mensaje("Vértices inv?lidos.")
            return
        
        camino = self.modelo.buscar_camino_mas_corto(u, v)
        if not camino:
            self.vista.mostrar_mensaje("No existe camino entre {} y {}.".format(u, v))
        else:
            self.vista.mostrar_mensaje("El camino m?s corto entre {} y {} es: {}".format(u, v, camino))
        self.modelo.estado = 3

    def set_gramatica(self):
        self.modelo.V = set(self.vista.pedir_entrada("Ingrese los s?mbolos no terminales (V), separados por espacios: ").split())
        if not self.modelo.V:
            self.vista.mostrar_mensaje("No se ingresaron s?mbolos no terminales.")
            return
        self.modelo.T = set(self.vista.pedir_entrada("Ingrese los s?mbolos terminales (T), separados por espacios: ").split())
        if not self.modelo.T:
            self.vista.mostrar_mensaje("No se ingresaron s?mbolos terminales.")
            return
        self.modelo.S = self.vista.pedir_entrada("Ingrese el s?mbolo inicial (S): ")
        if self.modelo.S not in self.modelo.V:
            self.vista.mostrar_mensaje("El s?mbolo inicial no es un s?mbolo no terminal.")
            return
        self.modelo.P = []

        num_reglas = int(self.vista.pedir_entrada("Ingrese el n?mero de reglas de producci?n: "))

        for _ in range(num_reglas):
            regla = self.vista.pedir_entrada("Ingrese una regla de producci?n en el formato 'A -> B' (donde A es un no terminal y B es una producci?n): ")
            if "->" not in regla:
                self.vista.mostrar_mensaje("Formato de regla inv?lido.")
                return
            A, B = regla.split("->")
            A = A.strip()
            B = B.strip()

            if A not in self.modelo.V:
                self.vista.mostrar_mensaje("El s?mbolo no terminal {} no est? en V.".format(A))
                return
            tflag = False
            # Se verifica que el simbolo de produccion este ya en P en caso de estarlo, B se agrega a la lista de producciones
            for i in range(len(self.modelo.P)):
                if self.modelo.P[i][0] == A:
                    self.modelo.P[i].append(B)
                    print(str(self.modelo.P) + "1")
                    tflag = True
                    break
            if tflag:
                continue
            # Se agrega la regla de producci?n en formato [[Simbolo no terminal1, regla1, regla2, ...], [Simbolo no terminal2, regla1, regla2, ...]]
            self.modelo.P.append([A] + B.split())
            print(str(self.modelo.P) + "2")

        print(str(self.modelo.P) + "3")
        self.modelo.estado = 5

    def check_gramatica(self):
        self.vista.mostrar_mensaje("1. Verificar si una cadena pertenece a la gram?tica\n2. Generar cadenas de la gram?tica\n3. Salir")
        opcion = self.vista.pedir_entrada("Ingrese una opci?n: ")
        if opcion == "1":
            self.modelo.estado = 6
        elif opcion == "2":
            self.modelo.estado = 7
        elif opcion == "3":
            self.modelo.estado = 0
        else:
            self.vista.mostrar_mensaje("Opci?n inv?lida.")

    def verificar_cadena(self):
        self.vista.mostrar_mensaje("Para verificar si una cadena pertenece a la gram?tica\nDigite -1 para salir\ningrese la cadena:")
        cadena = self.vista.pedir_entrada("")
        if cadena == "-1":
            self.modelo.reset()
            return
        if self.modelo.perteneceLenguaje(cadena):
            self.vista.mostrar_mensaje("La cadena pertenece a la gram?tica.")
        elif cadena == "":
            self.vista.mostrar_mensaje("Cadena vac?a.")
        else:
            self.vista.mostrar_mensaje("La cadena no pertenece a la gram?tica.")

        self.modelo.estado = 5

    def generar_cadenas(self):
        self.vista.mostrar_mensaje("Para generar cadenas de la gram?tica\nDigite -1 para salir\ningrese la cantidad de cadenas a generar:")
        num_cadenas = int(self.vista.pedir_entrada(""))
        if num_cadenas == -1:
            self.modelo.reset()
            return
        if num_cadenas < 0:
            self.vista.mostrar_mensaje("N?mero inv?lido.")
            return
        cadenas = self.modelo.generarVocabulario(num_cadenas)
        self.vista.mostrar_mensaje("Cadenas generadas:")
        for cadena in cadenas:
            self.vista.mostrar_mensaje(cadena)

        self.modelo.estado = 5

    def mostrar_grafo(self):
        self.modelo.preparar_grafo()
        self.vista.dibujar_grafo(self.modelo.G)

    def main(self):
        if self.modelo.estado == 0:
            self.menu()
        if self.modelo.estado == 1:
            self.set_grafo()
        if self.modelo.estado == 2:
            self.check_grafo()
        if self.modelo.estado == 3:
            self.elegir2vertices()
        if self.modelo.estado == 4:
            self.set_gramatica()
        if self.modelo.estado == 5:
            self.check_gramatica()
        if self.modelo.estado == 6:
            self.verificar_cadena()
        if self.modelo.estado == 7:
            self.generar_cadenas()
        