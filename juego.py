from tablero import Tablero

class Juego:

    def __init__(self):
        self.turno = None
        self.jugadores = []

    letras_a_numeros = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "D" : 4,
    "E" : 5,
    "F" : 6,
    "G" : 7,
    "H" : 8,
    "I" : 9,
    "J" : 10,
    "K" : 11,
    "L" : 12,
    "M" : 13,
    "N" : 14,
    "Ñ" : 15,
    "O" : 16,
    "P" : 17,
    "Q" : 18,
    "R" : 19,
    "S" : 20,
    "T" : 21,
    "U" : 22,
    "V" : 23,
    "W" : 24,
    "X" : 25,
    "Y" : 26,
    "Z" : 27
    }

    def cambiar_turno(self):
        self.turno = True
        while verificar_barcos():
            if self.turno:
                self.turno = False
                X = input()
                Y = input()
                lanzar(x, y)
            else:
                self.turno = True
                X = input()
                Y = input()
                lanzar(x, y)
