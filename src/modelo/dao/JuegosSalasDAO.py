from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src\modelo')

from vo.JuegosVO import * 
from conexion.conexion2JDBC import Conexion
from dao.JuegosSalasInterface import JuegosSalasInterface
# Creamos la clase UsuarioDAO que manejará las operaciones de acceso a datos para los usuarios

class JuegosSalasDao(JuegosSalasInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT * FROM JuegosSalas"
    SQL_INSERT = "INSERT INTO JuegosSalas(IDJuegoSala, IDSala) VALUES (?, ?)"
    SQL_DELETE = "DELETE FROM JuegosSalas WHERE IDJuegoSala = ?"
    SQL_UPDATE = "UPDATE JuegosSalas SET IDSala= ? WHERE IDJuegoSala = ?"
    SQL_FILTER = "SELECT * FROM JuegosSalas WHERE IDJuegoSala = ?"


    def getJuegosSalas(self) -> List[JuegosSalasVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        juegosSalas = []
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
                IDJuegoSala,IDSala= row
                juegoSalas = JuegosSalasVO()
                juegoSalas.set_IDJuegossalas(IDJuegoSala)
                juegoSalas.set_IDJuegossalas(IDSala)
                juegosSalas.append(juegoSalas)

        except Error as e:
            print("Error al seleccionar JuegosSalas:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return juegosSalas
    
    def getJuegoSalas(self,id) -> JuegosSalasVO:
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
            juegoSalas = JuegosSalasVO()
            IDJuegoSala,IDSala= row[0]   #Al filtrar por la clave primaria, solo hay 1 resultado almacenado en la 1º pos
            juegoSalas.set_IDJuegossalas(IDJuegoSala)
            juegoSalas.set_IDSala(IDSala)
        except Error as e:
            print("Error al seleccionar JuegosSalas:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return juegoSalas
    
    #se hace el proximo dia
    def insertJuegosSalas (self, juegosSalas: JuegosSalasVO) -> int:
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
            cursor.execute(self.SQL_INSERT, (juegosSalas.get_IDJuegossalas(),juegosSalas.get_IDSala()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al insertar juegosSalas:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def deleteJuegosSalas (self, id) -> int:
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
            print("Error al eliminar JuegosSalas:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def updateJuegosSalas(self, juegosSalas:JuegosSalasVO) -> int:
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
            cursor.execute(self.SQL_UPDATE, (juegosSalas.get_IDSala(),juegosSalas.get_IDJuegossalas()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar juegosSalas:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows
