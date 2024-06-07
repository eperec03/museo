from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src\modelo')

from vo.ExposicionesVO import ExposicionesVO 
from conexion.conexion2JDBC import Conexion
from dao.ExposicionesInterface import ExposicionesInterface
# Creamos la clase UsuarioDAO que manejará las operaciones de acceso a datos para los usuarios

class ExposicionesDao(ExposicionesInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT * FROM exposiciones"
    SQL_INSERT = "INSERT INTO exposiciones(IDExposiciones, Titulo, Imagen, Descripcion, NumSala) VALUES (?, ?, ?, ?)"
    SQL_DELETE = "DELETE FROM exposiciones WHERE IDExposiciones = ?"
    SQL_UPDATE = "UPDATE exposiciones SET Titulo= ?, Imagen= ?, Descripcion = ?, NumSala = ? WHERE IDExposiciones = ?"
    SQL_FILTER = "SELECT * FROM exposiciones WHERE IDExposiciones = ?"


    def getExposiciones(self) -> List[ExposicionesVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        exposiciones = []
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
                IDImagen,Titulo,Imagen,Descripcion,NumSala= row
                exposicion = ExposicionesVO()
                exposicion.setIDExposiciones(IDExposiciones)
                exposicion.setDescripcion(Descripcion)
                exposicion.setTitulo(Titulo)
                exposicion.setImagen(Imagen)
                exposicion.setNumSala(NumSala)
                exposiciones.append(exposicion)

        except Error as e:
            print("Error al seleccionar exposicion:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return exposiciones
    
    def getExposicion(self,id) -> ExposicionesVO:
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
            exposicion = ExposicionesVO()
            IDExposiciones,Titulo,Imagen,Descripcion,NumSala= row[0]   #Al filtrar por la clave primaria, solo hay 1 resultado almacenado en la 1º pos
            exposicion.setIdImagen(IDImagen)
            exposicion.setTitulo(Titulo)
            exposicion.setDescripcion(Descripcion)
            exposicion.setImagen(Imagen)
            exposicion.setNumSala(NumSala)
        except Error as e:
            print("Error al seleccionar exposicion:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return exposicion
    
    #se hace el proximo dia
    def insertexposicion (self, exposicion: ExposicionesVO) -> int:
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
            cursor.execute(self.SQL_INSERT, (exposicion.getIDExposiciones(),exposicion.getTitulo(),exposicion.getImagen(),exposicion.getDescripcion(),exposicion.getNumSala()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al insertar exposicion:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def deleteExposicion (self, id) -> int:
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
            print("Error al eliminar exposicion:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def updateExposicion(self, exposicion:ExposicionesVO) -> int:
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
            cursor.execute(self.SQL_UPDATE, (exposicion.getTitulo(),exposicion.getImagen(),exposicion.getDescripcion(),exposicion.getIdImagen(), exposicion.getNumSala()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar exposicion:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows
