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
    SQL_FILTER = "SELECT * FROM salas WHERE NumSala = ?"
    SQL_SELECT = "SELECT * FROM Salas"
    SQL_UPDATE = 'UPDATE salas SET Capacidad= ?, Tematica = ?, IDMapa= ? WHERE NumSala= ?'
    SQL_INSERT= 'INSERT INTO salas (NumSala, Capacidad, Tematica,IDMapa) VALUES (?,?,?,?)'

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
                Id,capacidad,tematica,idMapa=row
                sala.setNumeroSala(Id)
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

    def getSala(self,Id) -> SalasVO:
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
            sala = SalasVO()
            sala.setNumeroSala(Id)
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
    def insertSala (self, sala: SalasVO) -> int:
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
            cursor.execute(self.SQL_INSERT, (sala.getNumeroSala(),sala.getCapacidad(),sala.getTematica(),sala.getIdMapa()))
            conn.commit()
            #Asegurarse de que esos cambios se hagan permanentes: conn.commit(). Si conn.autocommit = True no es necesario llamar explícitamente a conn.commit() después de cada inserción, ya que la base de datos confirma automáticamente cada instrucción.
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al insertar usuario:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows


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
            cursor.execute(self.SQL_UPDATE, (Salas.getCapacidad(),Salas.getTematica(),Salas.getIdMapa(), Salas.getNumeroSala()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar Salas:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows
    
a=SalasVO()
a.setIdMapa(1)
a.setCapacidad(59875)
a.setNumeroSala(66)
a.setTematica('El suspenso gordo que nos va a caer')
b=SalasDao()
# b.insertSala(a)
a.setIdMapa(1)
a.setCapacidad(55)
a.setNumeroSala(66)
a.setTematica('El aprobado gordo que nos va a caer :D')
b.updateSala(a)

