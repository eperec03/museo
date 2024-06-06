from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src\modelo')

from vo.ObjetosVO import ObjetosVO 
from conexion.conexion2JDBC import Conexion
from dao.ObjetosInterface import ObjetosInterface

class ObjetosDao(ObjetosInterface, Conexion):
    # Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT * FROM objetos"
    SQL_INSERT = "INSERT INTO objetos(NombreObjeto, Imagen, Precio, Tipo, Inspiracion, Existencias, Agotado, IDCatalogo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    SQL_DELETE = "DELETE FROM objetos WHERE NombreObjeto = ?"
    SQL_UPDATE = "UPDATE objetos SET Imagen = ?, Precio = ?, Tipo = ?, Inspiracion = ?, Existencias = ?, Agotado = ?, IDCatalogo = ? WHERE NombreObjeto = ?"
    SQL_FILTER = "SELECT * FROM objetos WHERE NombreObjeto = ?"

    def getObjetos(self) -> List[ObjetosVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        objetos = []
        try:
            if conexion:
                conn = conexion
            else:
                print("La base de datos no está disponible")
            cursor = conn.cursor()
            cursor.execute(self.SQL_SELECT)  # Obtiene todas las filas resultantes de la consulta
            rows = cursor.fetchall()
            # Itera sobre todas las filas
            for row in rows:
                IDObjeto, NombreObjeto, Imagen, Precio, Tipo, Inspiracion, Existencias, Agotado, IDCatalogo = row
                objeto = ObjetosVO()
                objeto.setIdObjeto(IDObjeto)
                objeto.setNombreObjeto(NombreObjeto)
                objeto.setImagen(Imagen)
                objeto.setPrecio(Precio)
                objeto.setTipo(Tipo)
                objeto.setInspiracion(Inspiracion)
                objeto.setExistencias(Existencias)
                objeto.setAgotado(Agotado)
                objeto.setIdCatalogo(IDCatalogo)
                objetos.append(objeto)
        except Error as e:
            print("Error al seleccionar objetos:", e)
        finally:
            if cursor:
                cursor.close()
        conexion = self.closeConnection(conn)
        return objetos
    
    def getObjeto(self, nombre_objeto) -> ObjetosVO:
        conexion = self.getConnection()
        conn = None
        cursor = None
        try:
            if conexion:
                conn = conexion
            else:
                print("La base de datos no está disponible")
            cursor = conn.cursor()
            cursor.execute(self.SQL_FILTER, (nombre_objeto,))  # Obtiene las filas resultantes de la consulta
            row = cursor.fetchall()
            objeto = ObjetosVO()
            IDObjeto, NombreObjeto, Imagen, Precio, Tipo, Inspiracion, Existencias, Agotado, IDCatalogo = row[0]  # Al filtrar por la clave primaria, solo hay 1 resultado
            objeto.setIdObjeto(IDObjeto)
            objeto.setNombreObjeto(NombreObjeto)
            objeto.setImagen(Imagen)
            objeto.setPrecio(Precio)
            objeto.setTipo(Tipo)
            objeto.setInspiracion(Inspiracion)
            objeto.setExistencias(Existencias)
            objeto.setAgotado(Agotado)
            objeto.setIdCatalogo(IDCatalogo)
        except Error as e:
            print("Error al seleccionar objeto:", e)
        finally:
            if cursor:
                cursor.close()
        conexion = self.closeConnection(conn)
        return objeto
    
    def insertObjeto(self, objeto: ObjetosVO) -> int:
        conexion = self.getConnection()
        conn = None
        cursor = None
        rows = 0
        try:
            if conexion:
                conn = conexion
            else:
                print("La base de datos no está disponible")
            cursor = conn.cursor()
            cursor.execute(self.SQL_INSERT, (objeto.getNombreObjeto(), objeto.getImagen(), objeto.getPrecio(), objeto.getTipo(), objeto.getInspiracion(), objeto.getExistencias(), objeto.getAgotado(), objeto.getIdCatalogo()))
            conn.commit()
            rows = cursor.rowcount
        except Error as e:
            print("Error al insertar objeto:", e)
        finally:
            if cursor:
                cursor.close()
        conexion = self.closeConnection(conn)
        return rows

    def deleteObjeto(self, nombre_objeto) -> int:
        conexion = self.getConnection()
        conn = None
        cursor = None
        rows = 0
        try:
            if conexion:
                conn = conexion
            else:
                print("La base de datos no está disponible")
            cursor = conn.cursor()
            cursor.execute(self.SQL_DELETE, (nombre_objeto,))
            conn.commit()
            rows = cursor.rowcount
        except Error as e:
            print("Error al eliminar objeto:", e)
        finally:
            if cursor:
                cursor.close()
        conexion = self.closeConnection(conn)
        return rows

    def updateObjeto(self, objeto: ObjetosVO) -> int:
        conexion = self.getConnection()
        conn = None
        cursor = None
        rows = 0
        try:
            if conexion:
                conn = conexion
            else:
                print("La base de datos no está disponible")
            cursor = conn.cursor()
            cursor.execute(self.SQL_UPDATE, (objeto.getImagen(), objeto.getPrecio(), objeto.getTipo(), objeto.getInspiracion(), objeto.getExistencias(), objeto.getAgotado(), objeto.getIdCatalogo(), objeto.getNombreObjeto()))
            conn.commit()
            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar objeto:", e)
        finally:
            if cursor:
                cursor.close()
        conexion = self.closeConnection(conn)
        return rows
