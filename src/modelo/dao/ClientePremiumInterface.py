from typing import List
from abc import ABC, abstractmethod
import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')
from vo.ClientePremiumVO import ClientePremiumVO

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class ClientePInterface(ABC):
    @abstractmethod
    def getUsuarios(self) -> List[ClientePremiumVO]:
        """
        Recupera todos los usuarios de la base de datos.        
        Devuelve: List[UserDTO]: Una lista de objetos UserDTO.
        """
        raise NotImplementedError("Método getUsuarios no implementado")
    
    @abstractmethod
    def insertUsuario(self, usuarios: ClientePremiumVO):
        """
        Inserta un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto ClientePremiumVO a insertar.
        Devuelve: int: 1 si fue exitoso
        """
        raise NotImplementedError("Método insertUsuario no implementado")
    
    @abstractmethod
    def eliminateUsuario(self, usuarios: ClientePremiumVO):
        """
        Elimina un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto ClientePremiumVO para borrar.
        """
        raise NotImplementedError("Método eliminateUsuario no implementado")

    @abstractmethod
    def updateUsuario(self, usuarios: ClientePremiumVO):
        """
        Actualiza el usuario que tenga el mismo dni que el que se le pasa en la base de datos.
        Parametros requeridos: El objeto ClientePremiumVO a actualizar.
        """
        raise NotImplementedError("Método updateUsuario no implementado")