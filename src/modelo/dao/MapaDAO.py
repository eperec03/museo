from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src\modelo')
from vo.MapaVO import MapaVO
from conexion.conexion2JDBC import Conexion
from dao.MapaInterface import MapaInterface

class MapaDao(MapaInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT * FROM MAPA"
    SQL_INSERT = "INSERT INTO MAPA(IdMapa, Imagen) VALUES (?, ?)"
    SQL_UPDATE = "UPDATE MAPA SET Imagen = ? WHERE IdMapa = ?"


    def getInfoMapa(self) -> MapaVO:
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
            cursor.execute(self.SQL_SELECT) #Obtiene todas las filas resultantes de la consulta
            rows = cursor.fetchall()
            id,imagen=rows[0]
            mapa = MapaVO()
            mapa.setIdMapa(id)
            mapa.setImagen(imagen)
        except Error as e:
            print("Error al seleccionar usuarios:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return mapa
    


