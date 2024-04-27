import mysql.connector 
import datetime
# config = {'user': 'bduser', 'passwd' : 'bdpass', 'host':
# 'localhost', 'database': 'DataCars'}
# cnx = mysql.connector.connect(**config)
# cursor = cnx.cursor()
# # query = "INSERT INTO Pets(id, name, weight) VALUES ('GA111','Willow', 10.2)"
# # cursor.execute(query)
# cnx.commit() 
class UsuarioEspecial:
    def __init__(self, DNI, NombreCompleto, Telefono, Email,TarjetaBancaria, Contraseña, FechaRegistro):
        self.DNI = DNI
        self.NombreCompleto = NombreCompleto
        self.Telefono = Telefono
        self.Email = Email
        self.TarjetaBancaria = TarjetaBancaria
        self.Contraseña = Contraseña
        self.FechaRegistro = FechaRegistro

    def connect_to_db(self):
        config = {'user': self.user, 'passwd' : self.passwd, 'host':self.host, 'database': self.database}
        return mysql.connector.connect(**config)
    
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

    def getTarjetaBancaria(self):
        return self.TarjetaBancaria

    def setTarjetaBancaria(self, TarjetaBancaria):
        self.TarjetaBancaria = TarjetaBancaria

    def getContraseña(self):
        return self.Contraseña

    def setContraseña(self, Contraseña):
        self.Contraseña = Contraseña

    def getFechaRegistro(self):
        return self.FechaRegistro

    def setFechaRegistro(self, FechaRegistro):
        self.FechaRegistro = FechaRegistro