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
    SQL_INSERT = "INSERT INTO catalogo(IDCatalogo,Titulo, Imagen) VALUES (?, ?,?)"
    SQL_DELETE_SERV = "DELETE FROM servicios WHERE Nombre = ?"
    SQL_UPDATE = "UPDATE catalogo SET Imagen= ? WHERE Titulo = ?"
    SQL_FILTER = "SELECT * FROM catalogo WHERE Titulo = ?"
    SQL_INSERT_SERV="INSERT INTO SERVICIOS (Nombre) VALUE (?)"
    SQL_FILTER_SERV = "SELECT IDServicios FROM Servicios WHERE Nombre=?"


    def getCatalogos(self) -> List[CatalogoVO]:
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
                IDCatalogo,Titulo,Portada= row
                catalogo = CatalogoVO()
                catalogo.setIdCatalogo(IDCatalogo)
                catalogo.setTitulo(Titulo)
                catalogo.setPortada(Portada)
                catalogos.append(catalogo)

        except Error as e:
            print("Error al seleccionar catalogo:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return catalogos
    
    def getCatalogo(self,Titulo) -> CatalogoVO:
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
            cursor.execute(self.SQL_FILTER, (Titulo,)) #Obtiene todas las filas resultantes de la consulta
            #Obtiene todas las filas resultantes de la consulta
            row = cursor.fetchall()
            catalogo = CatalogoVO()
            IDCatalogo,Titulo,Portada= row[0]   #Al filtrar por la clave primaria, solo hay 1 resultado almacenado en la 1º pos
            catalogo.setIdCatalogo(IDCatalogo)
            catalogo.setTitulo(Titulo)
            catalogo.setPortada(Portada)
        except Error as e:
            print("Error al seleccionar catalogo:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return catalogo
    
    def insertCatalogo (self, catalogo: CatalogoVO) -> int:
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
            #Primero, lo metemos en servicios:
            cursor.execute(self.SQL_INSERT_SERV, (catalogo.getTitulo(),))
            conn.commit()
            cursor.execute(self.SQL_FILTER_SERV,(catalogo.getTitulo(),))
            id_serv=cursor.fetchone()[0] 
            cursor.execute(self.SQL_INSERT, (id_serv,catalogo.getTitulo(),catalogo.getPortada()))
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

    def deleteCatalogo (self, Titulo) -> int:
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
            #eliminamos en servicios(on delete cascade)
            cursor.execute(self.SQL_DELETE_SERV, (Titulo,))
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

    def updateCatalogo(self, catalogo:CatalogoVO) -> int:
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
            cursor.execute(self.SQL_UPDATE, (catalogo.getPortada(),catalogo.getTitulo()))
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

# a=CatalogoDao()
# b=CatalogoVO()
# b.setPortada('imagen.png')
# b.setTitulo('Catalogosisi')
# # a.insertCatalogo(b)
# a.deleteCatalogo('Catalogosisi')