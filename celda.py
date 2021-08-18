

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

    def eliminar_barco(self):
        if self.barco != None:
            self.barco = None
    
    def verificar_celda(self):
        if self.barco == None:
            return False
        else:
            return True