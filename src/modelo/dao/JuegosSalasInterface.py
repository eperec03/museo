from typing import List
from abc import ABC, abstractmethod
import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')
from vo.JuegosSalasVO import JuegosSalasVO

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class JuegosSalasInterface(ABC):
    @abstractmethod
    def getJuegosSalas(self) -> List[JuegosSalasVO]:
        """
        Recupera todas las JuegosSalas de la base de datos.        
        Devuelve: List[JuegosSalasVO]: Una lista de objetos JuegosSalasVO.
        """
        raise NotImplementedError("Método getJuegosSalas no implementado")
    
    @abstractmethod
    def getJuegosSalas(self,id) ->JuegosSalasVO:
        """
        Recupera la JuegosSalas de la base de datos cuyo identificador es id.        
        Devuelve: objeto JuegosSalasVO.
        """
        raise NotImplementedError("Método getJuegosSalas no implementado")
    
    @abstractmethod
    def inesertJuegosSalas(self, JuegosSalas: JuegosSalasVO):
        """
        Ineserta un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto JuegosSalasVO a inesertar.
        Devuelve: int: 1 si fue exitoso
        """
        raise NotImplementedError("Método inesertJuegosSalas no implementado")
    
    @abstractmethod
    def deleteJuegosSalas(self, JuegosSalas: JuegosSalasVO):
        """
        Elimina un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto JuegosSalasVO para borrar.
        """
        raise NotImplementedError("Método deleteJuegosSalas no implementado")

    @abstractmethod
    def updateJuegosSalas(self, JuegosSalas: JuegosSalasVO):
        """
        Actualiza el usuario que tenga el mismo dni que el que se le pasa en la base de datos.
        Parametros requeridos: El objeto JuegosSalasVO a actualizar.
        """
        raise NotImplementedError("Método updateJuegosSalas no implementado")