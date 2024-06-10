from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src\modelo')

from vo.ArtistasVO import ArtistasVO 
from conexion.conexion2JDBC import Conexion
from dao.ArtistasInterface import ArtistasInterface

class ArtistasDao(ArtistasInterface, Conexion):
    SQL_SELECT = "SELECT * FROM artistas"
    SQL_INSERT = "INSERT INTO artistas(NombreArtista, FechaNac, FechaMuerte, Descripcion, Corriente) VALUES (?, ?, ?, ?, ?)"
    SQL_DELETE = "DELETE FROM artistas WHERE NombreArtista = ?"
    SQL_UPDATE = "UPDATE artistas SET FechaNac= ?, FechaMuerte = ?, Descripcion = ?, Corriente = ? WHERE NombreArtista = ?"
    SQL_FILTER = "SELECT * FROM artistas WHERE NombreArtista = ?"
    SQL_FILTER_NOMBRE = "SELECT * FROM artistas WHERE IDArtista = ?"


    def getArtistas(self) -> List[ArtistasVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        artistas = []
        try:
            if conexion:
                conn = conexion
            else:
                print("La base de datos no esta disponible")
            #Crea un obra para poder ejecutar consultas SQL sobre la conexion abierta
            cursor = conn.cursor()
            #Ejecuta de consulta SQL
            cursor.execute(self.SQL_SELECT) #Obtiene todas las filas resultantes de la consulta
            rows = cursor.fetchall()
            for row in rows:
                IdArtista, NombreArtista, FechaNac, FechaMuerte, Descripcion, Corriente = row
                artista = ArtistasVO()
                artista.setIdArtista(IdArtista)
                artista.setNombreArtista(NombreArtista)
                artista.setFechaNacimiento(FechaNac)
                artista.setFechaMuerte(FechaMuerte)
                artista.setDescripcion(Descripcion)
                artista.setCorriente(Corriente)
                artistas.append(artista)

        except Error as e:
            print("Error al seleccionar artista:", e)
        finally:
            if cursor:
                cursor.close()
        conexion = self.closeConnection(conn)
        return artistas
    
    def getArtista(self, NombreArtista) -> ArtistasVO:
        conexion = self.getConnection()
        conn = None
        cursor = None
        try:
            if conexion:
                conn = conexion
            else:
                print("La base de datos no esta disponible")
            cursor = conn.cursor()
            cursor.execute(self.SQL_FILTER, (NombreArtista,))
            row = cursor.fetchall()
            artista = ArtistasVO()
            if len(row)>0:
                IdArtista, NombreArtista, FechaNac, FechaMuerte, Descripcion, Corriente = row[0]
                artista.setIdArtista(IdArtista)
                artista.setNombreArtista(NombreArtista)
                artista.setFechaNacimiento(FechaNac)
                artista.setFechaMuerte(FechaMuerte)
                artista.setDescripcion(Descripcion)
                artista.setCorriente(Corriente)

        except Error as e:
            print("Error al seleccionar artista:", e)

        finally:
            if cursor:
                cursor.close()
        conexion = self.closeConnection(conn)

        return artista
    
    def insertArtista(self, artista: ArtistasVO) -> int:
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
            cursor.execute(self.SQL_INSERT, (artista.getNombreArtista(), artista.getFechaNacimiento(), artista.getFechaMuerte(), artista.getDescripcion(), artista.getCorriente()))
            conn.commit()
            rows = cursor.rowcount
        except Error as e:
            print("Error al insertar artista:", e)
        finally:
            if cursor:
                cursor.close()
        conexion = self.closeConnection(conn)
        return rows

    def deleteArtista(self, Nombre) -> int:
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
            cursor.execute(self.SQL_DELETE, (Nombre,))
            conn.commit()
            rows = cursor.rowcount
        except Error as e:
            print("Error al eliminar artista:", e)
        finally:
            if cursor:
                cursor.close()
        conexion = self.closeConnection(conn)
        return rows

    def updateArtista(self, artista: ArtistasVO) -> int:
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
            cursor.execute(self.SQL_UPDATE, (artista.getFechaNacimiento(), artista.getFechaMuerte(), artista.getDescripcion(), artista.getCorriente(), artista.getNombreArtista()))
            conn.commit()
            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar artista:", e)
        finally:
            if cursor:
                cursor.close()
        conexion = self.closeConnection(conn)
        return rows
    
    def getArtistaNombre(self, IDArtista) -> ArtistasVO:
        conexion = self.getConnection()
        conn = None
        cursor = None
        try:
            if conexion:
                conn = conexion
            else:
                print("La base de datos no esta disponible")
            cursor = conn.cursor()
            cursor.execute(self.SQL_FILTER_NOMBRE, (IDArtista,))
            row = cursor.fetchone()
            artista = None
            if len(row)>0:
                IDArtista, NombreArtista, FechaNac, FechaMuerte, Descripcion, Corriente = row
                artista = ArtistasVO(IDArtista,NombreArtista, FechaNac, FechaMuerte, Descripcion, Corriente)
        except Error as e:
            print("Error al seleccionar artista:", e)
        finally:
            if cursor:
                cursor.close()
        conexion = self.closeConnection(conn)
        return artista
# a=ArtistasDao()
# b=ArtistasVO()
# b.setNombreArtista('Jesus Dominguez')
# b.setFechaNacimiento('1900-12-12')
# b.setFechaMuerte('1940-08-12')
# b.setCorriente('Generacion del 19')
# b.setDescripcion('Un buen paisano')
# # a.deleteArtista('Jesus Dominguez')
# # print(a.getArtistas())
# print(a.getArtista('frida kahlo'))