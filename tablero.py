import random
from celda import Celda
from barco import Barco

class Tablero:
    """ clase tablero almacena las celdas y barcos """



    def __init__(self):
        self.ancho = None
        self.alto = None
        self.barcos = []
        self.celdas =[]
        self.establecer_tamaño(int(input("ancho  ")), int(input("alto  ")))
        self.crear_tablero() 

    def establecer_tamaño(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def crear_tablero(self):
        for columna in range (1, self.ancho + 1):
            lista = []
            for fila in range (1, self.alto + 1):
                lista.append(Celda())
            self.celdas.append(lista)          

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
