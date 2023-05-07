import numpy as np
import random
from playsound import playsound
import funciones as fc
import variables as var
import time

print("Bienvenido a HUNDIR LA FLOTA")
# Se generan dos tableros con barcos y se pregunta si se quiere acceder al juego o a la demo
tablero_oculto_maquina = fc.generar_barcos_aleatorios()
tablero_oculto_jugador = fc.generar_barcos_aleatorios()
demo = input("Pulsa 1 para jugar. Pulsa cualquier otro carácter para demo.")

# Se inicia el juego
if demo == "1":
    print("Empieza el juego")
    while var.vidas > 0 and var.vidas_maquina > 0:
        print("Tu turno")
        while True:
            try:
                fila_disparo = int(input("Qué fila disparas (0-9)?"))
                if fila_disparo < 0 or fila_disparo > 9:
                    raise ValueError
                break
            except ValueError:
                print("El valor introducido no es un número del 0 al 9. Inténtalo de nuevo.")
        while True:
            try:
                columna_disparo = int(input("Qué columna disparas (0-9)?"))
                if columna_disparo < 0 or columna_disparo > 9:
                    raise ValueError
                break
            except ValueError:
                print("El valor introducido no es un número del 0 al 9. Inténtalo de nuevo.") 
        acierto_jugador = fc.disparar(fila_disparo, columna_disparo, tablero_oculto_jugador, var.tablero_jugador)
        time.sleep(1)
        playsound("disparo.mp3")
        print(var.tablero_jugador)
        if acierto_jugador == True:
            time.sleep(1)
            playsound("impacto.mp3")
            while acierto_jugador == True:
                var.vidas_maquina -= 1
                while True:
                    try:
                        fila_disparo = int(input("Qué fila disparas (0-9)?"))
                        if fila_disparo < 0 or fila_disparo > 9:
                            raise ValueError
                        break
                    except ValueError:
                        print("El valor introducido no es un número del 0 al 9. Inténtalo de nuevo.")
                while True:
                    try:
                        columna_disparo = int(input("Qué columna disparas (0-9)?"))
                        if columna_disparo < 0 or columna_disparo > 9:
                            raise ValueError
                        break
                    except ValueError:
                        print("El valor introducido no es un número del 0 al 9. Inténtalo de nuevo.")
                acierto_jugador = fc.disparar(fila_disparo, columna_disparo, tablero_oculto_jugador, var.tablero_jugador)
                time.sleep(1)
                playsound("disparo.mp3")
                print(var.tablero_jugador)
        else: 
            time.sleep(1)
            playsound("agua.mp3")
        if var.vidas_maquina == 0:
            print("Has ganado.")
            break
        print("Turno de la máquina")
        acierto_maquina = fc.disparar(random.randint(0,9), random.randint(0,9), tablero_oculto_maquina, var.tablero_maquina)
        time.sleep(1)
        playsound("disparo.mp3")
        print(tablero_oculto_maquina)
        if acierto_maquina == True:
            time.sleep(1)
            playsound("impacto.mp3")
            while acierto_maquina == True:
                var.vidas -= 1
                acierto_maquina = fc.disparar(random.randint(0,9), random.randint(0,9), tablero_oculto_maquina, var.tablero_maquina)
                time.sleep(1)
                playsound("disparo.mp3")
                print(tablero_oculto_maquina)
        else:
            time.sleep(1)
            playsound("agua.mp3")
        if var.vidas == 0:
            print("Has perdido.")
            break
else:
    print("Bienvenido a la versión demo.")
    while var.vidas > 0 and var.vidas_maquina > 0:
        print("Tu turno")
        while True:
            try:
                fila_disparo = int(input("Qué fila disparas (0-9)?"))
                if fila_disparo < 0 or fila_disparo > 9:
                    raise ValueError
                break
            except ValueError:
                print("El valor introducido no es un número del 0 al 9. Inténtalo de nuevo.")
        while True:
            try:
                columna_disparo = int(input("Qué columna disparas (0-9)?"))
                if columna_disparo < 0 or columna_disparo > 9:
                    raise ValueError
                break
            except ValueError:
                print("El valor introducido no es un número del 0 al 9. Inténtalo de nuevo.") 
        acierto_jugador = fc.disparar(fila_disparo, columna_disparo, tablero_oculto_jugador, var.tablero_jugador)
        time.sleep(1)
        playsound("disparo.mp3")
        print(var.tablero_jugador)
        if acierto_jugador == True:
            time.sleep(1)
            playsound("impacto.mp3")
            while acierto_jugador == True:
                var.vidas_maquina -= 10
                while True:
                    try:
                        fila_disparo = int(input("Qué fila disparas (0-9)?"))
                        if fila_disparo < 0 or fila_disparo > 9:
                            raise ValueError
                        break
                    except ValueError:
                        print("El valor introducido no es un número del 0 al 9. Inténtalo de nuevo.")
                while True:
                    try:
                        columna_disparo = int(input("Qué columna disparas (0-9)?"))
                        if columna_disparo < 0 or columna_disparo > 9:
                            raise ValueError
                        break
                    except ValueError:
                        print("El valor introducido no es un número del 0 al 9. Inténtalo de nuevo.")
                acierto_jugador = fc.disparar(fila_disparo, columna_disparo, tablero_oculto_jugador, var.tablero_jugador)
                time.sleep(1)
                playsound("disparo.mp3")
                print(var.tablero_jugador)
        else: 
            time.sleep(1)
            playsound("agua.mp3")
        if var.vidas_maquina == 0:
            print("Has ganado.")
            break
        print("Turno de la máquina")
        acierto_maquina = fc.disparar(random.randint(0,9), random.randint(0,9), tablero_oculto_maquina, var.tablero_maquina)
        time.sleep(1)
        playsound("disparo.mp3")
        print(tablero_oculto_maquina)
        if acierto_maquina == True:
            time.sleep(1)
            playsound("impacto.mp3")
            while acierto_maquina == True:
                var.vidas -= 10
                acierto_maquina = fc.disparar(random.randint(0,9), random.randint(0,9), tablero_oculto_maquina, var.tablero_maquina)
                time.sleep(1)
                playsound("disparo.mp3")
                print(tablero_oculto_maquina)
        else:
            time.sleep(1)
            playsound("agua.mp3")
        if var.vidas == 0:
            print("Has perdido.")
            break