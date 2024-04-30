from jaydebeapi import Error
from typing import List
from vo.UserVO import UserVO 
from conexion.conexion2JDBC import Conexion
from dao.UserInterface import UserInterface
# Creamos la clase UsuarioDAO que manejará las operaciones de acceso a datos para los usuarios

class UserDao(UserInterface,Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT DNI, NombreCompleto, Telefono, Email, Titular, Cvv, Caducidad, Contraseña, FechaRegistro FROM Usuarios"
    SQL_INSERT = "INSERT INTO Usuarios(DNI, NombreCompleto, Telefono, Email, Titular, Cvv, Caducidad, Contraseña, FechaRegistro) VALUES (?, ?, ?, ?, ?, ?, ? , ? , ?, ?)"


    def getUsuarios(self) -> List[UserVO]:
        conexion=self.getConnection()
        conn = None
        cursor = None
        usuarios = []

        try:
            if conexion:
                conn= conexion
            else:
                print("La base de datos no esta disponible")

            #Crea un objeto para poder ejecutar consultas SQL sobre la conexion abierta
            cursor= conn.cursor()
            #Ejecuta de sonsulta SQL
            cursor.execute(self.SQL_SELECT)
            #Obtiene todas las filas resultantes de la consulta
            rows = cursor.fetchall()

            #Itera sobre todas las filas
            for row in rows:
                DNI, NombreCompleto, Telefono, Email, Titular, Cvv, Caducidad, Contraseña, FechaRegistro = row
                #Crea un objeto UserVO para cada fila DNI, NombreCompleto...
                usuario = UserVO()
                usuario.setNombreCompleto(NombreCompleto)
                usuario.setTitular(Titular)
                usuario.setCvv(Cvv)
                usuario.setCaducidad(Caducidad)
                usuario.setEmail(Email)
                usuario.setFechaRegistro(FechaRegistro)
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
    def insertUsuario (self, usuario: UserVO) -> int:
        conn = None
        cursor = None
        return int



