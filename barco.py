class Barco:
    """ Una calse barco con el obejetivo de ser un blanco de tiro """

    def __init__(self):
        """ constructor de la clase """
        self.hundido = False

    def hundir(self):
        """ El Barco cambia al esto undido """
        self.hundido = True