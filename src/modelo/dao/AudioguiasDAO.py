from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src\modelo')

from vo.AudioguiasVO import AudioguiasVO 
from conexion.conexion2JDBC import Conexion
from dao.AudioguiasInterface import AudioguiasInterface
# Creamos la clase UsuarioDAO que manejará las operaciones de acceso a datos para los usuarios

class AudioguiasDao(AudioguiasInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT * FROM audioguias"
    SQL_INSERT = "INSERT INTO audioguias(IDAudioguiaguia, IDObra, Audio, Duracion) VALUES (?, ?, ?, ?)"
    SQL_DELETE = "DELETE FROM audioguias WHERE IDAudioguiaguia = ?"
    SQL_UPDATE = "UPDATE audioguias SET IDObra= ?, Audio= ?, Duracion = ? WHERE IDAudioguiaguia = ?"
    SQL_FILTER = "SELECT * FROM audioguias WHERE IDAudioguiaguia = ?"


    def getAudioguias(self) -> List[AudioguiasVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        audioguias = []
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
                IDAudioguia,IDObra,Audio,Duracion= row
                audioguia = AudioguiasVO()
                audioguia.setIDAudioguia(IDAudioguia)
                audioguia.setDuracion(Duracion)
                audioguia.setIdObra(IDObra)
                audioguia.setAudio(Audio)
                audioguias.append(audioguia)

        except Error as e:
            print("Error al seleccionar Audioguia:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return audioguias
    
    def getAudioguia(self,id) -> AudioguiasVO:
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
            audioguia = AudioguiasVO()
            IDAudioguia,IDObra,Audio,Duracion= row[0]   #Al filtrar por la clave primaria, solo hay 1 resultado almacenado en la 1º pos
            audioguia.setIDAudioguia(IDAudioguia)
            audioguia.setIdObra(IDObra)
            audioguia.setDuracion(Duracion)
            audioguia.setAudio(Audio)
        except Error as e:
            print("Error al seleccionar Audioguia:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return audioguia
    
    def insertAudioguia (self, audioguia: AudioguiasVO) -> int:
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
            cursor.execute(self.SQL_INSERT, (audioguia.getIDAudioguia(),audioguia.getIdObra(),audioguia.getAudio(),audioguia.getDuracion()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al insertar Audioguia:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def deleteAudioguia (self, id) -> int:
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
            print("Error al eliminar Audioguia:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def updateAudioguia(self, audioguia:AudioguiasVO) -> int:
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
            cursor.execute(self.SQL_UPDATE, (audioguia.getIdObra(),audioguia.getAudio(),audioguia.getDuracion(),audioguia.getIDAudioguia()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar Audioguia:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

# a=AudioguiasDao()
# b=AudioguiasVO()
# b.setIDAudioguia('3')
# b.setIdObra('3')
# b.setDuracion('01:15:00')
# b.setAudio('55')
# print(str(a.getAudioguia('3').Duracion))
# a.updateAudioguia(b)
# print(str(a.getAudioguia('3').Duracion))












