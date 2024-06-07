from typing import List
from abc import ABC, abstractmethod
import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')
from vo.SalasVO import *

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class SalasInterface(ABC):
    @abstractmethod
    def getSalas(self) -> List[SalasVO]:
        """
        Recupera todas las Sala de la base de datos.        
        Devuelve: List[SalasVO]: Una lista de objetoss SalasVO.
        """
        raise NotImplementedError("Método getSalas no implementado")
    
    @abstractmethod
    def getSala(self,id) ->SalasVO:
        """
        Recupera la Sala de la base de datos cuyo identificador es id.        
        Devuelve: objeto SalasVO.
        """
        raise NotImplementedError("Método getSala no implementado")
    
    @abstractmethod
    def insertSala(self, Sala: SalasVO):
        """
        Ineserta un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto SalasVO a inesertar.
        Devuelve: int: 1 si fue exitoso
        """
        raise NotImplementedError("Método inesertSala no implementado")
    
    # @abstractmethod
    # def deleteSala(self, Sala: SalasVO):
    #     """
    #     Elimina un nuevo usuario en la base de datos.
    #     Parametros requeridos: El objeto SalasVO para borrar.
    #     """
    #     raise NotImplementedError("Método deleteSala no implementado")

    @abstractmethod
    def updateSala(self, Sala: SalasVO):
        """
        Actualiza el usuario que tenga el mismo dni que el que se le pasa en la base de datos.
        Parametros requeridos: El objeto SalasVO a actualizar.
        """
        raise NotImplementedError("Método updateSala no implementado")