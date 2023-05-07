import numpy as np
import random

def colocar_barco(barco, tablero):
    """Función para colocar un barco en el tablero.

    Args:
        barco: barco que se desea colocar.
        tamaño: tablero en el que se va a colocar.

    Returns:
        Tablero con el barco colocado.
    """
    for casilla in barco:
        tablero[casilla[0]][casilla[1]] = "O"
    return tablero

def crear_barco_random(eslora, size):
    """Función para crear un barco aleatorio.

    Args:
        eslora: tamaño de la eslora.
        tamaño: tamaño del tablero en el que se va a colocar el barco.

    Returns:
        Las coordenadas del barco generado.
    """
    barco_random = []
    fila_random = random.randint(0, size - 1)
    columna_random = random.randint(0, size - 1)
    barco_random.append((fila_random,columna_random))
    orient = random.choice(["N","S","E","O"])

    while len(barco_random) < eslora:
        if orient == "O":
            columna_random = columna_random - 1 
        elif orient == "E":
            columna_random = columna_random + 1
        elif orient == "N":
            fila_random = fila_random - 1
        elif orient == "S":
            fila_random = fila_random + 1

        if fila_random not in range(size) or columna_random not in range(size):
            fila_random = random.randint(0, size - 1)
            columna_random = random.randint(0, size - 1)
            barco_random = []
            barco_random.append((fila_random,columna_random))
            orient = random.choice(["N","S","E","O"])
        else:
            barco_random.append((fila_random,columna_random))

    return barco_random

def disparar(fila, columna, tablero_barcos, tablero_jugador):
    """Función para realizar disparos.

    Args:
        fila: fila a la que se desea disparar.
        columna: columna a la que se desea disparar.
        tablero_barcos: tablero con barcos a los que se dispara.
        tablero_jugador: tablero que se muestra en pantalla, mostrando solo los disparos.

    Returns:
        Bool: True si se ha acertado, False si se falla.
    """
    if tablero_barcos[fila][columna] == "O":
        tablero_barcos[fila][columna] = "X"
        tablero_jugador[fila][columna] = "X"
        print("Tocado")
        return True
    else:
        tablero_barcos[fila][columna] = "-"
        tablero_jugador[fila][columna] = "-"
        print("Agua")
        return False

def generar_barcos_aleatorios():
    """Función para generar un tablero con 4 barcos de 1 de eslora, 3 barcos de 2 de eslora, 2 barcos de 3 de eslora y un barco de 4 de eslora.

    Returns:
        Tablero con dichos barcos colocados.
    """
    tablero = np.full((10,10), " ")
    lista_barcos = []

    while len(lista_barcos) < 4:
        barco_random1 = crear_barco_random(1, 10)
        if not hay_solapamiento(barco_random1, lista_barcos):
            lista_barcos.append(barco_random1)

    while len(lista_barcos) < 7:
        barco_random2 = crear_barco_random(2, 10)
        if not hay_solapamiento(barco_random2, lista_barcos):
            lista_barcos.append(barco_random2)

    while len(lista_barcos) < 9:
        barco_random3 = crear_barco_random(3, 10)
        if not hay_solapamiento(barco_random3, lista_barcos):
            lista_barcos.append(barco_random3)

    while len(lista_barcos) < 10:
        barco_random4 = crear_barco_random(4, 10)
        if not hay_solapamiento(barco_random4, lista_barcos):
            lista_barcos.append(barco_random4)

    for barco in lista_barcos:
        colocar_barco(barco, tablero)

    return tablero

def hay_solapamiento(barco, lista_barcos):
    """Función que comprueba si hay un barco ya colocado en las coordenadas del tablero.

    Args:
        barco: barco que se desea comprobar.
        lista_barcos: lista de barcos ya colocados.

    Returns:
        Bool: True si ya hay barco, False en caso contrario.
    """
    for coord in barco:
        for barco in lista_barcos:
            if coord in barco:
                return True
    return False