from typing import List
from abc import ABC, abstractmethod
import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')
from vo.ObjetosVO import ObjetosVO

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class ObjetosInterface(ABC):
    @abstractmethod
    def getObjetos(self) -> List[ObjetosVO]:
        """
        Recupera todas las Objeto de la base de datos.        
        Devuelve: List[ObjetosVO]: Una lista de objetos ObjetosVO.
        """
        raise NotImplementedError("Método getObjetos no implementado")
    
    @abstractmethod
    def getObjeto(self,id) ->ObjetosVO:
        """
        Recupera la Objeto de la base de datos cuyo identificador es id.        
        Devuelve: objeto ObjetosVO.
        """
        raise NotImplementedError("Método getObjeto no implementado")
    
    @abstractmethod
    def insertObjeto(self, objeto: ObjetosVO):
        """
        Ineserta un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto ObjetosVO a inesertar.
        Devuelve: int: 1 si fue exitoso
        """
        raise NotImplementedError("Método inesertObjeto no implementado")
    
    @abstractmethod
    def deleteObjeto(self, objeto: ObjetosVO):
        """
        Elimina un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto ObjetosVO para borrar.
        """
        raise NotImplementedError("Método deleteObjeto no implementado")

    @abstractmethod
    def updateObjeto(self, objeto: ObjetosVO):
        """
        Actualiza el usuario que tenga el mismo dni que el que se le pasa en la base de datos.
        Parametros requeridos: El objeto ObjetosVO a actualizar.
        """
        raise NotImplementedError("Método updateObjeto no implementado")