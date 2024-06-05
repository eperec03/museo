from typing import List
from abc import ABC, abstractmethod
import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')
from vo.ObrasVO import ObrasVO

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class ObrasInterface(ABC):
    @abstractmethod
    def getObras(self) -> List[ObrasVO]:
        """
        Recupera todas las Obra de la base de datos.        
        Devuelve: List[ObrasVO]: Una lista de objetos ObrasVO.
        """
        raise NotImplementedError("Método getObras no implementado")
    
    @abstractmethod
    def getObra(self,id) ->ObrasVO:
        """
        Recupera la Obra de la base de datos cuyo identificador es id.        
        Devuelve: objeto ObrasVO.
        """
        raise NotImplementedError("Método getObra no implementado")
    
    @abstractmethod
    def insertObra(self, obra: ObrasVO):
        """
        Inserta un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto ObrasVO a insertar.
        Devuelve: int: 1 si fue exitoso
        """
        raise NotImplementedError("Método insertObra no implementado")
    
    @abstractmethod
    def deleteObra(self, obra: ObrasVO):
        """
        Elimina un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto ObrasVO para borrar.
        """
        raise NotImplementedError("Método deleteObra no implementado")

    @abstractmethod
    def updateObra(self, obra: ObrasVO):
        """
        Actualiza el usuario que tenga el mismo dni que el que se le pasa en la base de datos.
        Parametros requeridos: El objeto ObrasVO a actualizar.
        """
        raise NotImplementedError("Método updateObra no implementado")