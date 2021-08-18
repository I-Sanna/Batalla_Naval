import random
from celda import Celda
from barco import Barco

class Tablero:
    """ clase tablero almacena las celdas y barcos """

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

    def __init__(self):
        self.ancho = None
        self.alto = None
        self.barcos = []
        self.celdas =[[], []]
        self.establecer_tamaño()
        self.crear_tablero() 

    def establecer_tamaño(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def crear_tablero(self):
        for x in range (1, self.ancho + 1):
            for y in range (1, self.alto + 1):
                self.celdas[x][y].append(Celda())

    def colocar_barco(self, posicion_x, posicion_y):
        self.celdas[posicion_x][posicion_y].posicionar_barco()

    def lanzar(self, posicion_x, posicion_y):
        resultado = self.celdas[posicion_x][posicion_y].atacar()
        if resultado:
            print ("Hundido!!!")
        print ("Agua")
    
    def limpiar_tablero(self):
        for x in range (self.ancho):
            for y in range (self.alto):
                sacar_barco(x, y)
            
    def aleatoriezar_barcos(self):
        for x in range (1, 9):
            verificador = True
            while verificador:
                posicion_x = random.randrange(1, self.ancho + 1)
                posicion_y = random.randrange(1, self.alto + 1)
                verificador = self.celdas[posicion_x][posicion_y].verificar_celda()
                if not verificador :
                    self.celdas[posicion_x][posicion_y].posicionar_barco()
                    self.barcos.append(Barco())
    
    def sacar_barco(self, posicion_x, posicion_y):
        self.celdas[posicion_x][posicion_y].eliminar_barco()
    
    def verificar_barcos():
        if self.barcos == []:
            return False
        else: 
            return True
