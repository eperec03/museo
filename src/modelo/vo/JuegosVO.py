class JuegosVO:
    def __init__(self, IdJuego=None, Nombre=None, Dificultad=None, Descripcion=None):
        self.IdJuego = IdJuego
        self.Nombre = Nombre
        self.Dificultad = Dificultad
        self.Descripcion = Descripcion

    def getIdJuego(self):
        return self.IdJuego

    def setIdJuego(self, IdJuego):
        self.IdJuego = IdJuego

    def getNombre(self):
        return self.Nombre

    def setNombre(self, Nombre):
        self.Nombre = Nombre

    def getDificultad(self):
        return self.Dificultad

    def setDificultad(self, Dificultad):
        self.Dificultad = Dificultad

    def getDescripcion(self):
        return self.Descripcion

    def setDescripcion(self, Descripcion):
        self.Descripcion = Descripcion

