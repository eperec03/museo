from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src\modelo')

from vo.CatalogoVO import CatalogoVO 
from conexion.conexion2JDBC import Conexion
from dao.CatalogoInterface import CatalogoInterface

class CatalogoDao(CatalogoInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT * FROM catalogo"
    SQL_INSERT = "INSERT INTO catalogo(IDCatalogo, Imagen) VALUES (?, ?)"
    SQL_DELETE = "DELETE FROM catalogo WHERE IDCatalogo = ?"
    SQL_UPDATE = "UPDATE catalogo SET Imagen= ? WHERE IDCatalogo = ?"
    SQL_FILTER = "SELECT * FROM catalogo WHERE IDCatalogo = ?"


    def getCatalogo(self) -> List[CatalogoVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        catalogos = []
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
                IDCatalogo,Imagen= row
                catalogo = CatalogoVO()
                catalogo.setIDCatalogo(IDCatalogo)
                catalogo.setImagen(Imagen)
                catalogos.append(catalogo)

        except Error as e:
            print("Error al seleccionar catalogo:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return catalogo
    
    def getCatalogo(self,id) -> CatalogoVO:
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
            catalogo = CatalogoVO()
            IDCatalogo,Imagen= row[0]   #Al filtrar por la clave primaria, solo hay 1 resultado almacenado en la 1º pos
            catalogo.setIDCatalogo(IDCatalogo)
            catalogo.setImagen(Imagen)
        except Error as e:
            print("Error al seleccionar catalogo:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return catalogo
    
    #se hace el proximo dia
    def insertcatalogo (self, catalogo: CatalogoVO) -> int:
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
            cursor.execute(self.SQL_INSERT, (catalogo.getIDCatalogo(),catalogo.getImagen()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al insertar catalogo:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def deletecatalogo (self, id) -> int:
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
            print("Error al eliminar catalogo:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def updatecatalogo(self, catalogo:CatalogoVO) -> int:
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
            cursor.execute(self.SQL_UPDATE, (catalogo.getImagen(),catalogo.getIDCatalogo()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar catalogo:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows
