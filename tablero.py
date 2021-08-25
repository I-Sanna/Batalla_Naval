import random
from celda import Celda

class Tablero:
    """ clase tablero almacena las celdas y barcos """



    def __init__(self, ancho, alto):
        self.ancho = None
        self.alto = None
        self.barcos = []
        self.celdas =[]
        self.establecer_tamaño(ancho, alto)
        self.crear_tablero() 

    def establecer_tamaño(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def crear_tablero(self):
        for columna in range (0, self.ancho):
            lista = []
            for fila in range (0, self.alto):
                lista.append(Celda())
            self.celdas.append(lista)          

    def colocar_barco(self, posicion_x, posicion_y):
        barco = self.celdas[posicion_y - 1][posicion_x - 1].posicionar_barco()
        self.barcos.append(barco)

    def lanzar(self, posicion_x, posicion_y):
        resultado, barco = self.celdas[posicion_y - 1][posicion_x - 1].atacar()
        if resultado:
            print ("Hundido!!!")
            self.barcos.remove(barco)
        else:
            print ("Agua")
    
    def limpiar_tablero(self):
        for x in range (1, self.ancho + 1):
            for y in range (self.alto + 1):
                print(self.sacar_barco(x, y))
            
    def aleatorizar_barcos(self):
        for x in range (8):
            verificador = True
            while verificador:
                posicion_x = random.randrange(0, self.alto)
                posicion_y = random.randrange(0, self.ancho)
                verificador = self.celdas[posicion_y][posicion_x].verificar_celda()
                if not verificador :
                    self.colocar_barco(posicion_x + 1, posicion_y + 1)
    
    def sacar_barco(self, posicion_x, posicion_y):
        verificador = self.celdas[posicion_y - 1][posicion_x - 1].verificar_celda()
        if verificador:
            barco = self.celdas[posicion_y - 1][posicion_x - 1].eliminar_barco()
            self.barcos.remove(barco)
            return "barco eliminado exitosamente"
        else:
            return "no hay un barco en la celda"
    
    def verificar_barcos(self):
        if self.barcos == []:
            return "no hay barcos"           
        else: 
            return "hay barcos"
