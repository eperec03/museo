class CLientePremiumVO:
    def __init__(self, DNI=None, NombreCompleto=None, Telefono=None, Email=None,
                 Titular=None, NumTarjeta=None, Cvv=None, Caducidad=None, Contraseña=None, FechaRegistro=None,
                  ObrasAdquiridas=None, Dinerogastado=None, TipoTarifa=None, Penalizacion=None):
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
        self.ObrasAdquiridas = ObrasAdquiridas
        self.Dinerogastado = Dinerogastado
        self.TipoTarifa = TipoTarifa
        self.Penalizacion = Penalizacion

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

    ObrasAdquiridas, Dinerogastado, TipoTarifa, Penalizacion

    def getObrasAdquiridas(self):
        return self.ObrasAdquiridas

    def setObrasAdquiridas(self, ObrasAdquiridas):
        self.ObrasAdquiridas = ObrasAdquiridas

    def getDinerogastado(self):
        return self.Dinerogastado

    def setDinerogastado(self, Dinerogastado):
        self.Dinerogastado = Dinerogastado

    def getTipoTarifa(self):
        return self.TipoTarifa

    def setTipoTarifa(self, TipoTarifa):
        self.TipoTarifa = TipoTarifa

    def getPenalizacion(self):
        return self.Penalizacion

    def setPenalizacion(self, Penalizacion):
        self.Penalizacion = Penalizacion

#cambiar a nuestros atributos
#No hace falta
    """def toString(self):
        return "UsuarioPremiumVO{" + "DNI=" + str(self._idUser) + ", NombreCompleto='" + self._nombre + "', Telefono='" + self._apellido1 + "', Email='" + self._apellido2 + "', Titular='" + self._email + "', NumTarjeta='" + self._email + "'"'}"

    def __str__(self):
        return self.toString()"""