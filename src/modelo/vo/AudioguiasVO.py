class AudioguiasVO:
    def __init__(self, IdAudio=None, IdObra=None, Audio=None, Duracion=None):
        self.IdAudio = IdAudio
        self.IdObra = IdObra
        self.Audio = Audio
        self.Duracion = Duracion

    def getIdAudio(self):
        return self.IdAudio

    def setIdAudio(self, IdAudio):
        self.IdAudio = IdAudio

    def getIdObra(self):
        return self.IdObra

    def setIdObra(self, IdObra):
        self.IdObra = IdObra

    def getAudio(self):
        return self.Audio

    def setAudio(self, Audio):
        self.Audio = Audio

    def getDuracion(self):
        return self.Duracion

    def setDuracion(self, Duracion):
        self.Duracion = Duracion
