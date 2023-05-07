import numpy as np
import random
import funciones as fc

class Tablero:
    """ Clase tablero
    Dimensiones de 10x10
    y se generan siempre dos tableros, uno vacío y otro con barcos colocados."""
    dimensiones = (10,10)
    tablero = np.full((10,10), " ")
    tablero_oculto = fc.generar_barcos_aleatorios()

    def __init__(self, id_jugador):
        # Id de jugador
        self.id_jugador = id_jugador
    
    def disparar(self, fila, columna):
        # Método disparo, va modificando las filas y las columnas del tablero las coordenadas del disparo
        if self.tablero[fila][columna] == "O":
            self.tablero[fila][columna] = "X"
            self.tablero_oculto[fila][columna] = "X"
            print("Tocado")
        else:
            self.tablero[fila][columna] = "-"
            self.tablero_oculto[fila][columna] = "-"
            print("Agua")

#Objetos de la clase tablero, del jugador y de la máquina
jugador = Tablero("jugador")
maquina = Tablero("maquina")
