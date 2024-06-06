class SubastasVO:
    def __init__(self, IdSubastas=None, Titulo=None, Descripcion=None,Fecha=None):
        self.IdSubastas = IdSubastas
        self.Titulo = Titulo
        self.Descripcion=Descripcion
        self.Fecha=Fecha

    def getIdSubastas(self):
        return self.IdSubastas

    def setIdSubastas(self, IdSubastas):
        self.IdSubastas = IdSubastas

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
        self.Fecha  = Fecha


    

