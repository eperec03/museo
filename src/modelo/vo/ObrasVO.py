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
    def __init__(self, Disponible=None, IDObraexpuesta=None):
        self.IDObraexpuesta = IDObraexpuesta
        self.Disponible = Disponible

    def get_IDObraexpuesta(self):
        return self.IDObraexpuesta

    def set_IDObraexpuesta(self, IDObraexpuesta):
        self.IDObraexpuesta = IDObraexpuesta

    def get_Disponible(self):
        return self.Disponible

    def set_Disponible(self, Disponible):
        self.Disponible = Disponible


class ObrasSubastadasVO(ObrasVO):
    def __init__(self ,PrecioSalida=None, PrecioVenta=None, MejorPostor=None, IDObrasubastada=None):
        self.IDObrasubastada = IDObrasubastada
        self.PrecioSalida = PrecioSalida
        self.PrecioVenta = PrecioVenta
        self.MejorPostor = MejorPostor

    def get_IDObrasubastada(self):
        return self.IDObrasubastada

    def set_IDObrasubastada(self, IDObrasubastada):
        self.IDObrasubastada = IDObrasubastada

    def get_PrecioSalida(self):
        return self.PrecioSalida

    def set_PrecioSalida(self, PrecioSalida):
        self.PrecioSalida = PrecioSalida

    def get_PrecioVenta(self):
        return self.PrecioVenta

    def set_PrecioVenta(self, PrecioVenta):
        self.PrecioVenta = PrecioVenta

    def get_MejorPostor(self):
        return self.MejorPostor

    def set_MejorPostor(self, MejorPostor):
        self.MejorPostor = MejorPostor