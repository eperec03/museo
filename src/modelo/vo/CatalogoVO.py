class CatalogoVO:
    def __init__(self, IdCatalogo=None, Titulo=None,Portada=None):
        self.IdCatalogo = IdCatalogo
        self.Titulo=Titulo
        self.Portada = Portada

    def getIdCatalogo(self):
        return self.IdCatalogo

    def setIdCatalogo(self, IdCatalogo):
        self.IdCatalogo = IdCatalogo
    
    def getTitulo(self):
        return self.Titulo

    def setTitulo(self, Titulo):
        self.Titulo = Titulo

    def getPortada(self):
        return self.Portada

    def setPortada(self, Portada):
        self.Portada = Portada
