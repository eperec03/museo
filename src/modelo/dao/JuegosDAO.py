from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')

from vo.JuegosVO import *
from conexion.conexion2JDBC import Conexion
from dao.JuegosInterface import JuegosInterface
# Creamos la clase UsuarioDAO que manejará las operaciones de acceso a datos para los usuarios

class JuegosDao(JuegosInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT * FROM juegos"
    SQL_INSERT = "INSERT INTO juegos(IdJuego, Nombre, Dificultad, Descripcion, Ruta) VALUES (?, ?, ?, ?, ?)"
    SQL_INSERT_SERV = "INSERT INTO Servicios(Nombre) VALUES (?)"
    SQL_DELETE_SERV = "DELETE FROM Juegos WHERE IdJuego = ?"
    SQL_UPDATE = "UPDATE juegos SET Nombre= ?, Dificultad= ?, Descripcion = ? WHERE IdJuego = ?"
    SQL_FILTER = "SELECT * FROM juegos WHERE IdJuego = ?"


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
                IdJuego,Nombre,Dificultad,Descripcion,ruta= row
                juego = JuegosVO()
                juego.set_IDJuego(IdJuego)
                juego.set_Descripcion(Descripcion)
                juego.set_Nombre(Nombre)
                juego.set_Dificultad(Dificultad)
                juego.set_ruta(ruta)
                juegos.append(juego)

        except Error as e:
            print("Error al seleccionar juego:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return juegos
    
    def getJuego(self,IdJuego) -> JuegosVO:
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
            cursor.execute(self.SQL_FILTER, (IdJuego,)) #Obtiene todas las filas resultantes de la consulta
            #Obtiene todas las filas resultantes de la consulta
            row = cursor.fetchall()
            juego = JuegosVO()
            if len(row)>0:
                IdJuego,Nombre,Dificultad,Descripcion,ruta= row[0]   #Al filtrar por la clave primaria, solo hay 1 resultado almacenado en la 1º pos
                juego.set_IDJuego(IdJuego)
                juego.set_Nombre(Nombre)
                juego.set_Dificultad(Dificultad)
                juego.set_Descripcion(Descripcion)
                juego.set_ruta(ruta)

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
            #Primero, vamos a insertarlo en Servicios:
            cursor.execute(self.SQL_INSERT_SERV, (juego.get_Nombre(), ))
            conn.commit()

            cursor.execute(self.SQL_SELECT_SERV, (juego.get_Nombre(), ))
            identificador_servicio = cursor.fetchone()[0] 
            cursor.execute(self.SQL_INSERT, (identificador_servicio,juego.get_Nombre(),juego.get_Dificultad(),juego.get_Descripcion(),juego.get_ruta()))
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

    def deleteJuego (self, IdJuego) -> int:
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
            #Primero, buscamos el identificador del servicio con el nombre (es unico)
            cursor.execute(self.SQL_DELETE_SERV, (IdJuego,))
            #Ahora, eliminamos el servicio de la tabla servicios (hay on delete cascade)
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
            #Antes de nada, necesitamos el identificador...lo buscamos con el nombre
            cursor.execute(self.SQL_SELECT_SERV, (juego.get_Nombre(), ))
            identificador_servicio = cursor.fetchone()[0] 
            cursor.execute(self.SQL_UPDATE, (juego.get_Nombre(),juego.get_Dificultad(),juego.get_Descripcion(),identificador_servicio))
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
    
a=JuegosDao()
print(a.deleteJuego('26'))
# # print(a.getJuego('Memory de Arte'))