from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src\modelo')

from vo.ArtistasVO import ArtistasVO 
from conexion.conexion2JDBC import Conexion
from dao.artistasInterface import ArtistasInterface
# Creamos la clase UsuarioDAO que manejará las operaciones de acceso a datos para los usuarios

class ArtistasDao(ArtistasInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
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
            #Crea un objeto para poder ejecutar consultas SQL sobre la conexion abierta
            cursor = conn.cursor()
            #Ejecuta de consulta SQL
            cursor.execute(self.SQL_SELECT) #Obtiene todas las filas resultantes de la consulta
            rows = cursor.fetchall()
            #Itera sobre todas las filas
            for row in rows:
                NombreArtista,FechaNacimiento,FechaMuerte,Descripcion,Corriente= row
                artista = ArtistasVO()
                artista.setNombreArtista(NombreArtista)
                artista.setFechaNacimiento(FechaNacimiento)
                artista.setFechaMuerte(FechaMuerte)
                artista.setDescripcion(Descripcion)
                artista.setDescripcion(Corriente)
                artista.append(artista)

        except Error as e:
            print("Error al seleccionar artista:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return artistas
    
    def getArtista(self,id) -> ArtistasVO:
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
            artista = ArtistasVO()
            NombreArtista,FechaNacimiento,FechaMuerte,Descripcion,Corriente= row[0]   #Al filtrar por la clave primaria, solo hay 1 resultado almacenado en la 1º pos
            artista.setNombreArtista(NombreArtista)
            artista.setFechaNacimiento(FechaNacimiento)
            artista.setFechaMuerte(FechaMuerte)
            artista.setDescripcion(Descripcion)
            artista.setCorriente(Corriente)
        except Error as e:
            print("Error al seleccionar artista:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return artista
    
    #se hace el proximo dia
    def insertArtista (self, artista: ArtistasVO) -> int:
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
            cursor.execute(self.SQL_INSERT, (artista.getNombreArtista(),artista.getFechaNacimiento(),artista.getFechaMuerte(),artista.getDescripcion(), artista.getCorriente()))
            # conn.commit()
            #Asegurarse de que esos cambios se hagan permanentes: conn.commit(). Si conn.autocommit = True no es necesario llamar explícitamente a conn.commit() después de cada inserción, ya que la base de datos confirma automáticamente cada instrucción.
           
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al insertar artista:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def deleteArtista (self, artista:ArtistasVO) -> int:
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
            #Asegurarse de que esos cambios se hagan permanentes: conn.commit(). Si conn.autocommit = True no es necesario llamar explícitamente a conn.commit() después de cada inserción, ya que la base de datos confirma automáticamente cada instrucción.
            # conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al eliminar artista:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def updateArtista(self, artista:ArtistasVO) -> int:
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
            cursor.execute(self.SQL_UPDATE, ( artista.getFechaNacimiento(),artista.getFechaMuerte(),artista.getDescripcion(), artista.getCorriente()))
            # conn.commit()
            #Asegurarse de que esos cambios se hagan permanentes: conn.commit(). Si conn.autocommit = True no es necesario llamar explícitamente a conn.commit() después de cada inserción, ya que la base de datos confirma automáticamente cada instrucción.
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar artista:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows



