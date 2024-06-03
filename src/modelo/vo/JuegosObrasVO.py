class JuegosObrasVO:
    def __init__(self, IdJuego=None, IdObra=None):
        self.IdJuego = IdJuego
        self.IdObra = IdObra

    def getIdJuego(self):
        return self.IdJuego

    def setIdJuego(self, IdJuego):
        self.IdJuego = IdJuego

    def getIdObra(self):
        return self.IdObra

    def setIdObra(self, IdObra):
        self.IdObra = IdObra
