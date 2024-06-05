from typing import List
from abc import ABC, abstractmethod
import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')
from vo.SubastasVO import SubastasVO

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class SubastasInterface(ABC):
    @abstractmethod
    def getSubastas(self) -> List[SubastasVO]:
        """
        Recupera todas las Subasta de la base de datos.        
        Devuelve: List[SubastasVO]: Una lista de objetos SubastasVO.
        """
        raise NotImplementedError("Método getSubastas no implementado")
    
    @abstractmethod
    def getSubasta(self,id) ->SubastasVO:
        """
        Recupera la Subasta de la base de datos cuyo identificador es id.        
        Devuelve: objeto SubastasVO.
        """
        raise NotImplementedError("Método getSubasta no implementado")
    
    @abstractmethod
    def inesertSubasta(self, subasta: SubastasVO):
        """
        Ineserta un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto SubastasVO a inesertar.
        Devuelve: int: 1 si fue exitoso
        """
        raise NotImplementedError("Método inesertSubasta no implementado")
    
    @abstractmethod
    def deleteSubasta(self, subasta: SubastasVO):
        """
        Elimina un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto SubastasVO para borrar.
        """
        raise NotImplementedError("Método deleteSubasta no implementado")

    @abstractmethod
    def updateSubasta(self, subasta: SubastasVO):
        """
        Actualiza el usuario que tenga el mismo dni que el que se le pasa en la base de datos.
        Parametros requeridos: El objeto SubastasVO a actualizar.
        """
        raise NotImplementedError("Método updateSubasta no implementado")