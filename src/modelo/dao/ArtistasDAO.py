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
    SQL_INSERT = "INSERT INTO artistas(NombreArtista, FechaNacimiento, FechaMuerte, Descripcion, Corriente) VALUES (?, ?, ?, ?, ?)"
    SQL_DELETE = "DELETE FROM artistas WHERE NombreArtista = ?"
    SQL_UPDATE = "UPDATE artistas SET FechaNacimiento= ?, FechaMuerte = ?, Descripcion = ?, Corriente = ? WHERE NombreArtista = ?"
    SQL_FILTER = "SELECT * FROM artistas WHERE NombreArtista = ?"

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
            cursor = conn.cursor()
            cursor.execute(self.SQL_SELECT)
            rows = cursor.fetchall()
            for row in rows:
                IdArtista, NombreArtista, FechaNacimiento, FechaMuerte, Descripcion, Corriente = row
                artista = ArtistasVO(IdArtista, NombreArtista, FechaNacimiento, FechaMuerte, Descripcion, Corriente)
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
            row = cursor.fetchone()
            artista = None
            if row:
                IdArtista, NombreArtista, FechaNacimiento, FechaMuerte, Descripcion, Corriente = row
                artista = ArtistasVO(IdArtista, NombreArtista, FechaNacimiento, FechaMuerte, Descripcion, Corriente)
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

    def deleteArtista(self, artista: ArtistasVO) -> int:
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
            cursor.execute(self.SQL_DELETE, (artista.getNombreArtista(),))
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

