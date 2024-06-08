from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')

from vo.ClienteEstandarVO import  *
from conexion.conexion2JDBC import Conexion
from dao.ClienteEstandarInterface import *

class ClienteEstandarDAO(ClienteEInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT NumEntrada FROM clienteestandar"
    SQL_FILTER = "SELECT * FROM clienteestandar WHERE NumEntrada = ?"
    SQL_INSERT = "INSERT INTO clienteestandar(NumEntrada, PrecioEntrada) VALUES (?, ?)"


    def getEntradas(self) -> List[ClienteEstandarVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        entradas = []
        try:
            if conexion:
                conn = conexion
            else:
                print("La base de datos no esta disponible")

            cursor = conn.cursor()

            cursor.execute(self.SQL_SELECT) 
            rows = cursor.fetchall()
            for row in rows:
                NumEntrada = row
                entrada = ClienteEstandarVO()
                entrada.setNumEntrada(NumEntrada)
                # entrada.setPrecioEntrada(PrecioEntrada)
                entradas.append(entrada)

        except Error as e:
            print("Error al seleccionar clientes estándar:", e)

        finally:
            if cursor:
                cursor.close()
        conexion = self.closeConnection(conn)
        return entradas

    def insertEntrada (self, clienteestandar:ClienteEstandarVO) -> int:
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
            cursor.execute(self.SQL_INSERT, (clienteestandar.getNumEntrada(),clienteestandar.getPrecioEntrada()))
            conn.commit()
            rows = cursor.rowcount

        except Error as e:
            print("Error al insertar usuario:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def getEntrada(self,num) -> ClienteEstandarVO:
        conexion = self.getConnection()
        conn = None
        cursor = None
        entradas = []

        try:
            if conexion:
                conn = conexion
            else:
                print("La base de datos no esta disponible")
            cursor = conn.cursor()
            cursor.execute(self.SQL_FILTER, (num,))
            rows = cursor.fetchall()
            if len(rows)>0:
                NumEntrada, PrecioEntrada = rows[0]
                #Ahora, obtenemos los aributos de la tabla Usuarios:
                entrada = ClienteEstandarVO()
                entrada.setNumEntrada(NumEntrada)
                entrada.setPrecioEntrada(PrecioEntrada)
                entradas.append(entrada)

        except Error as e:
            print("Error al seleccionar usuarios:", e)

        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return entradas







# a = ClienteEstandarDAO()

# print(a.getEntrada(1)[0].getNumEntrada())





