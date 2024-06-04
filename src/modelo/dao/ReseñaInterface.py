from typing import List
from abc import ABC, abstractmethod
import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')
from vo.ReseñasVO import ReseñasVO

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class ReseñasInterface(ABC):
    @abstractmethod
    def getReseñas(self) -> List[ReseñasVO]:
        """
        Recupera todas las Reseña de la base de datos.        
        Devuelve: List[ReseñasVO]: Una lista de objetoss ReseñasVO.
        """
        raise NotImplementedError("Método getReseñas no implementado")
    
    @abstractmethod
    def getReseña(self,id) ->ReseñasVO:
        """
        Recupera la Reseña de la base de datos cuyo identificador es id.        
        Devuelve: objeto ReseñasVO.
        """
        raise NotImplementedError("Método getReseña no implementado")
    
    @abstractmethod
    def inesertReseña(self, reseña: ReseñasVO):
        """
        Ineserta un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto ReseñasVO a inesertar.
        Devuelve: int: 1 si fue exitoso
        """
        raise NotImplementedError("Método inesertReseña no implementado")
    
    @abstractmethod
    def deleteReseña(self, reseña: ReseñasVO):
        """
        Elimina un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto ReseñasVO para borrar.
        """
        raise NotImplementedError("Método deleteReseña no implementado")

    @abstractmethod
    def updateReseña(self, reseña: ReseñasVO):
        """
        Actualiza el usuario que tenga el mismo dni que el que se le pasa en la base de datos.
        Parametros requeridos: El objeto ReseñasVO a actualizar.
        """
        raise NotImplementedError("Método updateReseña no implementado")