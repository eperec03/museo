class ArtistasVO:
    def __init__(self, IdArtista=None,NombreArtista=None, FechaNacimiento=None, FechaMuerte=None, Descripcion=None, Corriente=None):
        self.IdArtista=IdArtista
        self.NombreArtista = NombreArtista
        self.FechaNacimiento = FechaNacimiento
        self.FechaMuerte = FechaMuerte
        self.Descripcion = Descripcion
        self.Corriente = Corriente

    def getIdArtista(self):
        return self.IdArtista

    def setIdArtista(self, IdArtista):
        self.IdArtista = IdArtista
    
    def getNombreArtista(self):
        return self.NombreArtista

    def setNombreArtista(self, NombreArtista):
        self.NombreArtista = NombreArtista

    def getFechaNacimiento(self):
        return self.FechaNacimiento

    def setFechaNacimiento(self, FechaNacimiento):
        self.FechaNacimiento = FechaNacimiento

    def getFechaMuerte(self):
        return self.FechaMuerte

    def setFechaMuerte(self, FechaMuerte):
        self.FechaMuerte = FechaMuerte

    def getDescripcion(self):
        return self.Descripcion

    def setDescripcion(self, Descripcion):
        self.Descripcion = Descripcion

    def getCorriente(self):
        return self.Corriente

    def setCorriente(self, Corriente):
        self.Corriente = Corriente
