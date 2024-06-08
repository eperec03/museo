from typing import List
from abc import ABC, abstractmethod
import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')
from vo.UsuariosVO import ClientePremiumVO

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class ClientePInterface(ABC):
    @abstractmethod
    def getClientesP(self) -> List[ClientePremiumVO]:
        """
        Recupera todos los ClientePs de la base de datos.        
        Devuelve: List[UserDTO]: Una lista de objetos UserDTO.
        """
        raise NotImplementedError("Método getClientePs no implementado")
    
    @abstractmethod
    def insertClienteP(self, ClienteP: ClientePremiumVO):
        """
        Inserta un nuevo ClienteP en la base de datos.
        Parametros requeridos: El objeto ClientePremiumVO a insertar.
        Devuelve: int: 1 si fue exitoso
        """
        raise NotImplementedError("Método insertClienteP no implementado")
    
    @abstractmethod
    def eliminateClienteP(self, ClienteP: ClientePremiumVO):
        """
        Elimina un nuevo ClienteP en la base de datos.
        Parametros requeridos: El objeto ClientePremiumVO para borrar.
        """
        raise NotImplementedError("Método eliminateClienteP no implementado")

    @abstractmethod
    def updateClienteP(self, ClienteP: ClientePremiumVO):
        """
        Actualiza el ClienteP que tenga el mismo dni que el que se le pasa en la base de datos.
        Parametros requeridos: El objeto ClientePremiumVO a actualizar.
        """
        raise NotImplementedError("Método updateClienteP no implementado")