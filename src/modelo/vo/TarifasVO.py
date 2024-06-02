class TarifasVO:
    def __init__(self, TipoTarifa=None, Precio=None, Duracion=None):
        self.TipoTarifa = TipoTarifa
        self.Precio = Precio
        self.Duracion = Duracion

    def getTipoTarifa(self):
        return self.TipoTarifa

    def setTipoTarifa(self, TipoTarifa):
        self.TipoTarifa = TipoTarifa

    def getPrecio(self):
        return self.Precio

    def setPrecio(self, Precio):
        self.Precio = Precio

    def getDuracion(self):
        return self.Duracion

    def setDuracion(self, Duracion):
        self.Duracion = Duracion
