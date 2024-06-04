from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src\modelo')

from vo.ObjetosVO import ObjetosVO 
from conexion.conexion2JDBC import Conexion
from dao.ObjetosInterface import ObjetosInterface
# Creamos la clase UsuarioDAO que manejará las operaciones de acceso a datos para los usuarios

class ObjetosDao(ObjetosInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT * FROM objetos"
    SQL_INSERT = "INSERT INTO objetos(IDObjeto, Imagen, Tipo, Precio, Inspiracion, Existencias, Agotado, IDCatalogo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    SQL_DELETE = "DELETE FROM objetos WHERE IDObjeto = ?"
    SQL_UPDATE = "UPDATE objetos SET Imagen= ?, Tipo= ?, Precio = ?, Inspiracion = ?, Existencias = ?, Agotado = ?, IDCatalogo = ? WHERE IDObjeto = ?"
    SQL_FILTER = "SELECT * FROM objetos WHERE IDObjeto = ?"


    def getObjetos(self) -> List[ObjetosVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        objetos = []
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
                IDObjeto,Imagen,Tipo,Precio,Inspiracion,Existencias,Agotado,IDCatalogo= row
                objeto = ObjetosVO()
                objeto.setIDObjeto(IDObjeto)
                objeto.setPrecio(Precio)
                objeto.setImagen(Imagen)
                objeto.setTipo(Tipo)
                objeto.setInspiracion(Inspiracion)
                objeto.setExistencias(Existencias)
                objeto.setAgotado(Agotado)
                objeto.setIDCatalogo(IDCatalogo)
                objetos.append(objeto)

        except Error as e:
            print("Error al seleccionar objeto:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return objetos
    
    def getObjeto(self,id) -> ObjetosVO:
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
            objeto = ObjetosVO()
            IDObjeto,Imagen,Tipo,Precio= row[0]   #Al filtrar por la clave primaria, solo hay 1 resultado almacenado en la 1º pos
            objeto.setIDObjeto(IDObjeto)
            objeto.setImagen(Imagen)
            objeto.setPrecio(Precio)
            objeto.setTipo(Tipo)
        except Error as e:
            print("Error al seleccionar objeto:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return objeto
    
    #se hace el proximo dia
    def insertObjeto (self, objeto: ObjetosVO) -> int:
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
            cursor.execute(self.SQL_INSERT, (objeto.getIDObjeto(),objeto.getImagen(),objeto.getTipo(),objeto.getPrecio(),objeto.getInspiracion(),objeto.getExistencias(),objeto.getAgotado(),objeto.getIDCatalogo()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al insertar objeto:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def deleteObjeto (self, id) -> int:
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
            print("Error al eliminar objeto:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def updateObjeto(self, objeto:ObjetosVO) -> int:
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
            cursor.execute(self.SQL_UPDATE, (objeto.getImagen(),objeto.getTipo(),objeto.getPrecio(),objeto.getIDObjeto(),objeto.getInspiracion(),objeto.getExistencias(),objeto.getAgotado(),objeto.getIDCatalogo()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar objeto:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows
