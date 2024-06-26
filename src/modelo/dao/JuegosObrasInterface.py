from typing import List
from abc import ABC, abstractmethod
import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')
from vo.JuegosVO import JuegosObrasVO

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class JuegosObrasInterface(ABC):
    @abstractmethod
    def getJuegosObras(self) -> List[JuegosObrasVO]:
        """
        Recupera todas las JuegosObras de la base de datos.        
        Devuelve: List[JuegosObrasVO]: Una lista de objetos JuegosObrasVO.
        """
        raise NotImplementedError("Método getJuegosObras no implementado")
    
    @abstractmethod
    def getJuegosObras(self,id) ->JuegosObrasVO:
        """
        Recupera la JuegosObras de la base de datos cuyo identificador es id.        
        Devuelve: objeto JuegosObrasVO.
        """
        raise NotImplementedError("Método getJuegosObras no implementado")
    
    @abstractmethod
    def insertJuegosObras(self, juegosObras: JuegosObrasVO):
        """
        Ineserta un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto JuegosObrasVO a inesertar.
        Devuelve: int: 1 si fue exitoso
        """
        raise NotImplementedError("Método inesertJuegosObras no implementado")
    
    @abstractmethod
    def deleteJuegosObras(self, juegosObras: JuegosObrasVO):
        """
        Elimina un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto JuegosObrasVO para borrar.
        """
        raise NotImplementedError("Método deleteJuegosObras no implementado")

    @abstractmethod
    def updateJuegosObras(self, juegosObras: JuegosObrasVO):
        """
        Actualiza el usuario que tenga el mismo dni que el que se le pasa en la base de datos.
        Parametros requeridos: El objeto JuegosObrasVO a actualizar.
        """
        raise NotImplementedError("Método updateJuegosObras no implementado")