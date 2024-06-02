class SalasVO:
    def __init__(self, NumeroSala=None, Capacidad=None, Tematica=None, IdMapa=None):
        self.NumeroSala = NumeroSala
        self.Capacidad = Capacidad
        self.Tematica = Tematica
        self.IdMapa = IdMapa

    def getNumeroSala(self):
        return self.NumeroSala

    def setNumeroSala(self, NumeroSala):
        self.NumeroSala = NumeroSala

    def getCapacidad(self):
        return self.Capacidad

    def setCapacidad(self, Capacidad):
        self.Capacidad = Capacidad

    def getTematica(self):
        return self.Tematica

    def setTematica(self, Tematica):
        self.Tematica = Tematica

    def getIdMapa(self):
        return self.IdMapa

    def setIdMapa(self, IdMapa):
        self.IdMapa = IdMapa

#cambiar a nuestros atributos
#No hace falta
    """def toString(self):
        return "UsuarioPremiumVO{" + "DNI=" + str(self._idUser) + ", NombreCompleto='" + self._nombre + "', Telefono='" + self._apellido1 + "', Email='" + self._apellido2 + "', Titular='" + self._email + "', NumTarjeta='" + self._email + "'"'}"

    def __str__(self):
        return self.toString()"""