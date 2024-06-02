class ObrasSubastadasVO:
    def __init__(self, IdObraSubastada=None, PrecioSalida=None, PrecioVenta=None, MejorPostor=None, Titulo=None, Descripcion=None, Fecha=None, Imagen=None, IdArtista=None, IdExposicion=None):
        self.IdObraSubastada = IdObraSubastada
        self.PrecioSalida = PrecioSalida
        self.PrecioVenta = PrecioVenta
        self.MejorPostor = MejorPostor
        self.Titulo = Titulo
        self.Descripcion = Descripcion
        self.Fecha = Fecha
        self.Imagen = Imagen
        self.IdArtista = IdArtista
        self.IdExposicion = IdExposicion

    def getIdObraSubastada(self):
        return self.IdObraSubastada

    def setIdObraSubastada(self, IdObraSubastada):
        self.IdObraSubastada = IdObraSubastada

    def getPrecioSalida(self):
        return self.PrecioSalida

    def setPrecioSalida(self, PrecioSalida):
        self.PrecioSalida = PrecioSalida

    def getPrecioVenta(self):
        return self.PrecioVenta

    def setPrecioVenta(self, PrecioVenta):
        self.PrecioVenta = PrecioVenta

    def getMejorPostor(self):
        return self.MejorPostor

    def setMejorPostor(self, MejorPostor):
        self.MejorPostor = MejorPostor

    def getTitulo(self):
        return self.Titulo

    def setTitulo(self, Titulo):
        self.Titulo = Titulo

    def getDescripcion(self):
        return self.Descripcion

    def setDescripcion(self, Descripcion):
        self.Descripcion = Descripcion

    def getFecha(self):
        return self.Fecha

    def setFecha(self, Fecha):
        self.Fecha = Fecha

    def getImagen(self):
        return self.Imagen

    def setImagen(self, Imagen):
        self.Imagen = Imagen

    def getIdArtista(self):
        return self.IdArtista

    def setIdArtista(self, IdArtista):
        self.IdArtista = IdArtista

    def getIdExposicion(self):
        return self.IdExposicion

    def setIdExposicion(self, IdExposicion):
        self.IdExposicion = IdExposicion
