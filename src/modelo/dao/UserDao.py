from jaydebeapi import Error
from typing import List
from src.vo.userVO import UserVO 
from src.conexion.conexion2JDBC import Conexion
from src.dao.UserInterface import UserInterface
# Creamos la clase UsuarioDAO que manejará las operaciones de acceso a datos para los usuarios

class UserDao(UserInterface):
    def __init__(self, conexion=None):
        self.conexion=conexion

    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT DNI, NombreCompleto, Telefono, Email, Titular, Cvv, Caducidad, Contraseña, FechaRegistro FROM Usuarios"
    SQL_INSERT = "INSERT INTO Usuarios(DNI, NombreCompleto, Telefono, Email, Titular, Cvv, Caducidad, Contraseña, FechaRegistro)"


    def getUsuarios(self) -> List[UserVO]:
        conn = None
        cursor = None
        usuarios = []

        try:
            if self.conexion:
                conn= self.conexion

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

        return usuarios

    #se hace el proximo dia
    def insertUsuario (self, usuario: UserVO) -> int:
        conn = None
        cursor = None
        return int



