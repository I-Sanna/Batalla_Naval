import random

class tablero:
    """ clase tablero almacena las celdas y barcos """

    def __inti__(self):
        self.ancho = None
        self.alto = None
        self.celdas =[[], []]
        self.establecer_tamaño()
        self.crear_tablero() 

    def establecer_tamaño(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def crear_tablero(self):
        for x in range (self.ancho):
            for y in range (self.alto):
                self.celdas[x][y] = Celda()

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
                self.celdas[x][y].eliminar_barco()
            
    def aleatoriezar_barcos(self):
        for x in range (8):
            verificador = True
            while verificador:
                posicion_x = random.randrange(0, self.ancho + 1)
                posicion_y = random.randrange(0, self.alto + 1)
                verificador = self.celdas[posicion_x][posicion_y].Verificar_celda()
                self.celdas[posicion_x][posicion_y].posicionar_barco()