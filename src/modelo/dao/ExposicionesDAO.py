from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src\modelo')

from vo.ExposicionesVO import ExposicionesVO 
from conexion.conexion2JDBC import Conexion
from dao.ExposicionesInterface import ExposicionesInterface
# Creamos la clase UsuarioDAO que manejará las operaciones de acceso a datos para los usuarios

class ExposicionesDao(ExposicionesInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT * FROM exposiciones"
    SQL_INSERT = "INSERT INTO exposiciones(IDExposiciones, Titulo, Imagen, Descripcion, NumSala) VALUES (?, ?, ?, ?, ?)"
    SQL_UPDATE = "UPDATE exposiciones SET  Imagen= ?, Descripcion = ?, NumSala = ? WHERE Titulo = ?"
    SQL_FILTER = "SELECT * FROM exposiciones WHERE Titulo = ?"
    SQL_INSERT_SERV = "INSERT INTO Servicios(Nombre) VALUES (?)"
    SQL_SELECT_SERV = "SELECT IDServicios FROM servicios WHERE Nombre = ?"
    SQL_DELETE_SERV = "DELETE FROM Servicios WHERE IdServicios = ?"

    def getExposiciones(self) -> List[ExposicionesVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        exposiciones = []
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
                IDExposiciones,Titulo,Imagen,Descripcion,NumSala= row
                exposicion = ExposicionesVO()
                exposicion.setIdExposicion(IDExposiciones)
                exposicion.setDescripcion(Descripcion)
                exposicion.setTitulo(Titulo)
                exposicion.setImagen(Imagen)
                exposicion.setNumSala(NumSala)
                exposiciones.append(exposicion)

        except Error as e:
            print("Error al seleccionar exposicion:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return exposiciones
    
    def getExposicion(self,Titulo) -> ExposicionesVO:
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
            cursor.execute(self.SQL_FILTER, (Titulo,)) #Obtiene todas las filas resultantes de la consulta
            #Obtiene todas las filas resultantes de la consulta
            row = cursor.fetchall()
            exposicion = ExposicionesVO()
            IDExposiciones,Titulo,Imagen,Descripcion,NumSala= row[0]   #Al filtrar por la clave primaria, solo hay 1 resultado almacenado en la 1º pos
            exposicion.setIdExposicion(IDExposiciones)
            exposicion.setTitulo(Titulo)
            exposicion.setDescripcion(Descripcion)
            exposicion.setImagen(Imagen)
            exposicion.setNumSala(NumSala)
            
        except Error as e:
            print("Error al seleccionar exposicion:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return exposicion
    
    #se hace el proximo dia
    def insertExposicion (self, exposicion: ExposicionesVO) -> int:
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
            #Antes de insertarse, hay que insertarlo en servicios.
            cursor.execute(self.SQL_INSERT_SERV, (exposicion.getTitulo(),))
            conn.commit()
            #Ahora, cogemos el identificador del servicio que acabamos de crear, y finalmente insertamos la exposicion.
            cursor.execute(self.SQL_SELECT_SERV, (exposicion.getTitulo(),))
            identificador_servicio = cursor.fetchone()[0] 
            cursor.execute(self.SQL_INSERT, (identificador_servicio,exposicion.getTitulo(),exposicion.getImagen(),exposicion.getDescripcion(),exposicion.getNumSala()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al insertar exposicion:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def deleteExposicion (self, Titulo) -> int:
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
            #obtenemos el nombre de la exposicion:
            
            #Lo eliminamos en servicios (on delete cascade)
            cursor.execute(self.SQL_DELETE_SERV, (Titulo,))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al eliminar exposicion:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def updateExposicion(self, exposicion:ExposicionesVO) -> int:
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
            cursor.execute(self.SQL_UPDATE, (exposicion.getImagen(),exposicion.getDescripcion(), exposicion.getNumSala(),exposicion.getTitulo()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar exposicion:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows
# a=ExposicionesDao()
# exposicion1 = ExposicionesVO()
# exposicion1.setIdExposicion(1)
# exposicion1.setTitulo("Impresionismo")
# exposicion1.setImagen("impresionismo.jpg")
# exposicion1.setDescripcion("Una exposición de obras impresionistas")
# exposicion1.setNumSala(101)

# exposicion2 = ExposicionesVO()
# exposicion2.setIdExposicion(2)
# exposicion2.setTitulo("Renacimiento")
# exposicion2.setImagen("renacimiento.jpg")
# exposicion2.setDescripcion("Obras maestras del Renacimiento")
# exposicion2.setNumSala(102)

# exposicion3 = ExposicionesVO()
# exposicion3.setIdExposicion(3)
# exposicion3.setTitulo("Arte Moderno")
# exposicion3.setImagen("arte_moderno.jpg")
# exposicion3.setDescripcion("Exploración del arte moderno")
# exposicion3.setNumSala(103)

# exposicion4 = ExposicionesVO()
# exposicion4.setIdExposicion(4)
# exposicion4.setTitulo("Escultura Antigua")
# exposicion4.setImagen("escultura_antigua.jpg")
# exposicion4.setDescripcion("Colección de esculturas antiguas")
# exposicion4.setNumSala(101)

# exposicion5 = ExposicionesVO()
# exposicion5.setIdExposicion(10)
# exposicion5.setTitulo("Surrealismo")
# exposicion5.setImagen("surrealismo.jpg")
# exposicion5.setDescripcion("Obras a destacadas")
# exposicion5.setNumSala(102)

# print(a.getExposiciones())
# # a.insertExposicion(exposicion1)
# # a.insertExposicion(exposicion2)
# # a.insertExposicion(exposicion3)
# # a.insertExposicion(exposicion4)
# # a.insertExposicion(exposicion5)
# a.updateExposicion(exposicion5)