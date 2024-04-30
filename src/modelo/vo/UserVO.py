class Usuario:
    def __init__(self, DNI, NombreCompleto, Telefono, Email,
                 Titular, Cvv, Caducidad, Contraseña, FechaRegistro):
        self.DNI = DNI
        self.NombreCompleto = NombreCompleto
        self.Telefono = Telefono
        self.Email = Email
        self.Titular = Titular
        self.Cvv = Cvv
        self.Caducidad = Caducidad
        self.Contraseña = Contraseña
        self.FechaRegistro = FechaRegistro

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
