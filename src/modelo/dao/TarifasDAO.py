from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src\modelo')

from vo.TarifasVO import TarifasVO
from conexion.conexion2JDBC import Conexion
from dao.TarifasInterface import TarifasInterface
# Creamos la clase UsuarioDAO que manejará las operaciones de acceso a datos para los usuarios

class TarifasDao(TarifasInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT * FROM tarifas"
    SQL_INSERT = "INSERT INTO tarifas(TipoTarifa,Precio,Duracion) VALUES (?, ?, ?)"
    SQL_DELETE = "DELETE FROM tarifas WHERE TipoTarifa = ?"
    SQL_UPDATE = "UPDATE tarifas SET Precio= ?, Duracion = ? WHERE TipoTarifa = ?"
    SQL_FILTER = "SELECT * FROM tarifas WHERE TipoTarifa = ?"


    def getTarifas(self) -> List[TarifasVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        tarifas = []
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
                id,at1,at2= row
                tarifa = TarifasVO()
                tarifa.setTipoTarifa(id)
                tarifa.setPrecio(at1)
                tarifa.setDuracion(at2)
                tarifas.append(tarifa)

        except Error as e:
            print("Error al seleccionar Tarifa:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return tarifas
    
    def getTarifa(self,id) -> TarifasVO:
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
            Tarifa = TarifasVO()
            id,at1,at2= row[0]   #Al filtrar por la clave primaria, solo hay 1 resultado almacenado en la 1º pos
            Tarifa.setTipoTarifa(id)
            Tarifa.setPrecio(at1)
            Tarifa.setDuracion(at2)
        except Error as e:
            print("Error al seleccionar Tarifa:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return Tarifa
    
    #se hace el proximo dia
    def insertTarifa (self, Tarifa: TarifasVO) -> int:
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
            cursor.execute(self.SQL_INSERT, (Tarifa.getTipoTarifa(),Tarifa.getPrecio(),Tarifa.getDuracion()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al insertar Tarifa:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def deleteTarifa (self, id) -> int:
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
            print("Error al eliminar Tarifa:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def updateTarifa(self, Tarifa:TarifasVO) -> int:
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
            cursor.execute(self.SQL_UPDATE, (Tarifa.getPrecio(),Tarifa.getDuracion(),Tarifa.getTipoTarifa()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar Tarifa:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

# a=TarifasDao()
# b=TarifasVO()
# b.setTipoTarifa('Exclusiva')
# b.setDuracion('10 horas')
# b.setPrecio(150.00)
# a.insertTarifa(b)
# print(str(a.getTarifas()[0].Precio))
# print(str(a.getTarifa('Exclusiva').Precio))
# c=TarifasVO()
# c.setTipoTarifa('Exclusiva')
# c.setDuracion('152 horas')
# c.setPrecio(8000.50)
# a.updateTarifa(c)













