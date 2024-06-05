from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')

from vo.ClientesEstandarVO import  *
from conexion.conexion2JDBC import Conexion
from modelo.dao.ClienteEstandarInterface import *

class ClienteEstandarDAO(ClienteEInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT NumEntrada FROM clienteestandar"
    SQL_INSERT = "INSERT INTO clienteestandar(NumEntrada) VALUES (?)"


    def getEntradas(self) -> List[ClienteEstandarVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        entradas = []
        try:
            if conexion:
                conn = conexion
            else:
                print("La base de datos no esta disponible")

            cursor = conn.cursor()

            cursor.execute(self.SQL_SELECT) 
            rows = cursor.fetchall()
            for row in rows:
                NumEntrada = row
                entrada = ClienteEstandarVO()
                entrada.setNumEntrada(NumEntrada)
                entradas.append(entrada)

        except Error as e:
            print("Error al seleccionar clientes estándar:", e)

        finally:
            if cursor:
                cursor.close()
        conexion = self.closeConnection(conn)
        return entradas

    def insertEntrada (self, entrada: ClienteEstandarVO) -> int:
        if not isinstance(entrada, ClienteEstandarVO):
                raise TypeError("entrada must be an instance of ClienteEstandarVO")
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
            cursor.execute(self.SQL_INSERT, (entrada.getNumEntrada(),))
            rows = cursor.rowcount

        except Error as e:
            print("Error al insertar usuario:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    # def eliminateUsuario (self, usuario:ClientePremiumVO) -> int:
    #     conexion = self.getConnection()
    #     conn = None
    #     cursor = None
    #     rows = 0

    #     try:
    #         if conexion:
    #             conn = conexion
           
    #         else:
    #             print("La base de datos no esta disponible")

    #         cursor = conn.cursor()
    #         cursor.execute(self.SQL_DELETE, (usuario.getDNI(),))
            # conn.commit()
            #Asegurarse de que esos cambios se hagan permanentes: conn.commit(). Si conn.autocommit = True no es necesario llamar explícitamente a conn.commit() después de cada inserción, ya que la base de datos confirma automáticamente cada instrucción.
           
            #Devuelve 1 si la inserción fue exitosa
        #     rows = cursor.rowcount
        # except Error as e:
        #     print("Error al eliminar usuario:", e)


        # finally:
        #     if cursor:
        #         cursor.close()

        # conexion = self.closeConnection(conn)

        # return rows

    # def updateUsuario  (self, usuario:ClientePremiumVO) -> int:
    #     conexion = self.getConnection()
    #     conn = None
    #     cursor = None
    #     rows = 0

    #     try:
    #         if conexion:
    #             conn = conexion
           
    #         else:
    #             print("La base de datos no esta disponible")

    #         cursor = conn.cursor()
    #         cursor.execute(self.SQL_UPDATE, (usuario.getNombreCompleto(),usuario.getTelefono(),usuario.getEmail(),usuario.getTitular(),usuario.getNumTarjeta(),usuario.getCvv(),usuario.getCaducidad(),usuario.getContraseña(), usuario.getDNI()))
    #         # conn.commit()
    #         #Asegurarse de que esos cambios se hagan permanentes: conn.commit(). Si conn.autocommit = True no es necesario llamar explícitamente a conn.commit() después de cada inserción, ya que la base de datos confirma automáticamente cada instrucción.
           
    #         #Devuelve 1 si la inserción fue exitosa
    #         rows = cursor.rowcount
    #     except Error as e:
    #         print("Error al actualizar usuario:", e)


    #     finally:
    #         if cursor:
    #             cursor.close()

    #     conexion = self.closeConnection(conn)

    #     return rows














