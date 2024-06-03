class EdicionJuegosVO:
    def __init__(self, IdServicio=None, TipoGestion=None, SSN=None):
        self.IdServicio = IdServicio
        self.TipoGestion = TipoGestion
        self.SSN=SSN

    def getIdServicio(self):
        return self.IdServicio

    def setIdServicio(self, IdServicio):
        self.IdServicio = IdServicio

    def getTipoGestion(self):
        return self.TipoGestion

    def setTipoGestion(self, TipoGestion):
        self.TipoGestion = TipoGestion

    def getSSN(self):
        return self.SSN

    def setSSN(self, SSN):
        self.SSN = SSN


    

