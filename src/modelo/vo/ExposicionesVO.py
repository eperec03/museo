class ExposicionesVO:
    def __init__(self, IdExposicion, Titulo, Imagen, Descripcion, NumSala):
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

#cambiar a nuestros atributos
#No hace falta
    """def toString(self):
        return "UsuarioPremiumVO{" + "DNI=" + str(self._idUser) + ", NombreCompleto='" + self._nombre + "', Telefono='" + self._apellido1 + "', Email='" + self._apellido2 + "', Titular='" + self._email + "', NumTarjeta='" + self._email + "'"'}"

    def __str__(self):
        return self.toString()"""