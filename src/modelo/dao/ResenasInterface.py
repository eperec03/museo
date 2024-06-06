from typing import List
from abc import ABC, abstractmethod
import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')
from vo.ResenasVO import ResenasVO

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class ResenasInterface(ABC):
    @abstractmethod
    def getResenas(self) -> List[ResenasVO]:
        """
        Recupera todas las Resena de la base de datos.        
        Devuelve: List[ResenasVO]: Una lista de objetoss ResenasVO.
        """
        raise NotImplementedError("Método getResenas no implementado")
    
    @abstractmethod
    def getResena(self,id) ->ResenasVO:
        """
        Recupera la Resena de la base de datos cuyo identificador es id.        
        Devuelve: objeto ResenasVO.
        """
        raise NotImplementedError("Método getResena no implementado")
    
    @abstractmethod
    def insertResena(self, Resena: ResenasVO):
        """
        Ineserta un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto ResenasVO a inesertar.
        Devuelve: int: 1 si fue exitoso
        """
        raise NotImplementedError("Método inesertResena no implementado")
    
    @abstractmethod
    def deleteResena(self, Resena: ResenasVO):
        """
        Elimina un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto ResenasVO para borrar.
        """
        raise NotImplementedError("Método deleteResena no implementado")

    @abstractmethod
    def updateResena(self, Resena: ResenasVO):
        """
        Actualiza el usuario que tenga el mismo dni que el que se le pasa en la base de datos.
        Parametros requeridos: El objeto ResenasVO a actualizar.
        """
        raise NotImplementedError("Método updateResena no implementado")