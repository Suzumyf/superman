import random
from abc import ABC, abstractmethod

# Clase abstracta Jugador
class Jugador(ABC):
    def __init__(self, nombre, simbolo):
        self.nombre = nombre
        self.simbolo = simbolo 
        
    @abstractmethod
    def elegir_casilla(self, tablero):
        pass
    
# Clase JugadorHumano
class JugadorHumano(Jugador):
    def elegir_casilla(self, tablero):
        while True:
            try:
                entrada = input(f"{self.nombre}, ingrese la casilla en formato x,y (0,1,2): ")
                x, y = map(int, entrada.split(','))

                if 0 <= x <= 2 and 0 <= y <= 2:
                    if tablero.es_valida(x, y):
                        return x, y
                    else:
                        print("Esa casilla ya está ocupada. Inténtalo de nuevo.")
                else:
                    print("Por favor, ingrese números entre 0 y 2 para x e y.")
            except ValueError:
                print("Ingrese las coordenadas en el formato correcto (x,y).")

# Clase JugadorPC
class JugadorPC(Jugador):
    def elegir_casilla(self, tablero):
        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)

            if tablero.es_valida(x, y):
                return x, y

# Clase Tablero
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

    def hay_victoria(self):
        # Verificar filas y columnas
        for i in range(3):
            if self.casillas[(i, 0)] == self.casillas[(i, 1)] == self.casillas[(i, 2)] != " ":
                return True
            if self.casillas[(0, i)] == self.casillas[(1, i)] == self.casillas[(2, i)] != " ":
                return True

        # Verificar diagonales
        if self.casillas[(0, 0)] == self.casillas[(1, 1)] == self.casillas[(2, 2)] != " ":
            return True
        if self.casillas[(0, 2)] == self.casillas[(1, 1)] == self.casillas[(2, 0)] != " ":
            return True

        return False
