from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')

from vo.UsuariosVO import UsuarioVO 
from conexion.conexion2JDBC import Conexion
from dao.UsuarioInterface import ClientePInterface

class UsuariosDAO(ClientePInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT DNI, UsuNombreCompleto, UsuTfno, UsuEmail, UsuTitularMP, UsuCvvMP, UsuNumTarjMP, UsuCadMP, UsuContrasenna FROM usuarios"
    SQL_INSERT = "INSERT INTO usuarios(DNI, UsuNombreCompleto, UsuTfno, UsuEmail, UsuTitularMP, UsuNumTarjMP, UsuCvvMP, UsuCadMP, UsuContrasenna) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
    SQL_DELETE = "DELETE FROM Usuarios WHERE DNI = ?"
    SQL_UPDATE = "UPDATE Usuarios SET UsuNombreCompleto = ?, UsuTfno = ?, UsuEmail = ?, UsuTitularMP = ?, UsuNumTarjMP = ?,UsuCvvMP = ?, UsuCadMP = ?, UsuContrasenna = ? WHERE DNI = ?"
    SQL_FILTER = "SELECT * FROM Usuarios WHERE DNI = ?"


    def getUsuarios(self) -> List[UsuarioVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        usuarios = []
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
                DNI, UsuNombreCompleto, UsuTfno, UsuEmail, UsuTitularMP, UsuNumTarjMP, UsuCvvMP, UsuCadMP, UsuContrasenna = row
                #Crea un objeto UsuarioVO para cada fila DNI, NombreCompleto...
                usuario = UsuarioVO()
                usuario.set_DNI(DNI)
                usuario.set_UsuNombreCompleto(UsuNombreCompleto)
                usuario.set_Usutfno(UsuTfno)
                usuario.set_UsuEmail(UsuEmail)
                usuario.set_UsuTitularMP(UsuTitularMP)
                usuario.set_UsuNumTarjMP(UsuNumTarjMP)
                usuario.set_UsuCvvMP(UsuCvvMP)
                usuario.set_UsuCadMP(UsuCadMP)
                usuario.set_UsuContrasenna(UsuContrasenna)
                usuarios.append(usuario)

        except Error as e:
            print("Error al seleccionar usuarios:", e)

        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return usuarios
    
    def getUsuario(self,dni) -> UsuarioVO:
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
            cursor.execute(self.SQL_FILTER, (dni,)) #Obtiene todas las filas resultantes de la consulta
            #Obtiene todas las filas resultantes de la consulta
            rows = cursor.fetchall()
            DNI, UsuNombreCompleto, Usutfno, UsuEmail, UsuTitularMP, UsuNumTarjMP, UsuCvvMP, UsuCadMP, UsuContrasenna = rows[0]
            usuario = UsuarioVO()
            usuario.set_DNI(DNI)
            usuario.set_UsuNombreCompleto(UsuNombreCompleto)
            usuario.set_Usutfno(Usutfno)
            usuario.set_UsuEmail(UsuEmail)
            usuario.set_UsuTitularMP(UsuTitularMP)
            usuario.set_UsuNumTarjMP(UsuNumTarjMP)
            usuario.set_UsuCvvMP(UsuCvvMP)
            usuario.set_UsuCadMP(UsuCadMP)
            usuario.set_UsuContrasenna(UsuContrasenna)
        except Error as e:
            print("Error al seleccionar usuarios:", e)

        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return usuario
    #se hace el proximo dia
    def insertUsuario (self, usuario: UsuarioVO) -> int:
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
            cursor.execute(self.SQL_INSERT, (usuario.get_DNI(),usuario.get_UsuNombreCompleto(),usuario.get_Usutfno(),usuario.get_UsuEmail(),usuario.get_UsuTitularMP(),usuario.get_UsuNumTarjMP(),usuario.get_UsuCvvMP(),usuario.get_UsuCadMP(),usuario.get_UsuContrasenna()))
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

    def eliminateUsuario (self, dni) -> int:
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
            cursor.execute(self.SQL_DELETE, (dni,))
            conn.commit()
            #Asegurarse de que esos cambios se hagan permanentes: conn.commit(). Si conn.autocommit = True no es necesario llamar explícitamente a conn.commit() después de cada inserción, ya que la base de datos confirma automáticamente cada instrucción.
           
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount
        except Error as e:
            print("Error al eliminar usuario:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def updateUsuario  (self, usuario:UsuarioVO) -> int:
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
            cursor.execute(self.SQL_UPDATE, (usuario.get_UsuNombreCompleto(),usuario.get_Usutfno(),usuario.get_UsuEmail(),usuario.get_UsuTitularMP(),usuario.get_UsuNumTarjMP(),usuario.get_UsuCvvMP(),usuario.get_UsuCadMP(),usuario.get_UsuContrasenna(), usuario.get_DNI()))
            conn.commit()
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


# usuario_ejemplo=UsuarioVO()
# usuario_ejemplo.set_DNI("12345678A")
# usuario_ejemplo.set_UsuNombreCompleto("Juan Pérez")
# usuario_ejemplo.set_Usutfno("900123456")
# usuario_ejemplo.set_UsuEmail("juan.perez@example.com")
# usuario_ejemplo.set_UsuTitularMP("Juan Pérez")
# usuario_ejemplo.set_UsuNumTarjMP("1234567812345678")
# usuario_ejemplo.set_UsuCvvMP("123")
# usuario_ejemplo.set_UsuCadMP("2026-12-25")
# usuario_ejemplo.set_UsuContrasenna("PepeJuan558866")
# usuario_ejemplo.set_UsuFecha("2024-06-07")

# b=UsuariosDAO()
# b.insertUsuario(usuario_ejemplo)
# # b.eliminateUsuario('12345678A')

# usuario_ejemplo1=UsuarioVO()
# usuario_ejemplo1.set_DNI("12345678A")
# usuario_ejemplo1.set_UsuNombreCompleto("ERi Pérez")
# usuario_ejemplo1.set_Usutfno("601157070")
# usuario_ejemplo1.set_UsuEmail("eri.perez@example.com")
# usuario_ejemplo1.set_UsuTitularMP("Eri Pérez")
# usuario_ejemplo1.set_UsuNumTarjMP("1234567812345678")
# usuario_ejemplo1.set_UsuCvvMP("123")
# usuario_ejemplo1.set_UsuCadMP("2026-12-25")
# usuario_ejemplo1.set_UsuContrasenna("PepeJuan558866")
# usuario_ejemplo1.set_UsuFecha("2024-06-07")
# b.updateUsuario(usuario_ejemplo1)





