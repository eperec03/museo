from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src\modelo')

from vo.ObrasVO import ObrasVO 
from conexion.conexion2JDBC import Conexion
from dao.ObrasInterface import ObrasInterface
# Creamos la clase UsuarioDAO que manejará las operaciones de acceso a datos para los usuarios

class ObrasDao(ObrasInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT * FROM Obras"
    SQL_INSERT = "INSERT INTO Obras (Titulo, Descripcion, Fecha, Imagen, IDArtista, NumSala) VALUES (?, ?, ?, ?, ?, ?)"
    SQL_DELETE = "DELETE FROM Obras WHERE Titulo = ?"
    SQL_UPDATE = "UPDATE Obras SET Descripcion= ?, Fecha = ?, Imagen = ?, IDArtista = ?, NumSala = ? WHERE Titulo = ?"
    SQL_FILTER_TITULO = "SELECT * FROM Obras WHERE Titulo = ?"
    SQL_FILTER_ID = "SELECT * FROM Obras WHERE IDObra = ?"

    SQL_FILTER_SALA="SELECT * FROM Obras WHERE ID"


    def getObras(self) -> List[ObrasVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        obras = []
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
            #Itera sobre todas las filas
            for row in rows:
                IdObra,Imagen,Titulo,Descripcion,Fecha,IdArtista,NumSala= row
                obra = ObrasVO()
                obra.setIdObra(IdObra)
                obra.setDescripcion(Descripcion)
                obra.setImagen(Imagen)
                obra.setTitulo(Titulo)
                obra.setFecha(Fecha)
                obra.setIdArtista(IdArtista)
                obra.setNumSala(NumSala)
                obras.append(obra)

        except Error as e:
            print("Error al seleccionar obra:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return obras
    
    def getObraTitulo(self,titulo) -> ObrasVO:
        conexion = self.getConnection()
        conn = None
        cursor = None
        obras = []
        try:
            if conexion:
                conn = conexion
            else:
                print("La base de datos no esta disponible")
            #Crea un obra para poder ejecutar consultas SQL sobre la conexion abierta
            cursor = conn.cursor()
            #Ejecuta de consulta SQL
            cursor.execute(self.SQL_FILTER_TITULO, (titulo,)) #Obtiene todas las filas resultantes de la consulta
            #Obtiene todas las filas resultantes de la consulta
            row = cursor.fetchall()
            obra = ObrasVO()
            if len(row)>0:
                IdObra,Imagen,Titulo,Descripcion, Fecha, IdArtista, NumSala= row[0]   #Al filtrar por la clave primaria, solo hay 1 resultado almacenado en la 1º pos
                obra.setIdObra(IdObra)
                obra.setImagen(Imagen)
                obra.setDescripcion(Descripcion)
                obra.setTitulo(Titulo)
                obra.setFecha(Fecha)
                obra.setIdArtista(IdArtista)
                obra.setNumSala(NumSala)
                obras.append(obra)
        except Error as e:
            print("Error al seleccionar obra:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return obras
    
    def getObraId(self,titulo) -> ObrasVO:
        conexion = self.getConnection()
        conn = None
        cursor = None
        try:
            if conexion:
                conn = conexion
            else:
                print("La base de datos no esta disponible")
            #Crea un obra para poder ejecutar consultas SQL sobre la conexion abierta
            cursor = conn.cursor()
            #Ejecuta de consulta SQL
            cursor.execute(self.SQL_FILTER_ID, (titulo,)) #Obtiene todas las filas resultantes de la consulta
            #Obtiene todas las filas resultantes de la consulta
            row = cursor.fetchall()
            obra = ObrasVO()
            IdObra,Imagen,Titulo,Descripcion, Fecha, IdArtista, NumSala= row[0]   #Al filtrar por la clave primaria, solo hay 1 resultado almacenado en la 1º pos
            obra.setIdObra(IdObra)
            obra.setImagen(Imagen)
            obra.setDescripcion(Descripcion)
            obra.setTitulo(Titulo)
            obra.setFecha(Fecha)
            obra.setIdArtista(IdArtista)
            obra.setNumSala(NumSala)
        except Error as e:
            print("Error al seleccionar obra:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return obra
    
    #se hace el proximo dia
    def insertObra (self, obra: ObrasVO) -> int:
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
            cursor.execute(self.SQL_INSERT, (obra.getTitulo(),obra.getDescripcion(),obra.getFecha(),obra.getImagen(),obra.getIdArtista(),obra.getNumSala()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al insertar obra:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def deleteObra (self, titulo) -> int:
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
            cursor.execute(self.SQL_DELETE, (titulo,))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al eliminar obra:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def updateObra(self, obra:ObrasVO) -> int:
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
            cursor.execute(self.SQL_UPDATE, (obra.getDescripcion(),obra.getFecha(),obra.getImagen(),obra.getIdArtista(),obra.getNumSala(),obra.getTitulo()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar obra:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

# obra1 = ObrasVO()
# obra1.setIdObra(1)
# obra1.setTitulo("La Noche Estrellada")
# obra1.setDescripcion("Una pintura famosa de Vincent van Gogh")
# obra1.setFecha("1889-06-01")
# obra1.setImagen("noche_estrellada.jpg")
# obra1.setIdArtista(3)
# obra1.setNumSala(2)


# obra2 = ObrasVO()
# obra2.setIdObra(2)
# obra2.setTitulo("Mona Lisa")
# obra2.setDescripcion("Una pintura de Leonardo da Vinci")
# obra2.setFecha("1503-10-01")
# obra2.setImagen("mona_lisa.jpg")
# obra2.setIdArtista(2)
# obra2.setNumSala(2)

# obra3 = ObrasVO()
# obra3.setIdObra(3)
# obra3.setTitulo("El Grito")
# obra3.setDescripcion("Una pintura de Clarita Ule")
# obra3.setFecha("1893-01-01")
# obra3.setImagen("el_grito.jpg")
# obra3.setIdArtista(2)
# obra3.setNumSala(103)

# a=ObrasDao()
# print(a.getObraTitulo('La Gioconda'))