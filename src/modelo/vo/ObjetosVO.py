class ObjetosVO:
    def __init__(self, IdObjeto, Imagen, Precio, Tipo, 
    Inspiracion, Existencias, Agotado, IdCatalogo):
        self.IdObjeto = IdObjeto
        self.Imagen = Imagen
        self.Precio = Precio
        self.Tipo = Tipo
        self.Inspiracion = Inspiracion
        self.Existencias = Existencias
        self.Agotado = Agotado
        self.IdCatalogo = IdCatalogo

    def getIdObjeto(self):
        return self.IdObjeto

    def setIdObjeto(self, IdObjeto):
        self.IdObjeto = IdObjeto

    def getImagen(self):
        return self.Imagen

    def setImagen(self, Imagen):
        self.Imagen = Imagen

    def getPrecio(self):
        return self.Precio

    def setPrecio(self, Precio):
        self.Precio = Precio

    def getTipo(self):
        return self.Tipo

    def setTipo(self, Tipo):
        self.Tipo = Tipo

    def getInspiracion(self):
        return self.Inspiracion

    def setInspiracion(self, Inspiracion):
        self.Inspiracion = Inspiracion

    def getExistencias(self):
        return self.Existencias

    def setExistencias(self, Existencias):
        self.Existencias = Existencias

    def getAgotado(self):
        return self.Agotado

    def setAgotado(self, Agotado):
        self.Agotado = Agotado

    def getIdCatalogo(self):
        return self.IdCatalogo

    def setIdCatalogo(self, IdCatalogo):
        self.IdCatalogo = IdCatalogo

#cambiar a nuestros atributos
#No hace falta
    """def toString(self):
        return "UsuarioPremiumVO{" + "DNI=" + str(self._idUser) + ", NombreCompleto='" + self._nombre + "', Telefono='" + self._apellido1 + "', Email='" + self._apellido2 + "', Titular='" + self._email + "', NumTarjeta='" + self._email + "'"'}"

    def __str__(self):
        return self.toString()"""