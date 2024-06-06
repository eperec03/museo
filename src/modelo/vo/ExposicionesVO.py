class ExposicionesVO:
    def __init__(self, IdExposicion=None, Titulo=None, Imagen=None, Descripcion=None, NumSala=None):
        self.IdExposicion = IdExposicion
        self.Titulo = Titulo
        self.Imagen = Imagen
        self.Descripcion = Descripcion
        self.NumSala = NumSala

    def getIdExposicion(self):
        return self.IdExposicion

    def setIdExposicion(self, IdExposicion):
        self.IdExposicion = IdExposicion

    def getTitulo(self):
        return self.Titulo

    def setTitulo(self, Titulo):
        self.Titulo = Titulo

    def getImagen(self):
        return self.Imagen

    def setImagen(self, Imagen):
        self.Imagen = Imagen

    def getDescripcion(self):
        return self.Descripcion

    def setDescripcion(self, Descripcion):
        self.Descripcion = Descripcion

    def getNumSala(self):
        return self.NumSala

    def setNumSala(self, NumSala):
        self.NumSala = NumSala

