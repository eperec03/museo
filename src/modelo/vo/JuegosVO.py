class ExposicionesVO:
    def __init__(self, IdJuego=None, Nombre, Dificultad, Descripcion):
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

#cambiar a nuestros atributos
#No hace falta
    """def toString(self):
        return "UsuarioPremiumVO{" + "DNI=" + str(self._idUser) + ", NombreCompleto='" + self._nombre + "', Telefono='" + self._apellido1 + "', Email='" + self._apellido2 + "', Titular='" + self._email + "', NumTarjeta='" + self._email + "'"'}"

    def __str__(self):
        return self.toString()"""