from tablero import Tablero

class Juego:

    def __init__(self):
        self.turno = None


    def cambiar_tuno():
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
