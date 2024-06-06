from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src\modelo')

from vo.ObrasVO import ObrasVO 
from conexion.conexion2JDBC import Conexion
from dao.ObrasInterface import ObrasInterface
# Creamos la clase UsuarioDAO que manejará las operaciones de acceso a datos para los usuarios

class ObrasDao(ObrasInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT * FROM Obras"
    SQL_INSERT = "INSERT INTO Obras (Imagen, Titulo, Descripcion, Fecha, IDArtista, IDExposicion) VALUES (?, ?, ?, ?, ?, ?, ?)"
    SQL_DELETE = "DELETE FROM Obras WHERE IDObra = ?"
    SQL_UPDATE = "UPDATE Obras SET Imagen= ?, Titulo= ?, Descripcion = ?, Fecha = ?, IDArtista = ?, IDExposicion = ? WHERE IDObra = ?"
    SQL_FILTER = "SELECT * FROM Obras WHERE IDObra = ?"


    def getObras(self) -> List[ObrasVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        obras = []
        try:
            if conexion:
                conn = conexion
            else:
                print("La base de datos no esta disponible")
            #Crea un obra para poder ejecutar consultas SQL sobre la conexion abierta
            cursor = conn.cursor()
            #Ejecuta de consulta SQL
            cursor.execute(self.SQL_SELECT) #Obtiene todas las filas resultantes de la consulta
            rows = cursor.fetchall()
            #Itera sobre todas las filas
            for row in rows:
                IDObra,Imagen,Titulo,Descripcion,Fecha,IDArtista,IDExposicion= row
                obra = ObrasVO()
                obra.setIDObra(IDObra)
                obra.setDescripcion(Descripcion)
                obra.setImagen(Imagen)
                obra.setTitulo(Titulo)
                obra.setFecha(Fecha)
                obra.setIDArtista(IDArtista)
                obra.setIDExposicion(IDExposicion)
                obras.append(obra)

        except Error as e:
            print("Error al seleccionar obra:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return Obras
    
    def getObra(self,id) -> ObrasVO:
        conexion = self.getConnection()
        conn = None
        cursor = None
        try:
            if conexion:
                conn = conexion
            else:
                print("La base de datos no esta disponible")
            #Crea un obra para poder ejecutar consultas SQL sobre la conexion abierta
            cursor = conn.cursor()
            #Ejecuta de consulta SQL
            cursor.execute(self.SQL_FILTER, (id,)) #Obtiene todas las filas resultantes de la consulta
            #Obtiene todas las filas resultantes de la consulta
            row = cursor.fetchall()
            obra = ObrasVO()
            IDObra,Imagen,Titulo,Descripcion, Fecha, IDArtista, IDExposicion= row[0]   #Al filtrar por la clave primaria, solo hay 1 resultado almacenado en la 1º pos
            obra.setIDObra(IDObra)
            obra.setImagen(Imagen)
            obra.setDescripcion(Descripcion)
            obra.setTitulo(Titulo)
            obra.setFecha(Fecha)
            obra.setIDArtista(IDArtista)
            obra.setIDExposicion(IDExposicion)
        except Error as e:
            print("Error al seleccionar obra:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return obra
    
    #se hace el proximo dia
    def insertObra (self, obra: ObrasVO) -> int:
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
            cursor.execute(self.SQL_INSERT, (obra.getIDObra(),obra.getImagen(),obra.getTitulo(),obra.getDescripcion(),obra.getFecha(),obra.getIDArtista(),obra.getIDExposicion()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al insertar obra:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def deleteObra (self, id) -> int:
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
            print("Error al eliminar obra:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def updateObra(self, obra:ObrasVO) -> int:
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
            cursor.execute(self.SQL_UPDATE, (obra.getImagen(),obra.getTitulo(),obra.getDescripcion(),obra.getIDObra(),obra.getFecha(),obra.getIDArtista(),obra.getIDExposicion()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar obra:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows
