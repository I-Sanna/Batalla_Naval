from barco import Barco

class Celda:
    
    def __init__(self):
        self.barco = None

    def posicionar_barco(self):
        self.barco = Barco()
        return self.barco

    def atacar(self):
        if self.barco != None:
            self.barco.hundir()
            barco = self.eliminar_barco()
            return True, barco
        return False, None

    def eliminar_barco(self):
        if self.barco != None:
            barco = self.barco
            self.barco = None
            return barco
    
    def verificar_celda(self):
        if self.barco == None:
            return False
        else:
            return True