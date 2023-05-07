import numpy as np
import random
import funciones as fc

class Tablero:
    dimensiones = (10,10)
    tablero = np.full((10,10), " ")
    tablero_oculto = fc.generar_barcos_aleatorios()

    def __init__(self, id_jugador):
        self.id_jugador = id_jugador
    
    def disparar(self, fila, columna):
        if self.tablero[fila][columna] == "O":
            self.tablero[fila][columna] = "X"
            self.tablero_oculto[fila][columna] = "X"
            print("Tocado")
        else:
            self.tablero[fila][columna] = "-"
            self.tablero_oculto[fila][columna] = "-"
            print("Agua")

jugador = Tablero("jugador")
maquina = Tablero("maquina")
