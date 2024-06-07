from typing import List
from abc import ABC, abstractmethod
import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')
from vo.JuegosVO import JuegosVO

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class JuegosInterface(ABC):
    @abstractmethod
    def getJuegos(self) -> List[JuegosVO]:
        """
        Recupera todas las Juego de la base de datos.        
        Devuelve: List[JuegosVO]: Una lista de objetos JuegosVO.
        """
        raise NotImplementedError("Método getJuegos no implementado")
    
    @abstractmethod
    def getJuego(self,id) ->JuegosVO:
        """
        Recupera la Juego de la base de datos cuyo identificador es id.        
        Devuelve: objeto JuegosVO.
        """
        raise NotImplementedError("Método getJuego no implementado")
    
    @abstractmethod
    def insertJuego(self, juego: JuegosVO):
        """
        Ineserta un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto JuegosVO a inesertar.
        Devuelve: int: 1 si fue exitoso
        """
        raise NotImplementedError("Método inesertJuego no implementado")
    
    @abstractmethod
    def deleteJuego(self, juego: JuegosVO):
        """
        Elimina un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto JuegosVO para borrar.
        """
        raise NotImplementedError("Método deleteJuego no implementado")

    @abstractmethod
    def updateJuego(self, juego: JuegosVO):
        """
        Actualiza el usuario que tenga el mismo dni que el que se le pasa en la base de datos.
        Parametros requeridos: El objeto JuegosVO a actualizar.
        """
        raise NotImplementedError("Método updateJuego no implementado")