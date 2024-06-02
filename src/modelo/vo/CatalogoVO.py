class CatalogoVO:
    def __init__(self, IdCatalogo=None, Portada=None):
        self.IdCatalogo = IdCatalogo
        self.Portada = Portada

    def getIdCatalogo(self):
        return self.IdCatalogo

    def setIdCatalogo(self, IdCatalogo):
        self.IdCatalogo = IdCatalogo

    def getPortada(self):
        return self.Portada

    def setPortada(self, Portada):
        self.Portada = Portada
