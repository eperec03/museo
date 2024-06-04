IDObrafrom jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src\modelo')

from vo.JuegosVO import JuegosVO 
from conexion.conexion2JDBC import Conexion
from dao.JuegosInterface import JuegosInterface
# Creamos la clase UsuarioDAO que manejará las operaciones de acceso a datos para los usuarios

class JuegosDao(JuegosInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT * FROM juegos"
    SQL_INSERT = "INSERT INTO juegos(IDJuego, Nombre, Dificultad, Descripcion) VALUES (?, ?, ?, ?)"
    SQL_DELETE = "DELETE FROM juegos WHERE IDJuego = ?"
    SQL_UPDATE = "UPDATE juegos SET Nombre= ?, Dificultad= ?, Descripcion = ? WHERE IDJuego = ?"
    SQL_FILTER = "SELECT * FROM juegos WHERE IDJuego = ?"


    def getJuegos(self) -> List[JuegosVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        juegos = []
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
                IDJuego,Nombre,Dificultad,Descripcion= row
                juego = JuegosVO()
                juego.setIDJuego(IDJuego)
                juego.setDescripcion(Descripcion)
                juego.setNombre(Nombre)
                juego.setDificultad(Dificultad)
                juegos.append(juego)

        except Error as e:
            print("Error al seleccionar juego:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return Juegos
    
    def getJuego(self,id) -> JuegosVO:
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
            juego = JuegosVO()
            IDJuego,Nombre,Dificultad,Descripcion= row[0]   #Al filtrar por la clave primaria, solo hay 1 resultado almacenado en la 1º pos
            juego.setIDJuego(IDJuego)
            juego.setNombre(Nombre)
            juego.setDescripcion(Descripcion)
            juego.setDificultad(Dificultad)
        except Error as e:
            print("Error al seleccionar juego:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return juego
    
    #se hace el proximo dia
    def insertJuego (self, juego: JuegosVO) -> int:
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
            cursor.execute(self.SQL_INSERT, (Juego.getIDJuego(),Juego.getNombre(),Juego.getDificultad(),Juego.getDescripcion()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al insertar juego:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def deleteJuego (self, id) -> int:
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
            print("Error al eliminar juego:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def updateJuego(self, juego:JuegosVO) -> int:
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
            cursor.execute(self.SQL_UPDATE, (juego.getNombre(),juego.getDificultad(),juego.getDescripcion(),juego.getIDJuego()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar juego:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows