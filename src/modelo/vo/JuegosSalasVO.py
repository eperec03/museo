class JuegosSalasVO:
    def __init__(self, IdJuego=None, IdSala=None):
        self.IdJuego = IdJuego
        self.IdSala = IdSala

    def getIdJuego(self):
        return self.IdJuego

    def setIdJuego(self, IdJuego):
        self.IdJuego = IdJuego

    def getIdSala(self):
        return self.IdSala

    def setIdSala(self, IdSala):
        self.IdSala = IdSala
