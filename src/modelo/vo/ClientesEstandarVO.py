class ClienteEstandarVO:
    def __init__(self, NumEntrada, PrecioEntrada):
        self.NumEntrada = NumEntrada
        self.PrecioEntrada = PrecioEntrada

    def getNumEntrada(self):
        return self.NumEntrada

    def setNumEntrada(self, NumEntrada):
        self.NumEntrada = NumEntrada

    def getPrecioEntrada(self):
        return self.PrecioEntrada

    def setPrecioEntrada(self, PrecioEntrada):
        self.PrecioEntrada = PrecioEntrada

    