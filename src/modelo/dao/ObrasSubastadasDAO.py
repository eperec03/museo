from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src\modelo')

from vo.ObrasSubastadasVO import ObrasSubastadasVO 
from conexion.conexion2JDBC import Conexion
from dao.ObrasSubastadasInterface import ObrasSubastadasInterface
# Creamos la clase UsuarioDAO que manejará las operaciones de acceso a datos para los usuarios

class ObrasSubastadasDao(ObrasSubastadasInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT * FROM ObrasSubastadas"
    SQL_INSERT = "INSERT INTO ObrasSubastadas (PrecioSalida, PrecioVenta, MejorPostor, Fecha, IDArtista, IDExposicion) VALUES (?, ?, ?, ?, ?, ?, ?)"
    SQL_DELETE = "DELETE FROM ObrasSubastadas WHERE IDObra = ?"
    SQL_UPDATE = "UPDATE ObrasSubastadas SET PrecioSalida= ?, PrecioVenta= ?, MejorPostor = ?, Fecha = ?, IDArtista = ?, IDExposicion = ? WHERE IDObra = ?"
    SQL_FILTER = "SELECT * FROM ObrasSubastadas WHERE IDObra = ?"
    SQL_SELECT_SERV = "SELECT IDObra FROM obras WHERE Nombre = ?"


    def getObrasSubastadas(self) -> List[ObrasSubastadasVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        obrasSubastadas = []
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
                IdObra,Titulo,Descripcion,Fecha,Imagen,IdArtista,IdExposicion,PrecioSalida,PrecioVenta,MejorPostor= row
                obraSubastada = ObrasSubastadasVO()
                obraSubastada.setIDObra(IDObra)
                obraSubastada.setTitulo(Titulo)
                obraSubastada.setDescripcion(Descripcion)
                obraSubastada.setFecha(Fecha)
                obraSubastada.setImagen(Imagen)
                obraSubastada.setIdArtista(IdArtista)
                obraSubastada.setIdExposicion(IdExposicion)
                obraSubastada.setMejorPostor(MejorPostor)
                obraSubastada.setPrecioSalida(PrecioSalida)
                obraSubastada.setPrecioVenta(PrecioVenta)
                obrasSubastadas.append(obraSubastada)

        except Error as e:
            print("Error al seleccionar obra:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return obrasSubastadas
    
    def getObraSubastada(self,Id) -> ObrasSubastadasVO:
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
            cursor.execute(self.SQL_FILTER, (Id,)) #Obtiene todas las filas resultantes de la consulta
            #Obtiene todas las filas resultantes de la consulta
            row = cursor.fetchall()
            obraSubastada = ObrasSubastadasVO()
            IdObra,Titulo,Descripcion,Fecha,Imagen,IdArtista,IdExposicion,PrecioSalida,PrecioVenta,MejorPostor= row
            obraSubastada.setIdObra(IdObra)
            obraSubastada.setTitulo(Titulo)
            obraSubastada.setDescripcion(Descripcion)
            obraSubastada.setFecha(Fecha)
            obraSubastada.setImagen(Imagen)
            obraSubastada.setIdArtista(IdArtista)
            obraSubastada.setIdExposicion(IdExposicion)
            obraSubastada.setMejorPostor(MejorPostor)
            obraSubastada.setPrecioSalida(PrecioSalida)
            obraSubastada.setPrecioVenta(PrecioVenta)
        except Error as e:
            print("Error al seleccionar obraSubastada:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return obraSubastada
    
    #se hace el proximo dia
    def insertObraSubastada (self, obraSub: ObrasSubastadasVO) -> int:
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

            obra=ObrasVO(IDObra=obraSub.getIdObra(),Titulo=obraSub.getTitulo(),Descripcion=obraSub.getDescripcion(),Fecha=obraSub.getFecha(), Imagen=obraSub.getImagen(), IdArtista=obraSub.getIdArtista(), IdExposiciones=obraSub.getIdExposiciones())
            obra_dao=ObraDAO()
            obra_dao.insertObra(obra)
            cursor.execute(self.SQL_SELECT_ID, (obra.getIdObra(),))
            identificador_id = cursor.fetchone()[0] 
            cursor.execute(self.SQL_INSERT, (identificador_id,obraSub.get_PrecioSalida(),obraSub.get_PrecioVenta(),obraSub.get_MejorPostor()))
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

    def deleteObraSubastada (self, id) -> int:
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
            print("Error al eliminar obra:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def updateObraSubastada(self, obraSubastada:ObrasSubastadasVO) -> int:
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


            cursor.execute(self.SQL_UPDATE, (obra.getIDObra(),obra.getPrecioSalida(),obra.getPrecioVenta(),obra.getMejorPostor()))
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
