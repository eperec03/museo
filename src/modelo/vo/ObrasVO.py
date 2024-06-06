class ObrasVO:
    def __init__(self, IdObra=None, Titulo=None, Descripcion=None, Fecha=None, Imagen=None, IdArtista=None, IdExposicion=None):
        self.IdObra = IdObra
        self.Titulo = Titulo
        self.Descripcion = Descripcion
        self.Fecha = Fecha
        self.Imagen = Imagen
        self.IdArtista = IdArtista
        self.IdExposicion = IdExposicion

    def getIdObra(self):
        return self.IdObra

    def setIdObra(self, IdObra):
        self.IdObra = IdObra

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

class ObrasExpuestaVO(ObrasVO):
    def __init__(self, IDObra, Titulo, Descripcion, Fecha, Imagen, IDArtista, IDExposicion, Disponible):
        super().__init__(IDObra, Titulo, Descripcion, Fecha, Imagen, IDArtista, IDExposicion)
        self._Disponible = Disponible

    def get_Disponible(self):
        return self._Disponible

    def set_Disponible(self, Disponible):
        self._Disponible = Disponible


class ObrasSubastadaVO(ObrasVO):
    def __init__(self, IDObra, Titulo, Descripcion, Fecha, Imagen, IDArtista, IDExposicion, PrecioSalida, PrecioVenta, MejorPostor):
        super().__init__(IDObra, Titulo, Descripcion, Fecha, Imagen, IDArtista, IDExposicion)
        self._PrecioSalida = PrecioSalida
        self._PrecioVenta = PrecioVenta
        self._MejorPostor = MejorPostor

    def get_PrecioSalida(self):
        return self._PrecioSalida

    def set_PrecioSalida(self, PrecioSalida):
        self._PrecioSalida = PrecioSalida

    def get_PrecioVenta(self):
        return self._PrecioVenta

    def set_PrecioVenta(self, PrecioVenta):
        self._PrecioVenta = PrecioVenta

    def get_MejorPostor(self):
        return self._MejorPostor

    def set_MejorPostor(self, MejorPostor):
        self._MejorPostor = MejorPostor