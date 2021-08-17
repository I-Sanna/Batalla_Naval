class tablero:
    """ clase tablero almacena las celdas y barcos """

    def __inti__(self):
        self.ancho = None
        self.alto = None
        self.celdas =[[], []]
        self.establecer_tamaño(int, int)
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

class Celda:
    
    def __init__(self):
        self.barco = None

    def posicionar_barco(self):
        self.barco = Barco()

    def atacar(self):
        if self.barco != None:
            self.barco.hundir()
            self.barco = None
            return True
        return False

class Barco:
    """"""

    def __init__(self):
        self.hundido = False

    def hundir(self):
        self.hundido = True