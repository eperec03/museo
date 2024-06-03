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
    SQL_INSERT = "INSERT INTO audioguias(DNI, UsuNombreCompleto, UsuTfno, UsuEmail, UsuTitularMP, UsuNumTarjMP, UsuCvvMP, UsuCadMP, UsuContrasenna, UsuFecha) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    SQL_DELETE = "DELETE FROM audioguias WHERE IDAudioguia = ?"
    SQL_UPDATE = "UPDATE audioguias SET Audio= ?, Duracion = ? WHERE IDAudioguia = ?"
    SQL_FILTER = "SELECT * FROM audioguias WHERE IDAudioguia = ?"


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
                IDAudio,IDObra,Audio,Duracion= row
                audioguia = AudioguiasVO()
                audioguia.setIdAudio(IDAudio)
                audioguia.setDuracion(Duracion)
                audioguia.setIdObra(IDObra)
                audioguia.setAudio(Audio)
                audioguias.append(audioguia)

        except Error as e:
            print("Error al seleccionar audioguia:", e)
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
            IDAudio,IDObra,Audio,Duracion= row[0]   #Al filtrar por la clave primaria, solo hay 1 resultado almacenado en la 1º pos
            audioguia.setIdAudio(IDAudio)
            audioguia.setIdObra(IDObra)
            audioguia.setDuracion(Duracion)
            audioguia.setAudio(Audio)
        except Error as e:
            print("Error al seleccionar audioguia:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return audioguia
    
    #se hace el proximo dia
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
            cursor.execute(self.SQL_INSERT, (audioguia.getIdAudio(),audioguia.getIdObra(),audioguia.getDuracion(),audioguia.getAudio()))
            # conn.commit()
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

    def deleteAudioguia (self, audioguia:AudioguiasVO) -> int:
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
            cursor.execute(self.SQL_DELETE, (audioguia.getIdAudio(),))
            #Asegurarse de que esos cambios se hagan permanentes: conn.commit(). Si conn.autocommit = True no es necesario llamar explícitamente a conn.commit() después de cada inserción, ya que la base de datos confirma automáticamente cada instrucción.
            # conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al eliminar usuario:", e)


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
            cursor.execute(self.SQL_UPDATE, (audioguia.getAudio(),audioguia.getDuracion()))
            # conn.commit()
            #Asegurarse de que esos cambios se hagan permanentes: conn.commit(). Si conn.autocommit = True no es necesario llamar explícitamente a conn.commit() después de cada inserción, ya que la base de datos confirma automáticamente cada instrucción.
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar usuario:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

a=AudioguiasDao()
b=AudioguiasVO()
b.setIdAudio('12')
b.setIdObra('1')
b.setAudio('audio')
b.setDuracion('00:50:55')
a.insertAudioguia(b)

#print(str(a.getAudioguia('13').Duracion))









