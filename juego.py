from Jugador import Jugador

class Juego:

    def __init__(self):
        self.jugador1 = None
        self.jugador2 = None
        self.punto_j1 = 0
        self.punto_j2 = 0
        self.juego_nuevo()
        self.cambiar_turno()

    def juego_nuevo(self):
        verificador = False
        while not verificador:
            ancho = input("Decidan, el ancho de los tableros: ")
            alto = input("Decidan, el alto de los tableros: ")
            if ancho.isnumeric() and alto.isnumeric() and int(ancho) < 28 and int(alto) < 28 and int(alto) * int(ancho) > 7 :
                verificador = True
                ancho = int(ancho)
                alto = int(alto)
            else:
                print("el minimo del tablero es 7 casillas (4*2, 2*4 o 3*3)")
        self.jugador1 = Jugador(ancho, alto, 1)
        while True:
            respuesta = input(self.jugador1.nombre + ". Desea colocar los barcos manualmente? (y/n)   ")
            if respuesta.lower() in ("y", "n"):
                if respuesta == "y":
                    self.jugador1.colocar_barcos()
                    break
                else:
                    self.jugador1.barcos_randoms()
                    break
            else:
                print ("Ingrese un respuesta valida porfavor")
        self.jugador2 = Jugador(ancho, alto, 2)
        while True:
            respuesta = input(self.jugador2.nombre + ". Desea colocar los barcos manualmente? (y/n)   ")
            if respuesta.lower() in ("y", "n"):
                if respuesta == "y":
                    self.jugador2.colocar_barcos()
                    break
                else:
                    self.jugador2.barcos_randoms()
                    break
            else:
                print ("Ingrese un respuesta valida porfavor")


    def cambiar_turno(self):
        while True:
            print("Turno de " + self.jugador1.nombre + "    Barcos enemigos hundidos: " + str(self.punto_j1))
            termino, punto = self.jugador2.atacar()
            if punto:
                self.punto_j1 += 1
                print (str(self.punto_j1) + " punto/s") 
            if not termino:
                print ( self.jugador2.nombre + " ha ganado" )
                break
            print ("Turno de " + self.jugador2.nombre + "    Barcos enemigos hundidos: " + str(self.punto_j2))
            termino, punto = self.jugador1.atacar()
            if punto:
                self.punto_j2 += 1
                print (str(self.punto_j2) + " punto/s")
            if not termino:
                print ( self.jugador2.nombre + " ha ganado")
                break
        while True:
            respuesta = input("Desea empezar un juego nuevo? (y/n)")
            if respuesta.lower() in ('y', 'n'):
                if respuesta.lower() == 'y':
                    self.juego_nuevo()
                    break
                else:
                    break
                
j = Juego()