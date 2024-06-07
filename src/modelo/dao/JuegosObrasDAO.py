from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src\modelo')

from vo.JuegosVO import * 
from dao.JuegosDAO import *
from conexion.conexion2JDBC import Conexion
from dao.JuegosObrasInterface import JuegosObrasInterface
# Creamos la clase UsuarioDAO que manejará las operaciones de acceso a datos para los usuarios

class JuegosObrasDao(JuegosObrasInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT * FROM JuegosObras"
    SQL_INSERT = "INSERT INTO JuegosObras(IDJuegoObra, IDObra) VALUES (?, ?)"
    SQL_DELETE = "DELETE FROM JuegosObras WHERE IDJuegoObra = ?"
    SQL_UPDATE = "UPDATE JuegosObras SET IDObra= ? WHERE IDJuegoObra = ?"
    SQL_FILTER = "SELECT * FROM JuegosObras WHERE IDJuegoObra = ?"
    SQL_SELECT_SERV = "SELECT IDServicios FROM servicios WHERE Nombre = ?"
    SQL_DELETE_SERV = "DELETE FROM Servicios WHERE IDServicios = ?"




    def getJuegosObras(self) -> List[JuegosObrasVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        juegosObras = []
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
                IDJuegoObra,IDObra= row
                juegoObras = JuegosObrasVO()
                juegoObras.set_IDJuegoobra(IDJuegoObra)
                juegoObras.set_IDObra(IDObra)
                juegosObras.append(juegoObras)

        except Error as e:
            print("Error al seleccionar JuegosObras:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return juegosObras
    
    def getJuegosObras(self,id) -> JuegosObrasVO:
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
            JuegosObras = JuegosObrasVO()
            IDJuegoObra,IDObra= row[0]   #Al filtrar por la clave primaria, solo hay 1 resultado almacenado en la 1º pos
            JuegosObras.set_IDJuegoobra(IDJuegoObra)
            JuegosObras.set_IDObra(IDObra)
        except Error as e:
            print("Error al seleccionar JuegosObras:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return JuegosObras
    
    def insertJuegosObras (self, juegosObras: JuegosObrasVO) -> int:
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
            #Ahora, antes de crear la instancia de JuegosObras, hay que crearla en Juegos. Con los valores proporcionados:
            juego=JuegosVO(Nombre=juegosObras.get_Nombre(),Dificultad=juegosObras.get_Dificultad(),Descripcion=juegosObras.get_Descripcion(),ruta=juegosObras.get_ruta())
            juego_dao=JuegosDao()
            juego_dao.insertJuego(juego)
            cursor.execute(self.SQL_SELECT_SERV,(juegosObras.get_Nombre(), ))
            identificador_servicio = cursor.fetchone()[0] 
            #Ahora, ya podemos insertarlo en la tabla juegosObras.
            cursor.execute(self.SQL_INSERT, (identificador_servicio,juegosObras.get_IDObra()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al insertar JuegosObras:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def deleteJuegosObras (self, nombre) -> int:
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
            cursor.execute(self.SQL_SELECT_SERV, (nombre,))
            identificador_servicio = cursor.fetchone()[0] 
            print(identificador_servicio)
            #Ahora, eliminamos el servicio de la tabla servicios (hay on delete cascade)
            cursor.execute(self.SQL_DELETE_SERV, (identificador_servicio,))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al eliminar JuegosObras:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def updateJuegosObras(self, juegosObras:JuegosObrasVO) -> int:
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
            #Pimero, actualizamos los atributos de juegos;
            juegos=JuegosVO()
            juegos.set_Nombre(juegosObras.get_Nombre())
            juegos.set_Descripcion(juegosObras.get_Descripcion())
            juegos.set_Dificultad(juegosObras.get_Dificultad())
            juegos.set_ruta(juegosObras.get_ruta())
            juegos_dao=JuegosDao()
            juegos_dao.updateJuego(juegos)
            cursor.execute(self.SQL_UPDATE, (juegosObras.get_IDObra(),juegosObras.get_IDJuegoobra()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar JuegosObras:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows
    
a=JuegosObrasDao()
# # b=JuegosObrasVO()
# # b.set_Nombre('Snake')
# # b.set_Dificultad('Imposible')
# # b.set_Descripcion('Serpiente manzana ñam ñam')
# # b.set_ruta('/Escritorio')
# # b.set_IDObra('2')
# # a.insertJuegosObras(b)
# b=JuegosObrasVO()
# b.set_Nombre('Snake')
# b.set_Dificultad('Facilon')
# b.set_Descripcion('Serpiente manzana ñom ñom')
# b.set_ruta('/MiCasa')
# b.set_IDObra('3')
# a.updateJuegosObras(b)
a.deleteJuegosObras('Snake')
