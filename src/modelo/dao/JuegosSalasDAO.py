from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src\modelo')

from vo.JuegosVO import * 
from dao.JuegosDAO import JuegosDao
from conexion.conexion2JDBC import Conexion
from dao.JuegosSalasInterface import JuegosSalasInterface
# Creamos la clase UsuarioDAO que manejará las operaciones de acceso a datos para los usuarios

class JuegosSalasDao(JuegosSalasInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT * FROM JuegosSalas"
    SQL_INSERT = "INSERT INTO JuegosSalas(IDJuegossalas, IDSala) VALUES (?, ?)"
    SQL_DELETE = "DELETE FROM JuegosSalas WHERE IDJuegossalas = ?"
    SQL_UPDATE = "UPDATE JuegosSalas SET IDSala= ? WHERE IDJuegossalas = ?"
    SQL_FILTER = "SELECT * FROM JuegosSalas WHERE IDJuegossalas = ?"
    SQL_SELECT_SERV = "SELECT IDServicios FROM servicios WHERE Nombre = ?"
    SQL_DELETE_SERV = "DELETE FROM Servicios WHERE IDServicios = ?"
    SQL_FILTER_JUEGO_GETALL = "SELECT Nombre FROM Juegos WHERE IDJuego = ?"
    SQL_FILTER_SERV = "SELECT * FROM Juegos WHERE IDJuego = ?"
    


    def getJuegosSalas(self) -> List[JuegosSalasVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        juegosSalas = []
        try:
            if conexion:
                conn = conexion
            else:
                print("La base de datos no esta disponible")
            #Crea un objeto para poder ejecutar consultas SQL sobre la conexion abierta
            cursor = conn.cursor()
            #Ejecuta de consulta SQL
            juegos_dao=JuegosDao()
            cursor.execute(self.SQL_SELECT) #Obtiene todas las filas resultantes de la consulta
            rows = cursor.fetchall()
            #Itera sobre todas las filas
            for row in rows:
                IDJuegoSala,IDSala= row
                cursor.execute(self.SQL_FILTER_JUEGO_GETALL,(IDJuegoSala, ))
                nombre = cursor.fetchone()[0] 
                juego_vo=juegos_dao.getJuego(nombre)
                #En juego_vo tenemos los atributos de la tabla Juegos...
                juegoSala = JuegosSalasVO()
                juegoSala.set_IDJuego(IDJuegoSala)
                juegoSala.set_IDSala(IDSala)
                juegoSala.set_Nombre(juego_vo.get_Nombre())
                juegoSala.set_Dificultad(juego_vo.get_Dificultad())
                juegoSala.set_Descripcion(juego_vo.get_Descripcion())
                juegoSala.set_ruta(juego_vo.get_ruta())
                juegosSalas.append(juegoSala)

        except Error as e:
            print("Error al seleccionar JuegosSalas:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return juegosSalas
    
    def getJuegoSalas(self,Titulo) -> JuegosSalasVO:
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
            #Primero, obtiene los datos de la tabla Juegos. Obtengamos su informacion:
            juegos_dao=JuegosDao()
            juego_vo=juegos_dao.getJuego(Titulo)
            #En juegovo tenemos los atributos de la tabla Juegos...
            cursor.execute(self.SQL_FILTER, (juego_vo.get_IDJuego(),)) #Obtiene todas las filas resultantes de la consulta
            row = cursor.fetchall()
            juegoSalas = JuegosSalasVO()
            IDJuegoSala,IDSala= row[0]   #Al filtrar por la clave primaria, solo hay 1 resultado almacenado en la 1º pos
            juegoSalas.set_IDJuego(IDJuegoSala)
            juegoSalas.set_IDSala(IDSala)
            juegoSalas.set_Nombre(juego_vo.get_Nombre())
            juegoSalas.set_Dificultad(juego_vo.get_Dificultad())
            juegoSalas.set_Descripcion(juego_vo.get_Descripcion())
            juegoSalas.set_ruta(juego_vo.get_ruta())

        except Error as e:
            print("Error al seleccionar JuegosSalas:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return juegoSalas
    
    #se hace el proximo dia
    def insertJuegosSalas (self, juegosSalas: JuegosSalasVO) -> int:
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
            #Primero, lo insertamos en el padre
            juego=JuegosVO(Nombre=juegosSalas.get_Nombre(),Dificultad=juegosSalas.get_Dificultad(),Descripcion=juegosSalas.get_Descripcion(),ruta=juegosSalas.get_ruta())
            juego_dao=JuegosDao()
            juego_dao.insertJuego(juego)
            cursor.execute(self.SQL_SELECT_SERV,(juegosSalas.get_Nombre(), ))
            identificador_servicio = cursor.fetchone()[0] 
            #Ahora, ya podemos insertarlo en la tabla juegosSalas.
            cursor.execute(self.SQL_INSERT, (identificador_servicio,juegosSalas.get_IDSala()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al insertar juegosSalas:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def deleteJuegosSalas (self, nombre) -> int:
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
            #Ahora, eliminamos el servicio de la tabla servicios (hay on delete cascade)
            cursor.execute(self.SQL_DELETE_SERV, (identificador_servicio,))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al eliminar JuegosSalas:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def updateJuegosSalas(self, juegosSalas:JuegosSalasVO) -> int:
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
            juegos=JuegosVO()
            juegos.set_Nombre(juegosSalas.get_Nombre())
            juegos.set_Descripcion(juegosSalas.get_Descripcion())
            juegos.set_Dificultad(juegosSalas.get_Dificultad())
            juegos.set_ruta(juegosSalas.get_ruta())
            juegos_dao=JuegosDao()
            juegos_dao.updateJuego(juegos)
            cursor.execute(self.SQL_UPDATE, (juegosSalas.get_IDSala(),juegosSalas.get_IDJuego()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar juegosSalas:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

# juego_sala1 = JuegosSalasVO()
# juego_sala1.set_IDJuego(1)
# juego_sala1.set_Nombre("Escape Room")
# juego_sala1.set_Dificultad("Alta")
# juego_sala1.set_Descripcion("Un juego desafiante de escape")
# juego_sala1.set_ruta("/ruta/escape_room")
# juego_sala1.set_IDSala(101)

# juego_sala2 = JuegosSalasVO()
# juego_sala2.set_IDJuego(2)
# juego_sala2.set_Nombre("Trivia Artística")
# juego_sala2.set_Dificultad("Media")
# juego_sala2.set_Descripcion("Juego de preguntas sobre arte")
# juego_sala2.set_ruta("/ruta/trivia_artistica")
# juego_sala2.set_IDSala(102)

# juego_sala3 = JuegosSalasVO()
# juego_sala3.set_IDJuego(3)
# juego_sala3.set_Nombre("Puzzle de Obras")
# juego_sala3.set_Dificultad("Baja")
# juego_sala3.set_Descripcion("Un puzzle con imágenes de obras de arte")
# juego_sala3.set_ruta("/ruta/puzzle_obras")
# juego_sala3.set_IDSala(103)

# juego_sala4 = JuegosSalasVO()
# juego_sala4.set_IDJuego(4)
# juego_sala4.set_Nombre("Adivina el Artista")
# juego_sala4.set_Dificultad("Media")
# juego_sala4.set_Descripcion("Identifica al artista de la obra mostrada")
# juego_sala4.set_ruta("/ruta/adivina_artista")
# juego_sala4.set_IDSala(101)

# juego_sala5 = JuegosSalasVO()
# juego_sala5.set_IDJuego(5)
# juego_sala5.set_Nombre("Memory de Arte")
# juego_sala5.set_Dificultad("Altisima")
# juego_sala5.set_Descripcion("Encuentra las parejas :D")
# juego_sala5.set_ruta("/ruta/memory_arte")
# # juego_sala5.set_IDSala(102)

# a=JuegosSalasDao()
# # # # a.insertJuegosSalas(juego_sala1)
# # # # a.insertJuegosSalas(juego_sala5)
# # # # a.deleteJuegosSalas("Escape Room")
# # # a.updateJuegosSalas(juego_sala5)
# # print(a.getJuegoSalas('Memory de Arte').Dificultad)
# print(a.getJuegosSalas())