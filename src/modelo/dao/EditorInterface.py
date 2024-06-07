from typing import List
from abc import ABC, abstractmethod
import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')
from vo.UsuariosVO import EditorVO

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class EditorInterface(ABC):
    @abstractmethod
    def getUsuarios(self) -> List[EditorVO]:
        """
        Recupera todos los usuarios de la base de datos.        
        Devuelve: List[UserDTO]: Una lista de objetos UserDTO.
        """
        raise NotImplementedError("Método getUsuarios no implementado")
    
    @abstractmethod
    def insertUsuario(self, usuario: EditorVO):
        """
        Inserta un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto EditorVO a insertar.
        Devuelve: int: 1 si fue exitoso
        """
        raise NotImplementedError("Método insertUsuario no implementado")
    
    @abstractmethod
    def eliminateUsuario(self, usuario: EditorVO):
        """
        Elimina un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto EditorVO para borrar.
        """
        raise NotImplementedError("Método eliminateUsuario no implementado")

    @abstractmethod
    def updateUsuario(self, usuario: EditorVO):
        """
        Actualiza el usuario que tenga el mismo dni que el que se le pasa en la base de datos.
        Parametros requeridos: El objeto EditorVO a actualizar.
        """
        raise NotImplementedError("Método updateUsuario no implementado")