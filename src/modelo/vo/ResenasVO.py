class ResenasVO:
    def __init__(self, NumReseña=None, IdObra=None, Texto=None, NumEstrellas=None, Visible=None, Fecha=None):
        self.NumReseña = NumReseña
        self.IdObra = IdObra
        self.Texto = Texto
        self.NumEstrellas = NumEstrellas
        self.Visible = Visible
        self.Fecha = Fecha

    def getNumReseña(self):
        return self.NumReseña

    def setNumReseña(self, NumReseña):
        self.NumReseña = NumReseña

    def getIdObra(self):
        return self.IdObra

    def setIdObra(self, IdObra):
        self.IdObra = IdObra

    def getTexto(self):
        return self.Texto

    def setTexto(self, Texto):
        self.Texto = Texto

    def getNumEstrellas(self):
        return self.NumEstrellas

    def setNumEstrellas(self, NumEstrellas):
        self.NumEstrellas = NumEstrellas

    def getVisible(self):
        return self.Visible

    def setVisible(self, Visible):
        self.Visible = Visible

    def getFecha(self):
        return self.Fecha

    def setFecha(self, Fecha):
        self.Fecha = Fecha
