from jaydebeapi import Error
from typing import List

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')

from vo.UsuariosVO import * 
from dao.UsuarioDAO import UsuariosDAO
from conexion.conexion2JDBC import Conexion
from modelo.dao.ClientePremiumInterface import ClientePInterface

class ClientePremiumDAO(ClientePInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT * FROM Clientespremium"
    SQL_INSERT = "INSERT INTO Clientespremium(DNI, ObrasAdquiridas, DineroGastado, Penalizacion, TipoTarifa) VALUES (?, ?, ?, ?, ?)"
    SQL_UPDATE = "UPDATE clientespremium SET  ObrasAdquiridas = ?, DineroGastado = ?, Penalizacion = ?, TipoTarifa = ? WHERE DNI = ?"
    SQL_FILTER = "SELECT * FROM clientespremium WHERE DNI = ?"
    SQL_DELETE_USU = "DELETE FROM Usuarios WHERE DNI = ?"   

    def getClientesP(self) -> List[ClientePremiumVO]:
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
                DNI,ObrasAdquiridas,DineroGastado,Penalizacion,TipoTarifa= row
                #Ahora, obtenemos los aributos de la tabla Usuarios:
                usu_dao=UsuariosDAO()
                usu_vo=usu_dao.getUsuario(DNI)
                clipremium = ClientePremiumVO()
                clipremium.set_DNI(DNI)
                clipremium.set_UsuNombreCompleto(usu_vo.get_UsuNombreCompleto())
                clipremium.set_Usutfno(usu_vo.get_Usutfno())
                clipremium.set_UsuEmail(usu_vo.get_UsuEmail())
                clipremium.set_UsuTitularMP(usu_vo.get_UsuTitularMP())
                clipremium.set_UsuNumTarjMP(usu_vo.get_UsuNumTarjMP())
                clipremium.set_UsuCvvMP(usu_vo.get_UsuCvvMP())
                clipremium.set_UsuCadMP(usu_vo.get_UsuCadMP())
                clipremium.set_UsuContrasenna(usu_vo.get_UsuContrasenna())
                clipremium.set_ObrasAdquiridas(ObrasAdquiridas)
                clipremium.set_DineroGastado(DineroGastado)
                clipremium.set_Penalizacion(Penalizacion)
                clipremium.set_TipoTarifa(TipoTarifa)
                usuarios.append(clipremium)

        except Error as e:
            print("Error al seleccionar usuarios:", e)

        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return usuarios
    
    def getClienteP(self,dni) -> ClientePremiumVO:
        conexion = self.getConnection()
        conn = None
        cursor = None
        clientes = []

        try:
            if conexion:
                conn = conexion
            else:
                print("La base de datos no esta disponible")
            cursor = conn.cursor()
            cursor.execute(self.SQL_FILTER, (dni,))
            rows = cursor.fetchall()
            if len(rows)>0:
                DNI,ObrasAdquiridas,DineroGastado,Penalizacion,TipoTarifa= rows[0]
                #Ahora, obtenemos los aributos de la tabla Usuarios:
                usu_dao=UsuariosDAO()
                usu_vo=usu_dao.getUsuario(DNI)
                clipremium = ClientePremiumVO()
                clipremium.set_DNI(DNI)
                clipremium.set_UsuNombreCompleto(usu_vo.get_UsuNombreCompleto())
                clipremium.set_Usutfno(usu_vo.get_Usutfno())
                clipremium.set_UsuEmail(usu_vo.get_UsuEmail())
                clipremium.set_UsuTitularMP(usu_vo.get_UsuTitularMP())
                clipremium.set_UsuNumTarjMP(usu_vo.get_UsuNumTarjMP())
                clipremium.set_UsuCvvMP(usu_vo.get_UsuCvvMP())
                clipremium.set_UsuCadMP(usu_vo.get_UsuCadMP())
                clipremium.set_UsuContrasenna(usu_vo.get_UsuContrasenna())
                clipremium.set_ObrasAdquiridas(ObrasAdquiridas)
                clipremium.set_DineroGastado(DineroGastado)
                clipremium.set_Penalizacion(Penalizacion)
                clipremium.set_TipoTarifa(TipoTarifa)
                clientes.append(clipremium)
        except Error as e:
            print("Error al seleccionar usuarios:", e)

        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()
        conexion = self.closeConnection(conn)
        return clientes

    def insertClienteP (self, usuario: ClientePremiumVO) -> int:
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
            cursor.execute(self.SQL_INSERT, (usuario.get_DNI(),usuario.get_ObrasAdquiridas(),usuario.get_DineroGastado(),usuario.get_Penalizacion(),usuario.get_TipoTarifa()))
            conn.commit()
            rows = cursor.rowcount
        except Error as e:
            print("Error al insertar usuario:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def eliminateClienteP (self, DNI) -> int:
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
            cursor.execute(self.SQL_DELETE_USU, (DNI,))
            conn.commit()
            rows = cursor.rowcount
        except Error as e:
            print("Error al eliminar usuario:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows

    def updateClienteP  (self, usuario:ClientePremiumVO) -> int:
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
            #Ahra, actualizamos ClientesPremium
            cursor.execute(self.SQL_UPDATE, (usuario.get_ObrasAdquiridas(),usuario.get_DineroGastado(),usuario.get_Penalizacion(),usuario.get_TipoTarifa(),usuario.get_DNI()))
            conn.commit()

            rows = cursor.rowcount
        except Error as e:
            print("Error al actualizar usuario:", e)


        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows


# cliente1 = ClientePremiumVO()

# cliente1.set_DNI("12345678A")
# cliente1.set_UsuNombreCompleto("Juan Pérez")
# cliente1.set_Usutfno("123456789")
# cliente1.set_UsuEmail("juan.perez@example.com")
# cliente1.set_UsuTitularMP("Juan Pérez")
# cliente1.set_UsuNumTarjMP("1234 5678 9012 3456")
# cliente1.set_UsuCvvMP("123")
# cliente1.set_UsuCadMP("2024-12-31")  
# cliente1.set_UsuContrasenna("miContraseñaSegura")
# cliente1.set_UsuFecha("2024-06-01")  
# cliente1.set_ObrasAdquiridas(10)
# cliente1.set_DineroGastado(2500.75)
# cliente1.set_Penalizacion(0)
# cliente1.set_TipoTarifa("Reducida")

# cliente2 = ClientePremiumVO()

# cliente2.set_DNI("87654321B")
# cliente2.set_UsuNombreCompleto("Ana Gómez")
# cliente2.set_Usutfno("987654321")
# cliente2.set_UsuEmail("ana.gomez@example.com")
# cliente2.set_UsuTitularMP("Ana Gómez")
# cliente2.set_UsuNumTarjMP("6543 2109 8765 4321")
# cliente2.set_UsuCvvMP("456")
# cliente2.set_UsuCadMP("2025-06-30")  
# cliente2.set_UsuContrasenna("otraContraseñaSegura")
# cliente2.set_UsuFecha("2024-06-02")  
# cliente2.set_ObrasAdquiridas(15)
# cliente2.set_DineroGastado(3500.50)
# cliente2.set_Penalizacion(1)
# cliente2.set_TipoTarifa("Normal")

a=ClientePremiumDAO()
# a.insertClienteP(cliente2)
# a.eliminateClienteP('12345678A')
print(a.getClientesP())







