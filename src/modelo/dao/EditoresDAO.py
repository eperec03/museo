from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')

from vo.UsuariosVO import * 
from dao.UsuarioDAO import *
from conexion.conexion2JDBC import Conexion
from modelo.dao.EditorInterface import EditorInterface
# Creamos la clase UsuarioDAO que manejará las operaciones de acceso a datos para los usuarios

class EditorDAO(EditorInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT *  FROM editores"
    SQL_INSERT = "INSERT INTO editores(SSN, Rol) VALUES (?, ?)"
    SQL_UPDATE = "UPDATE editores SET Rol = ?  WHERE SSN = ?"
    SQL_FILTER = "SELECT * FROM editores WHERE SSN = ?"
    SQL_DELETE_USU = "DELETE FROM Usuarios WHERE DNI = ?"


    def getUsuarios(self) -> List[EditorVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        editores = []
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
                SSN, rol = row
                #Ahora, obtenemos los aributos de la tabla Usuarios:
                usu_dao=UsuariosDAO()
                usu_vo=usu_dao.getUsuario(SSN)
                editor = EditorVO()
                editor.set_DNI(SSN)
                editor.set_UsuNombreCompleto(usu_vo.get_UsuNombreCompleto())
                editor.set_Usutfno(usu_vo.get_Usutfno())
                editor.set_UsuEmail(usu_vo.get_UsuEmail())
                editor.set_UsuTitularMP(usu_vo.get_UsuTitularMP())
                editor.set_UsuNumTarjMP(usu_vo.get_UsuNumTarjMP())
                editor.set_UsuCvvMP(usu_vo.get_UsuCvvMP())
                editor.set_UsuCadMP(usu_vo.get_UsuCadMP())
                editor.set_UsuContrasenna(usu_vo.get_UsuContrasenna())
                editor.set_Rol(rol)
                editores.append(editor)

        except Error as e:
            print("Error al seleccionar usuarios:", e)

        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return editores
    
    def getFiltroUsuarios(self,dni) -> List[EditorVO]:
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
            cursor.execute(self.SQL_FILTER, (dni,)) 
            rows = cursor.fetchall()
            SSN, rol = rows[0]
            #Ahora, cogemos el resto de atributos de la tabla usuarios:
            usu_dao=UsuariosDAO()
            usu_vo=usu_dao.getUsuario(SSN)
            editor = EditorVO()
            editor.set_DNI(SSN)
            editor.set_UsuNombreCompleto(usu_vo.get_UsuNombreCompleto())
            editor.set_Usutfno(usu_vo.get_Usutfno())
            editor.set_UsuEmail(usu_vo.get_UsuEmail())
            editor.set_UsuTitularMP(usu_vo.get_UsuTitularMP())
            editor.set_UsuNumTarjMP(usu_vo.get_UsuNumTarjMP())
            editor.set_UsuCvvMP(usu_vo.get_UsuCvvMP())
            editor.set_UsuCadMP(usu_vo.get_UsuCadMP())
            editor.set_UsuContrasenna(usu_vo.get_UsuContrasenna())
            editor.set_Rol(rol)
        except Error as e:
            print("Error al seleccionar usuarios:", e)

        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return editor
    
    def insertUsuario (self, usuario: EditorVO) -> int:
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
            #Primero, insertamos en usuarios:
            usu_vo=UsuarioVO()
            usu_vo.set_DNI(usuario.get_DNI())
            usu_vo.set_UsuNombreCompleto(usuario.get_UsuNombreCompleto())
            usu_vo.set_Usutfno(usuario.get_Usutfno())
            usu_vo.set_UsuEmail(usuario.get_UsuEmail())
            usu_vo.set_UsuTitularMP(usuario.get_UsuTitularMP())
            usu_vo.set_UsuNumTarjMP(usuario.get_UsuNumTarjMP())
            usu_vo.set_UsuCvvMP(usuario.get_UsuCvvMP())
            usu_vo.set_UsuCadMP(usuario.get_UsuCadMP())
            usu_vo.set_UsuContrasenna(usuario.get_UsuContrasenna())
            usu_dao=UsuariosDAO()
            usu_dao.insertUsuario(usu_vo)
            #Ahora, ya podemos meter nuestros datos en Editor
            cursor.execute(self.SQL_INSERT, (usuario.get_DNI(),usuario.get_Rol()))
            conn.commit()
            rows = cursor.rowcount
        except Error as e:
            print("Error al insertar usuario:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def eliminateUsuario (self,SSN) -> int:
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
            #eliminamos de usuario (on delete cascade)
            cursor.execute(self.SQL_DELETE_USU, (SSN,))
            conn.commit()
           
            rows = cursor.rowcount
        except Error as e:
            print("Error al eliminar usuario:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def updateUsuario  (self, usuario:EditorVO) -> int:
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
            #actualizamos los atributos de Usuario, y despues los de Editores
            usu_vo=UsuarioVO()
            usu_vo.set_DNI(usuario.get_DNI())
            usu_vo.set_UsuNombreCompleto(usuario.get_UsuNombreCompleto())
            usu_vo.set_Usutfno(usuario.get_Usutfno())
            usu_vo.set_UsuEmail(usuario.get_UsuEmail())
            usu_vo.set_UsuTitularMP(usuario.get_UsuTitularMP())
            usu_vo.set_UsuNumTarjMP(usuario.get_UsuNumTarjMP())
            usu_vo.set_UsuCvvMP(usuario.get_UsuCvvMP())
            usu_vo.set_UsuCadMP(usuario.get_UsuCadMP())
            usu_vo.set_UsuContrasenna(usuario.get_UsuContrasenna())
            usu_dao=UsuariosDAO()
            usu_dao.updateUsuario(usu_vo)
            #Ahra, actualizamos Editores
            cursor.execute(self.SQL_UPDATE, (usuario.get_Rol(),usuario.get_DNI()))
            conn.commit()

            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar usuario:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

# editor1 = EditorVO()
# editor1.set_DNI("123456789")
# editor1.set_UsuNombreCompleto("Carlos Perez")
# editor1.set_Usutfno("555-1234")
# editor1.set_UsuEmail("carlos.perez@example.com")
# editor1.set_UsuTitularMP("Carlos Perez")
# editor1.set_UsuNumTarjMP("4111111111111111")
# editor1.set_UsuCvvMP("123")
# editor1.set_UsuCadMP("2025-12-25")
# editor1.set_UsuContrasenna("password123")
# editor1.set_Rol("Editor de Contenido")

# editor2 = EditorVO()
# editor2.set_DNI("987654321")
# editor2.set_UsuNombreCompleto("Ana Gomez")
# editor2.set_Usutfno("555-5678")
# editor2.set_UsuEmail("ana.gomez@example.com")
# editor2.set_UsuTitularMP("Ana Gomez")
# editor2.set_UsuNumTarjMP("4222222222222222")
# editor2.set_UsuCvvMP("456")
# editor2.set_UsuCadMP("2011-11-24")
# editor2.set_UsuContrasenna("securepass456")
# editor2.set_UsuFecha("2023-02-15")
# editor2.set_Rol("Editor de Imágenes")

# editor3 = EditorVO()
# editor3.set_DNI("192837465")
# editor3.set_UsuNombreCompleto("Juan Martinez")
# editor3.set_Usutfno("555-9876")
# editor3.set_UsuEmail("juan.martinez@example.com")
# editor3.set_UsuTitularMP("Juan Martinez")
# editor3.set_UsuNumTarjMP("4333333333333333")
# editor3.set_UsuCvvMP("789")
# editor3.set_UsuCadMP("2009-10-23")
# editor3.set_UsuContrasenna("mypassword789")
# editor3.set_UsuFecha("2023-03-10")
# editor3.set_Rol("Editor de Video")

# editor4 = EditorVO()
# editor4.set_DNI("564738291")
# editor4.set_UsuNombreCompleto("Lucia Fernandez")
# editor4.set_Usutfno("555-4321")
# editor4.set_UsuEmail("lucia.fernandez@example.com")
# editor4.set_UsuTitularMP("Lucia Fernandez")
# editor4.set_UsuNumTarjMP("4444444444444444")
# editor4.set_UsuCvvMP("012")
# editor4.set_UsuCadMP("2028-09-26")
# editor4.set_UsuContrasenna("password012")
# editor4.set_UsuFecha("2023-04-05")
# editor4.set_Rol("Editor de Texto")

# editor5 = EditorVO()
# editor5.set_DNI("102938475")
# editor5.set_UsuNombreCompleto("Eri Lopez")
# editor5.set_Usutfno("555-6789")
# editor5.set_UsuEmail("miguel.lopez@example.com")
# editor5.set_UsuTitularMP("Miguel Lopez")
# editor5.set_UsuNumTarjMP("4555555555555555")
# editor5.set_UsuCvvMP("345")
# editor5.set_UsuCadMP("2022-08-22")
# editor5.set_UsuContrasenna("mypassword345")
# editor5.set_UsuFecha("2023-05-20")
# editor5.set_Rol("Editor General")

# a=EditorDAO()
# # a.insertUsuario(editor1)
# # a.insertUsuario(editor2)
# # a.insertUsuario(editor3)
# # a.insertUsuario(editor4)
# # a.insertUsuario(editor5)
# # a.eliminateUsuario("123456789")
# # print(a.getUsuarios())
# # print(a.getFiltroUsuarios('987654321'))
# a.updateUsuario(editor5)












