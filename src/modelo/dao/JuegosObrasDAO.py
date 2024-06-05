from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src\modelo')

from vo.JuegosObrasVO import JuegosObrasVO 
from conexion.conexion2JDBC import Conexion
from dao.JuegosObrasInterface import JuegosObrasInterface
# Creamos la clase UsuarioDAO que manejará las operaciones de acceso a datos para los usuarios

class JuegosObrasDao(JuegosObrasInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT * FROM JuegosObras"
    SQL_INSERT = "INSERT INTO JuegosObras(IDJuegoObra, IDObra) VALUES (?, ?)"
    SQL_DELETE = "DELETE FROM JuegosObras WHERE IDJuegoObra = ?"
    SQL_UPDATE = "UPDATE JuegosObras SET IDObra= ? WHERE IDJuegoObra = ?"
    SQL_FILTER = "SELECT * FROM JuegosObras WHERE IDJuegoObra = ?"


    def getJuegosObras(self) -> List[JuegosObrasVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        juegosObras = []
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
                IDJuegoObra,IDObra= row
                juegosObras = JuegosObrasVO()
                juegosObras.setIDJuegoObra(IDJuegoObra)
                juegosObras.setIDObra(IDObra)
                juegosObras.append(JuegosObras)

        except Error as e:
            print("Error al seleccionar JuegosObras:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return juegosObras
    
    def getJuegosObras(self,id) -> JuegosObrasVO:
        conexion = self.getConnection()
        conn = None
        cursor = None
        try:
            if conexion:
                conn = conexion
            else:
                print("La base de datos no esta disponible")
            #Crea un objeto para poder ejecutar consultas SQL sobre la conexion abierta
            cursor = conn.cursor()
            #Ejecuta de consulta SQL
            cursor.execute(self.SQL_FILTER, (id,)) #Obtiene todas las filas resultantes de la consulta
            #Obtiene todas las filas resultantes de la consulta
            row = cursor.fetchall()
            JuegosObras = JuegosObrasVO()
            IDJuegoObra,IDObra= row[0]   #Al filtrar por la clave primaria, solo hay 1 resultado almacenado en la 1º pos
            JuegosObras.setIDJuegoObra(IDJuegoObra)
            JuegosObras.setIDObra(IDObra)
        except Error as e:
            print("Error al seleccionar JuegosObras:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return juegosObras
    
    #se hace el proximo dia
    def insertJuegosObras (self, juegosObras: JuegosObrasVO) -> int:
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
            cursor.execute(self.SQL_INSERT, (JuegosObras.getIDJuegoObra(),JuegosObras.getIDObra()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al insertar JuegosObras:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def deleteJuegosObras (self, id) -> int:
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
            cursor.execute(self.SQL_DELETE, (id,))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al eliminar JuegosObras:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def updateJuegosObras(self, juegosObras:JuegosObrasVO) -> int:
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
            cursor.execute(self.SQL_UPDATE, (JuegosObras.getIDObra(),JuegosObras.getIDJuegoObra()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar JuegosObras:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows
