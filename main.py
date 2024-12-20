# -*- coding: cp1256 -*-

from modelo import Modelo
from vista import Vista
from controlador import Controlador

def main():
    modelo = Modelo()
    vista = Vista()
    controlador = Controlador(modelo, vista)
    while controlador.modelo.estado >= 0:
        controlador.main()

if __name__ == "__main__":
    main()