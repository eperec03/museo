from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src\modelo')

from vo.ObrasVO import * 
from dao.ObrasDAO import ObrasDao
from conexion.conexion2JDBC import Conexion
from dao.ObrasSubastadasInterface import ObrasSubastadasInterface

# Creamos la clase UsuarioDAO que manejará las operaciones de acceso a datos para los usuarios

class ObrasSubastadasDao(ObrasSubastadasInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT * FROM ObrasSubastadas"
    SQL_INSERT = "INSERT INTO ObrasSubastadas (IDObrassubastadas, PrecioSalida, PrecioVenta, MejorPostor) VALUES (?, ?, ?, ?)"
    SQL_UPDATE = "UPDATE ObrasSubastadas SET PrecioSalida= ?, PrecioVenta= ?, MejorPostor = ? WHERE Titulo = ?"
    SQL_FILTER = "SELECT * FROM ObrasSubastadas WHERE IDObrassubastadas = ?"
    SQL_FILTER_OBR = "SELECT * FROM obras WHERE Titulo = ?"
    SQL_SELECT_OBR = "SELECT IDObra FROM obras WHERE Titulo = ?"


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
                obraSubastada.set_IDObrasubastada(IdObra)
                obraSubastada.setTitulo(Titulo)
                obraSubastada.setDescripcion(Descripcion)
                obraSubastada.setFecha(Fecha)
                obraSubastada.setImagen(Imagen)
                obraSubastada.setIdArtista(IdArtista)
                obraSubastada.setIdExposicion(IdExposicion)
                obraSubastada.set_MejorPostor(MejorPostor)
                obraSubastada.set_PrecioSalida(PrecioSalida)
                obraSubastada.set_PrecioVenta(PrecioVenta)
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
    
    def getObraSubastada(self,titulo) -> ObrasSubastadasVO:
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
            #Primero, vamos a obtener los atributos de la tabla Obras
            cursor.execute(self.SQL_FILTER_OBR, (titulo,))
            row_obr = cursor.fetchall()
            IdObra,Titulo,Descripcion,Fecha,Imagen,IdArtista,IdExposicion= row_obr[0]
            #Ahora, cogemos los parámetros de la tabla ObrasSubastadas
            cursor.execute(self.SQL_FILTER, (IdObra,)) 
            row_obrsub = cursor.fetchall()
            print(row_obrsub[0])
            IdObraSubastada,PrecioSalida,PrecioVenta,MejorPostor =row_obrsub[0]
            obraSubastada = ObrasSubastadasVO()
            obraSubastada.set_IDObrasubastada(IdObraSubastada)
            obraSubastada.setTitulo(Titulo)
            obraSubastada.setDescripcion(Descripcion)
            obraSubastada.setFecha(Fecha)
            obraSubastada.setImagen(Imagen)
            obraSubastada.setIdArtista(IdArtista)
            obraSubastada.setIdExposicion(IdExposicion)
            obraSubastada.set_MejorPostor(MejorPostor)
            obraSubastada.set_PrecioSalida(PrecioSalida)
            obraSubastada.set_PrecioVenta(PrecioVenta)
            print('Hola')
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
            obra=ObrasVO(IdObra=obraSub.getIdObra(),Titulo=obraSub.getTitulo(),Descripcion=obraSub.getDescripcion(),Fecha=obraSub.getFecha(), Imagen=obraSub.getImagen(), IdArtista=obraSub.getIdArtista(), IdExposicion=obraSub.getIdExposicion())
            obra_dao=ObrasDao()
            obra_dao.insertObra(obra)
            cursor.execute(self.SQL_SELECT_OBR, (obra.getTitulo(),))
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

    def deleteObraSubastada (self, Titulo) -> int:
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
            #la eliminamos del padre-on delete cascade
            obras_dao=ObrasDao()
            obras_dao.deleteObra(Titulo)
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

    def updateObraSubastada(self, obraSub:ObrasSubastadasVO) -> int:
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
            #Tenemos que actualizar el padre:
            obra=ObrasVO(IdObra=obraSub.getIdObra(),Titulo=obraSub.getTitulo(),Descripcion=obraSub.getDescripcion(),Fecha=obraSub.getFecha(), Imagen=obraSub.getImagen(), IdArtista=obraSub.getIdArtista(), IdExposicion=obraSub.getIdExposicion())
            obras_dao=ObrasDao()
            obras_dao.updateObra(obra)
            obras_dao.updateObra()
            cursor.execute(self.SQL_UPDATE, (obraSub.get_PrecioSalida(),obraSub.get_PrecioVenta(),obraSub.get_MejorPostor(),obraSub.getTitulo()))
            conn.commit()
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar obraSubastada:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows
obra_subastada1 = ObrasSubastadasVO()
# Setear valores usando setters
obra_subastada1.setIdObra(1)
obra_subastada1.setTitulo("La Noche Estrellada")
obra_subastada1.setDescripcion("Una pintura famosa de Vincent van Gogh")
obra_subastada1.setFecha("1889-06-01")
obra_subastada1.setImagen("noche_estrellada.jpg")
obra_subastada1.setIdArtista(1)
obra_subastada1.setIdExposicion(2)
obra_subastada1.set_IDObrasubastada(1001)
obra_subastada1.set_PrecioSalida(500000)
obra_subastada1.set_PrecioVenta(650000)
obra_subastada1.set_MejorPostor("John Doe")

# Crear instancia vacía
obra_subastada2 = ObrasSubastadasVO()
# Setear valores usando setters
obra_subastada2.setIdObra(2)
obra_subastada2.setTitulo("Mona Lisa")
obra_subastada2.setDescripcion("Una pintura de Leonardo da Vinci")
obra_subastada2.setFecha("1503-10-01")
obra_subastada2.setImagen("mona_lisa.jpg")
obra_subastada2.setIdArtista(2)
obra_subastada2.setIdExposicion(3)
obra_subastada2.set_IDObrasubastada(1002)
obra_subastada2.set_PrecioSalida(750000)
obra_subastada2.set_PrecioVenta(950000)
obra_subastada2.set_MejorPostor("Jane Smith")

a=ObrasSubastadasDao()
# a.insertObraSubastada(obra_subastada1)
# a.insertObraSubastada(obra_subastada2)
# a.deleteObraSubastada("Mona Lisa")
print(a.getObraSubastada("Mona Lisa").getIdObra())