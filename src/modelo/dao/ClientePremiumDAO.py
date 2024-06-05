from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')

from vo.ClientePremiumVO import ClientePremiumVO 
from conexion.conexion2JDBC import Conexion
from modelo.dao.ClientePremiumInterface import ClientePInterface
# Creamos la clase UsuarioDAO que manejará las operaciones de acceso a datos para los usuarios

class ClientePremiumDAO(ClientePInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT DNI, UsuNombreCompleto, UsuTfno, UsuEmail, UsuTitularMP, UsuCvvMP, UsuNumTarjMP, UsuCadMP, UsuContrasenna, FROM Clientespremium"
    SQL_INSERT = "INSERT INTO Clientespremium(DNI, UsuNombreCompleto, UsuTfno, UsuEmail, UsuTitularMP, UsuNumTarjMP, UsuCvvMP, UsuCadMP, UsuContrasenna) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
    SQL_DELETE = "DELETE FROM Usuarios WHERE DNI = ?"
    SQL_UPDATE = "UPDATE Usuarios SET UsuNombreCompleto = ?, UsuTfno = ?, UsuEmail = ?, UsuTitularMP = ?, UsuCvvMP = ?, UsuNumTarjMP = ?, UsuCadMP = ?, UsuContrasenna = ? WHERE DNI = ?"
    SQL_FILTER = "SELECT * FROM Usuarios WHERE DNI = ?"


    def getUsuarios(self) -> List[ClientePremiumVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        usuarios = []
        try:
            if conexion:
                conn = conexion
            else:
                print("La base de datos no esta disponible")
            #Crea un objeto para poder ejecutar consultas SQL sobre la conexion abierta
            cursor = conn.cursor()
            #Ejecuta de consulta SQL
            cursor.execute(self.SQL_SELECT) #Obtiene todas las filas resultantes de la consulta
            rows = cursor.fetchall()
            #Itera sobre todas las filas
            for row in rows:
                DNI, UsuNombreCompleto, UsuTfno, UsuEmail, UsuTitularMP, UsuNumTarjMP, UsuCvvMP, UsuCadMP, UsuContrasenna = row
                #Crea un objeto ClientePremiumVO para cada fila DNI, NombreCompleto...
                usuario = ClientePremiumVO()
                usuario.setDNI(DNI)
                usuario.setNombreCompleto(UsuNombreCompleto)
                usuario.setTelefono(UsuTfno)
                usuario.setEmail(UsuEmail)
                usuario.setTitular(UsuTitularMP)
                usuario.setNumTarjeta(UsuNumTarjMP)
                usuario.setCvv(UsuCvvMP)
                usuario.setCaducidad(UsuCadMP)
                usuario.setContraseña(UsuContrasenna)
                usuarios.append(usuario)

        except Error as e:
            print("Error al seleccionar usuarios:", e)

        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return usuarios
    
    def getFiltroUsuarios(self,dni) -> List[ClientePremiumVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        usuarios = []

        try:
            if conexion:
                conn = conexion
            else:
                print("La base de datos no esta disponible")
            #Crea un objeto para poder ejecutar consultas SQL sobre la conexion abierta
            cursor = conn.cursor()
            #Ejecuta de consulta SQL
            cursor.execute(self.SQL_FILTER, (dni,)) #Obtiene todas las filas resultantes de la consulta
            #Obtiene todas las filas resultantes de la consulta
            rows = cursor.fetchall()
            print(rows)

            #Crea un objeto ClientePremiumVO para cada fila DNI, NombreCompleto...
            for row in rows:
                DNI, UsuNombreCompleto, UsuTfno, UsuEmail, UsuTitularMP, UsuNumTarjMP, UsuCvvMP, UsuCadMP, UsuContrasenna, UsuFecha = row
                #Crea un objeto ClientePremiumVO para cada fila DNI, NombreCompleto...
                usuario = ClientePremiumVO(DNI=DNI, NombreCompleto=UsuNombreCompleto, Telefono=UsuTfno,Email=UsuEmail, Titular= UsuTitularMP, NumTarjeta= UsuNumTarjMP,Cvv= UsuCvvMP, Caducidad= UsuCadMP, Contraseña=UsuContrasenna, FechaRegistro=UsuFecha)
                usuarios.append(usuario)

        except Error as e:
            print("Error al seleccionar usuarios:", e)

        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return usuarios
    #se hace el proximo dia
    def insertUsuario (self, usuario: ClientePremiumVO) -> int:
        conexion = self.getConnection()
        conn = None
        cursor = None
        rows = 0

        try:
            if conexion:
                conn = conexion
           
            else:
                print("La base de datos no esta disponible")

            cursor = conn.cursor()
            cursor.execute(self.SQL_INSERT, (usuario.getDNI(),usuario.getNombreCompleto(),usuario.getTelefono(),usuario.getEmail(),usuario.getTitular(),usuario.getNumTarjeta(),usuario.getCvv(),usuario.getCaducidad(),usuario.getContraseña()))
            # conn.commit()
            #Asegurarse de que esos cambios se hagan permanentes: conn.commit(). Si conn.autocommit = True no es necesario llamar explícitamente a conn.commit() después de cada inserción, ya que la base de datos confirma automáticamente cada instrucción.
           
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al insertar usuario:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def eliminateUsuario (self, usuario:ClientePremiumVO) -> int:
        conexion = self.getConnection()
        conn = None
        cursor = None
        rows = 0

        try:
            if conexion:
                conn = conexion
           
            else:
                print("La base de datos no esta disponible")

            cursor = conn.cursor()
            cursor.execute(self.SQL_DELETE, (usuario.getDNI(),))
            # conn.commit()
            #Asegurarse de que esos cambios se hagan permanentes: conn.commit(). Si conn.autocommit = True no es necesario llamar explícitamente a conn.commit() después de cada inserción, ya que la base de datos confirma automáticamente cada instrucción.
           
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al eliminar usuario:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def updateUsuario  (self, usuario:ClientePremiumVO) -> int:
        conexion = self.getConnection()
        conn = None
        cursor = None
        rows = 0

        try:
            if conexion:
                conn = conexion
           
            else:
                print("La base de datos no esta disponible")

            cursor = conn.cursor()
            cursor.execute(self.SQL_UPDATE, (usuario.getNombreCompleto(),usuario.getTelefono(),usuario.getEmail(),usuario.getTitular(),usuario.getNumTarjeta(),usuario.getCvv(),usuario.getCaducidad(),usuario.getContraseña(), usuario.getDNI()))
            # conn.commit()
            #Asegurarse de que esos cambios se hagan permanentes: conn.commit(). Si conn.autocommit = True no es necesario llamar explícitamente a conn.commit() después de cada inserción, ya que la base de datos confirma automáticamente cada instrucción.
           
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar usuario:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows














