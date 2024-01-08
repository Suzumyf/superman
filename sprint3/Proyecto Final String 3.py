# Estudiante: Ismael Cansignia 
"""Implementar el clásico juego de tres en raya mediante la creación de clases y métodos que modelen jugadores y el tablero de juego"""

import random
from abc import ABC, abstractmethod
# El menu del juego aparecera despues de la primera ronda.
# Clase abstracta jugador

class Jugador(ABC):
    
    def __init__(self, nombre:str, simbolo:str)-> None:
        self.nombre= nombre
        self.simbolo= simbolo 
        
    @abstractmethod
    def elegir_casilla(self)-> float:
        pass
    
# Clase jugador humano

class JugadorHumano(Jugador):
    def elegir_casilla(self, tablero):
        while True:
            try:
                entrada = input(f"{self.nombre}, ingrese la casilla en formato x,y (0,1,2): ")
                x, y = map(int, entrada.split(','))

                if 0 <= x <= 2 and 0 <= y <= 2:
                    if tablero[(x, y)] == " ":  
                        return x, y
                    else:
                        print("Esa casilla ya está ocupada. Inténtalo de nuevo.")
                else:
                    print("Por favor, ingrese números entre 0 y 2 para x e y.")
            except ValueError:
                print("Ingrese las coordenadas en el formato correcto porfavor (x,y).")


# Clase JugadorPC

class JugadorPC(Jugador):
    def elegir_casilla(self, tablero):
        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)

            if tablero[(x, y)] == " ":  
                return x, y


# clase tablero 

class Tablero:
    def __init__(self):
        self.casillas = {(x, y): " " for x in range(3) for y in range(3)}

    def marcar_casilla(self, x, y, simbolo):
        if self.es_valida(x, y):
            self.casillas[(x, y)] = simbolo
            return True
        else:
            return False

    def es_valida(self, x, y):
        return self.casillas[(x, y)] == " "

    def hay_victoria(self, simbolo):
        
        for i in range(3):
            if self.casillas[(i, 0)] == self.casillas[(i, 1)] == self.casillas[(i, 2)] == simbolo:
                return True
            if self.casillas[(0, i)] == self.casillas[(1, i)] == self.casillas[(2, i)] == simbolo:
                return True

        # Verificar diagonales
        if self.casillas[(0, 0)] == self.casillas[(1, 1)] == self.casillas[(2, 2)] == simbolo:
            return True
        if self.casillas[(0, 2)] == self.casillas[(1, 1 )] == self.casillas[(2, 0)] == simbolo:
            return True

        return False

#Activacion del juego   
def imprimir_tablero(tablero):
    for i in range(3):
        for j in range(3):
            print(tablero.casillas[(i, j)], end=" ")
        print()

def jugar_tres_en_raya():
    tablero = Tablero()
    jugadores = [JugadorHumano("Jugador", "X"), JugadorPC("Computadora", "O")]
    jugador_actual = 0
    jugando = True

    while jugando:
        imprimir_tablero(tablero)
        jugador = jugadores[jugador_actual]

        if isinstance(jugador, JugadorHumano):
            x, y = jugador.elegir_casilla(tablero.casillas)
        else:
            x, y = jugador.elegir_casilla(tablero.casillas)

        if tablero.marcar_casilla(x, y, jugador.simbolo):
            if tablero.hay_victoria(jugador.simbolo):
                imprimir_tablero(tablero)
                print(f"¡{jugador.nombre} ha ganado!")
                jugando = False
            elif all(not tablero.es_valida(i, j) for i in range(3) for j in range(3)):
                imprimir_tablero(tablero)
                print("¡Es un empate!")
                jugando = False
            else:
                jugador_actual = 1 - jugador_actual
        else:
            print("Esa casilla ya está ocupada. Inténtalo de nuevo.")

if __name__ == "__main__":
    jugar_tres_en_raya()

#Menu
def poner_nombre():
    nombre = input("Ingresa tu nombre: ")
    return nombre

def iniciar_juego(nombre):
    print(f"¡Hola, {nombre}! El juego ha empezado.")

def menu():
    nombre = None
    jugando = False
    while True:
        print("\nMENU:")
        print("1. Poner Nombre")
        print("2. Iniciar Juego")
        print("3. Salir del juego")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = poner_nombre()
            
        elif opcion == "2":
            if nombre:
                iniciar_juego(nombre)
                jugando = True
            else:
                print("Por favor, primero pon tu nombre.")
                
        elif opcion == "3":
            print("¡Muchas gracias por jugar!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

        if jugando:
            jugar_tres_en_raya()
            jugando = False

if __name__ == "__main__":
    menu()


