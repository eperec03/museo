from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src\modelo')

from vo.ReseñasVO import ReseñasVO 
from conexion.conexion2JDBC import Conexion
from dao.ReseñaInterface import ReseñasInterface
# Creamos la clase UsuarioDAO que manejará las operaciones de acceso a datos para los usuarios

class ReseñasDao(ReseñasInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT * FROM reseñas"
    SQL_INSERT = "INSERT INTO reseñas(IDObra, Texto, NumEstrellas, Visible, Fecha) VALUES (?, ?, ?, ?, ?)"
    SQL_DELETE = "DELETE FROM reseñas WHERE NumReseña = ?"
    SQL_UPDATE = "UPDATE reseñas SET IDObra= ?, Texto= ?, NumEstrellas = ?, Visible = ?, Fecha = ?, Agotado = ?, IDCatalogo = ? WHERE NumReseña = ?"
    SQL_FILTER = "SELECT * FROM reseñas WHERE NumReseña = ?"


    def getReseñas(self) -> List[ReseñasVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        reseñas = []
        try:
            if conexion:
                conn = conexion
            else:
                print("La base de datos no esta disponible")
            #Crea un reseña para poder ejecutar consultas SQL sobre la conexion abierta
            cursor = conn.cursor()
            #Ejecuta de consulta SQL
            cursor.execute(self.SQL_SELECT) #Obtiene todas las filas resultantes de la consulta
            rows = cursor.fetchall()
            #Itera sobre todas las filas
            for row in rows:
                NumReseña,IDObra,Texto,NumEstrellas,Visible,Fecha= row
                reseña = ReseñasVO()
                reseña.setNumReseña(NumReseña)
                reseña.setNumEstrellas(NumEstrellas)
                reseña.setIDObra(IDObra)
                reseña.setTexto(Texto)
                reseña.setVisible(Visible)
                reseña.setFecha(Fecha)
                reseñas.append(reseña)

        except Error as e:
            print("Error al seleccionar reseña:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return reseñas
    
    def getReseña(self,id) -> ReseñasVO:
        conexion = self.getConnection()
        conn = None
        cursor = None
        try:
            if conexion:
                conn = conexion
            else:
                print("La base de datos no esta disponible")
            #Crea un reseña para poder ejecutar consultas SQL sobre la conexion abierta
            cursor = conn.cursor()
            #Ejecuta de consulta SQL
            cursor.execute(self.SQL_FILTER, (id,)) #Obtiene todas las filas resultantes de la consulta
            #Obtiene todas las filas resultantes de la consulta
            row = cursor.fetchall()
            reseña = ReseñasVO()
            NumReseña,IDObra,Texto,NumEstrellas,Visible,Fecha= row[0]   #Al filtrar por la clave primaria, solo hay 1 resultado almacenado en la 1º pos
            reseña.setNumReseña(NumReseña)
            reseña.setIDObra(IDObra)
            reseña.setNumEstrellas(NumEstrellas)
            reseña.setVisible(Visible)
            reseña.setFecha(Fecha)
            reseña.setTexto(Texto)
        except Error as e:
            print("Error al seleccionar reseña:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return reseña
    
    #se hace el proximo dia
    def insertReseña (self, reseña: ReseñasVO) -> int:
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
            cursor.execute(self.SQL_INSERT, (reseña.getNumReseña(),reseña.getIDObra(),reseña.getTexto(),reseña.getNumEstrellas(),reseña.getVisible(),reseña.getFecha()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al insertar reseña:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def deleteReseña (self, id) -> int:
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
            print("Error al eliminar reseña:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def updateReseña(self, reseña:ReseñasVO) -> int:
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
            cursor.execute(self.SQL_UPDATE, (reseña.getIDObra(),reseña.getTexto(),reseña.getNumEstrellas(),reseña.getNumReseña(),reseña.getVisible()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar reseña:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows