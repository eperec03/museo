from typing import List
from abc import ABC, abstractmethod
import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')
from vo.ExposicionesVO import ExposicionesVO

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class ExposicionesInterface(ABC):
    @abstractmethod
    def getExposiciones(self) -> List[ExposicionesVO]:
        """
        Recupera todas las Exposicion de la base de datos.        
        Devuelve: List[ExposicionesVO]: Una lista de objetos ExposicionesVO.
        """
        raise NotImplementedError("Método getExposiciones no implementado")
    
    @abstractmethod
    def getExposicion(self,id) ->ExposicionesVO:
        """
        Recupera la Exposicion de la base de datos cuyo identificador es id.        
        Devuelve: objeto ExposicionesVO.
        """
        raise NotImplementedError("Método getExposicion no implementado")
    
    @abstractmethod
    def inesertExposicion(self, exposicion: ExposicionesVO):
        """
        Ineserta un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto ExposicionesVO a inesertar.
        Devuelve: int: 1 si fue exitoso
        """
        raise NotImplementedError("Método inesertExposicion no implementado")
    
    @abstractmethod
    def deleteExposicion(self, exposicion: ExposicionesVO):
        """
        Elimina un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto ExposicionesVO para borrar.
        """
        raise NotImplementedError("Método deleteExposicion no implementado")

    @abstractmethod
    def updateExposicion(self, exposicion: ExposicionesVO):
        """
        Actualiza el usuario que tenga el mismo dni que el que se le pasa en la base de datos.
        Parametros requeridos: El objeto ExposicionesVO a actualizar.
        """
        raise NotImplementedError("Método updateExposicion no implementado")