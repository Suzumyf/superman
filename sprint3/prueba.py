from abc import ABC, abstractmethod

class Jugador(ABC):
    def __init__(self, nombre, simbolo):
        self.nombre = nombre
        self.simbolo = simbolo

    @abstractmethod
    def elegir_casilla(self, tablero):
        pass

class JugadorHumano(Jugador):
    def elegir_casilla(self, tablero):
        while True:
            try:
                fila = int(input(f"{self.nombre}, ingrese el número de fila (0, 1, 2): "))
                columna = int(input(f"{self.nombre}, ingrese el número de columna (0, 1, 2): "))
                if tablero[fila][columna] == " ":
                    return fila, columna
                else:
                    print("Esa casilla ya está ocupada. Inténtalo de nuevo.")
            except ValueError:
                print("Ingrese un número válido.")

class JugadorComputadora(Jugador):
    def elegir_casilla(self, tablero):
        # Aquí puedes implementar la lógica para que la computadora elija una casilla automáticamente
        pass

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)

def verificar_ganador(tablero, jugador):
    # Verificar filas y columnas
    for i in range(3):
        if all(tablero[i][j] == jugador for j in range(3)) or all(tablero[j][i] == jugador for j in range(3)):
            return True

    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2-i] == jugador for i in range(3)):
        return True

    return False

def jugar_3enRaya():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugadores = [JugadorHumano("Jugador 1", "X"), JugadorComputadora("Computadora", "O")]
    jugador_actual = 0
    jugando = True

    while jugando:
        imprimir_tablero(tablero)
        fila, columna = jugadores[jugador_actual].elegir_casilla(tablero)

        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugadores[jugador_actual].simbolo
            if verificar_ganador(tablero, jugadores[jugador_actual].simbolo):
                imprimir_tablero(tablero)
                print(f"¡{jugadores[jugador_actual].nombre} ha ganado!")
                jugando = False
            else:
                jugador_actual = 1 - jugador_actual
        else:
            print("Esa casilla ya está ocupada. Inténtalo de nuevo.")

        if all(tablero[i][j] != " " for i in range(3) for j in range(3)):
            imprimir_tablero(tablero)
            print("¡Es un empate!")
            jugando = False

jugar_3enRaya()
