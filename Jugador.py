from tablero import Tablero

class Jugador: 
    
    def __init__(self, ancho, alto):
        self.nombre = None
        self.ancho_tablero = ancho
        self.alto_tablero = alto
        self.tablero = Tablero(ancho, alto)
    
    def barcos_randoms(self):
        self.tablero.aleatorizar_barcos()

    def colocar_barcos(self):
        for x in range(8):
            verificador = False
            while not verificador:
                posicion_x = input("Ingrese la columna(1, 2, 3...): ")
                posicion_y = input("Ingrese la fila(A, B, C...): ")
                try:
                    posicion_y = letras_a_numeros[posicion_y.upper]
                except:
                    print ("La fila ingresada no existe.")
                    continue
                if posicion_x.isnumeric() and posicion_x =< self.ancho_tablero and posicion_x != 0 and posicion_y =< self.alto_tablero:
                    verificador = True
                else:
                    print("La columna ingresada no existe")
            self.tablero.colocar_barco(int(posicion_x) - 1, posicion_y - 1)
        
    def atacar(self):
        verificador = False
            while not verificador:
                posicion_x = input("Ingrese la columna(1, 2, 3...): ")
                posicion_y = input("Ingrese la fila(A, B, C...): ")
                try:
                    posicion_y = letras_a_numeros[posicion_y.upper]
                except:
                    print ("La fila ingresada no existe.")
                    continue
                if posicion_x.isnumeric() and posicion_x =< self.ancho_tablero and posicion_x != 0 and posicion_y =< self.alto_tablero:
                    verificador = True
                else:
                    print("La columna ingresada no existe")
            self.tablero.lanzar(int(posicion_x) - 1, posicion_y - 1)
            hay_barcos = self.tablero.verificar_barcos()
            return hay_barcos

    
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