from Jugador import Jugador

class Juego:

    def __init__(self):
        self.jugador1 = None
        self.jugador2 = None

    def juego_nuevo(self):
        verificador = False
        while not verificador
            ancho = input("Decidan, el ancho de los tableros: ")
            alto = input("Decidan, el alto de los tableros: ")
            if ancho.isnumeric() and alto.isnumeric() and ancho < 28 and alto < 28:
                verificador = True
                ancho = int(ancho)
                alto = int(alto)
        self.jugador1 = Jugador(ancho, alto)
        self.jugador2 = Jugador(ancho, alto)


    def cambiar_turno(self):
        gano = False
        while not gano:
            termino = jugador1.
        
