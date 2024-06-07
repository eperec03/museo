from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src')

from modelo.vo.ResenasVO import ResenasVO 
from modelo.conexion.conexion2JDBC import Conexion
from modelo.dao.ResenasInterface import ResenasInterface
# Creamos la clase UsuarioDAO que manejará las operaciones de acceso a datos para los usuarios

class ResenasDao(ResenasInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT * FROM resenas"
    SQL_INSERT = "INSERT INTO resenas(Titulo, IDObra, Texto, NumEstrellas, Visible, Fecha) VALUES (?, ?, ?, ?, ?, ?)"
    SQL_DELETE = "DELETE FROM resenas WHERE Titulo = ?"
    SQL_UPDATE = "UPDATE resenas SET IDObra= ?, Texto= ?, NumEstrellas = ?, Visible = ?, Fecha = ?, Agotado = ?, IDCatalogo = ? WHERE Titulo = ?"
    SQL_FILTER = "SELECT * FROM resenas WHERE Titulo = ?"


    def getResenas(self) -> List[ResenasVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        resenas = []
        try:
            if conexion:
                conn = conexion
            else:
                print("La base de datos no esta disponible")
            #Crea un resena para poder ejecutar consultas SQL sobre la conexion abierta
            cursor = conn.cursor()
            #Ejecuta de consulta SQL
            cursor.execute(self.SQL_SELECT) #Obtiene todas las filas resultantes de la consulta
            rows = cursor.fetchall()
            #Itera sobre todas las filas
            for row in rows:
                NumResena,Titulo ,IDObra,Texto,NumEstrellas,Visible,Fecha= row
                resena = ResenasVO()
                resena.setNumResena(NumResena)
                resena.setTitulo(Titulo)
                resena.setNumEstrellas(NumEstrellas)
                resena.setIdObra(IDObra)
                resena.setTexto(Texto)
                resena.setVisible(Visible)
                resena.setFecha(Fecha)
                resenas.append(resena)

        except Error as e:
            print("Error al seleccionar resena:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return resenas
    
    def getResena(self,id) -> ResenasVO:
        conexion = self.getConnection()
        conn = None
        cursor = None
        try:
            if conexion:
                conn = conexion
            else:
                print("La base de datos no esta disponible")
            #Crea un resena para poder ejecutar consultas SQL sobre la conexion abierta
            cursor = conn.cursor()
            #Ejecuta de consulta SQL
            cursor.execute(self.SQL_FILTER, (id,)) #Obtiene todas las filas resultantes de la consulta
            #Obtiene todas las filas resultantes de la consulta
            row = cursor.fetchall()
            resena = ResenasVO()
            NumResena,Titulo,IDObra,Texto,NumEstrellas,Visible,Fecha= row[0]   #Al filtrar por la clave primaria, solo hay 1 resultado almacenado en la 1º pos
            resena.setNumResena(NumResena)
            resena.setTitulo(Titulo)
            resena.setIdObra(IDObra)
            resena.setNumEstrellas(NumEstrellas)
            resena.setVisible(Visible)
            resena.setFecha(Fecha)
            resena.setTexto(Texto)
        except Error as e:
            print("Error al seleccionar resena:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return resena
    
    #se hace el proximo dia
    def insertResena (self, resena: ResenasVO) -> int:
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
            cursor.execute(self.SQL_INSERT, (resena.getTitulo(),resena.getIdObra(),resena.getTexto(),resena.getNumEstrellas(),resena.getVisible(),resena.getFecha()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al insertar resena:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def deleteResena (self, id) -> int:
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
            print("Error al eliminar resena:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def updateResena(self, resena:ResenasVO) -> int:
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
            cursor.execute(self.SQL_UPDATE, (resena.getIdObra(),resena.getTexto(),resena.getNumEstrellas(),resena.getNumResena(),resena.getVisible()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar resena:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows
    
a=ResenasDao()
b=ResenasVO()
b.setTitulo('Amor incondicional a panceta')
b.setIdObra(1)
b.setFecha('2024-12-12')
b.setNumEstrellas(5)
b.setTexto('Me encanta panceta')
b.setVisible(1)
# a.insertResena(b)
print(a.getResenas())
