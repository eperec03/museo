class EditorVO:
    def __init__(self, DNI=None, NombreCompleto=None, Telefono=None, Email=None,
                 Titular=None, NumTarjeta=None, Cvv=None, Caducidad=None, Contraseña=None, FechaRegistro=None, Horario=None, TipoContrato=None, Estudios=None):
        self.DNI = DNI
        self.NombreCompleto = NombreCompleto
        self.Telefono = Telefono
        self.Email = Email
        self.Titular = Titular
        self.NumTarjeta = NumTarjeta
        self.Cvv = Cvv
        self.Caducidad = Caducidad
        self.Contraseña = Contraseña
        self.FechaRegistro = FechaRegistro
        self.Horario=Horario
        self.TipoContrato= TipoContrato
        self.Estudios = Estudios


    def getDNI(self):
        return self.DNI

    def setDNI(self, DNI):
        self.DNI = DNI

    def getNombreCompleto(self):
        return self.NombreCompleto

    def setNombreCompleto(self, NombreCompleto):
        self.NombreCompleto = NombreCompleto

    def getTelefono(self):
        return self.Telefono

    def setTelefono(self, Telefono):
        self.Telefono = Telefono

    def getEmail(self):
        return self.Email
    
    def getHorario(self):
        return self.Horario
    
    def getTipoContrato(self):
        return self.TipoContrato
    
    def getEstudios(self):
        return self.Estudios

    def setEmail(self, Email):
        self.Email = Email

    def getTitular(self):
        return self.Titular

    def setTitular(self, Titular):
        self.Titular = Titular

    def getNumTarjeta(self):
        return self.NumTarjeta

    def setNumTarjeta(self, NumTarjeta):
        self.NumTarjeta = NumTarjeta

    def getCvv(self):
        return self.Cvv

    def setCvv(self, Cvv):
        self.Cvv = Cvv

    def getCaducidad(self):
        return self.Caducidad

    def setCaducidad(self, Caducidad):
        self.Caducidad = Caducidad

    def getContraseña(self):
        return self.Contraseña

    def setContraseña(self, Contraseña):
        self.Contraseña = Contraseña

    def getFechaRegistro(self):
        return self.FechaRegistro

    def setFechaRegistro(self, FechaRegistro):
        self.FechaRegistro = FechaRegistro
    
    def getHorario(self):
        return self.Horario

    def setHorario(self, Horario):
        self.Horario = Horario

    def getTipoContrato(self):
        return self.TipoContrato

    def setTipoContrato(self,TipoContrato):
        self.TipoContrato =TipoContrato
    
    def getEstudios(self):
        return self.Estudios

    def setEstudios(self, Estudios):
        self.Estudios = Estudios

#cambiar a nuestros atributos
    # def toString(self):
    #     return "{" + "DNI=" + str(self._idUser) + ", nombre='" + self._nombre + "', apellido1='" + self._apellido1 + "', apellido2='" + self._apellido2 + "', email='" + self._email + "'}"

    # def __str__(self):
    #     return self.toString()