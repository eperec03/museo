from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src\modelo')

from vo.SubastasVO import SubastasVO 
from conexion.conexion2JDBC import Conexion
from dao.SubastasInterface import SubastasInterface
# Creamos la clase UsuarioDAO que manejará las operaciones de acceso a datos para los usuarios

class SubastasDao(SubastasInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT * FROM Subastas"
    SQL_INSERT = "INSERT INTO Subastas(Titulo, Descripcion, Fecha) VALUES (?, ?, ?)"
    SQL_DELETE = "DELETE FROM Subastas WHERE Titulo = ?"
    SQL_UPDATE = "UPDATE Subastas SET Titulo= ?, Descripcion= ?, Fecha = ? WHERE Titulo = ?"
    SQL_FILTER = "SELECT * FROM Subastas WHERE IDSubasta = ?"


    def getSubastas(self) -> List[SubastasVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        subastas = []
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
                IDSubasta,Titulo,Descripcion,Fecha= row
                subasta = SubastasVO()
                subasta.setIdSubastas(IDSubasta)
                subasta.setDescripcion(Descripcion)
                subasta.setTitulo(Titulo)
                subasta.setFecha(Fecha)
                subastas.append(subasta)

        except Error as e:
            print("Error al seleccionar subasta:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return subastas
    
    def getSubasta(self,id) -> SubastasVO:
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
            subasta = SubastasVO()
            IDSubasta,Titulo,Descripcion,Fecha = row[0]   #Al filtrar por la clave primaria, solo hay 1 resultado almacenado en la 1º pos
            subasta.setIdSubastas(IDSubasta)
            subasta.setTitulo(Titulo)
            subasta.setFecha(Fecha)
            subasta.setDescripcion(Descripcion)
        except Error as e:
            print("Error al seleccionar subasta:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return subasta
    
    #se hace el proximo dia
    def insertSubasta (self, subasta: SubastasVO) -> int:
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
            cursor.execute(self.SQL_INSERT, (subasta.getTitulo(),subasta.getDescripcion(),subasta.getFecha()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al insertar subasta:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def deleteSubasta (self, id) -> int:
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
            print("Error al eliminar subasta:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def updateSubasta(self, subasta:SubastasVO) -> int:
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
            cursor.execute(self.SQL_UPDATE, (subasta.getTitulo(),subasta.getDescripcion(),subasta.getFecha(),subasta.getTitulo()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar subasta:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows
    
# a=SubastasDao()
# b=SubastasVO()
# b.setDescripcion('Vendemos a Panceta, Puska,...')
# b.setFecha('2024-12-06')
# b.setTitulo('ClaritaULE')
# # a.insertSubasta(b)
# print(str(a.getSubastas()[0].Descripcion))
# c=SubastasVO()
# c.setTitulo('ClaritaULE')
# c.setFecha('2024-05-29')
# c.setDescripcion('Vendemos a Panceta, Puska,...')
# a.updateSubasta(c)






