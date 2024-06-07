from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src\modelo')
from vo.SalasVO import SalasVO
from conexion.conexion2JDBC import Conexion
from dao.SalasInterface import SalasInterface

class SalasDao(SalasInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_FILTER = "SELECT * FROM salas WHERE NumeroSala = ?"
    SQL_SELECT = "SELECT * FROM Salas"

    def getSalas(self) -> List[SalasVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        salas = []
        try:
            if conexion:
                conn = conexion
            else:
                print("La base de datos no esta disponible")
            #Crea un sala para poder ejecutar consultas SQL sobre la conexion abierta
            cursor = conn.cursor()
            #Ejecuta de consulta SQL
            cursor.execute(self.SQL_SELECT) #Obtiene todas las filas resultantes de la consulta
            rows = cursor.fetchall()
            #Itera sobre todas las filas
            for row in rows:
                sala = SalasVO()
                Id,imagen,capacidad,tematica,idMapa=rows[0]
                sala = SalaVO()
                sala.setNumeroSala(Id)
                sala.setImagen(imagen)
                sala.setCapacidad(capacidad)
                sala.setTematica(tematica)
                sala.setIdMapa(idMapa)
                salas.append(sala)

        except Error as e:
            print("Error al seleccionar sala:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return salas

    def getSala(self,Id) -> SalaVO:
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
            cursor.execute(self.SQL_FILTER, (Id,)) #Obtiene todas las filas resultantes de la consulta
            rows = cursor.fetchall()
            sala = SalasVO()
            Id,imagen,capacidad,tematica,idMapa=rows[0]
            sala = SalaVO()
            sala.setNumeroSala(Id)
            sala.setImagen(imagen)
            sala.setCapacidad(capacidad)
            sala.setTematica(tematica)
            sala.setIdMapa(idMapa)
        except Error as e:
            print("Error al seleccionar sala:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return sala

    def updateSala(self, Salas:SalasVO) -> int:
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


            cursor.execute(self.SQL_UPDATE, (sala.getNumeroSala(),sala.getImagen(),sala.getCapacidad(),sala.getTematica(),sala.getIdMapa()))
            sala.setNumeroSala(Id)
            sala.setImagen(imagen)
            sala.setCapacidad(capacidad)
            sala.setTematica(tematica)
            sala.setIdMapa(idMapa)
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar sala:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows
    


