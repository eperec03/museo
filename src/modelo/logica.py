import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
from conexion.conexion2JDBC import Conexion
from dao.UserDao import UserDao
from vo.UserVO import UserVO #-- aun no está este script

class Logica:
    def __init__(self, conexion=None):
        self.conexion=conexion

    def obtener_usuarios(self):
        mi_persona_dao=None
        #valida que no inserten emails vacios
        mi_persona_dao = UserDao(self.conexion)
        usuarios = mi_persona_dao.getUsuarios()
        return usuarios

    def registrar_usuario(self):
        usuario = UserVO ("120", "Pedro")
        persona_dao = UserDao(self.conexion)
        usuario.persona_dao.insertUsuario(usuario)
        return (usuario)

conexion= Conexion.getConnection()
l=Logica(conexion)