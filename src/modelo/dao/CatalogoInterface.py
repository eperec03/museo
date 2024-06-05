from typing import List
from abc import ABC, abstractmethod
import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')
from vo.CatalogoVO import CatalogoVO

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class CatalogoInterface(ABC):
    @abstractmethod
    def getCatalogo(self) -> List[CatalogoVO]:
        """
        Recupera todas las Catalogo de la base de datos.        
        Devuelve: List[CatalogoVO]: Una lista de objetos CatalogoVO.
        """
        raise NotImplementedError("Método getCatalogo no implementado")
    
    @abstractmethod
    def getCatalogo(self,id) ->CatalogoVO:
        """
        Recupera la Catalogo de la base de datos cuyo identificador es id.        
        Devuelve: objeto CatalogoVO.
        """
        raise NotImplementedError("Método getCatalogo no implementado")
    
    @abstractmethod
    def inesertCatalogo(self, catalogo: CatalogoVO):
        """
        Ineserta un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto CatalogoVO a inesertar.
        Devuelve: int: 1 si fue exitoso
        """
        raise NotImplementedError("Método inesertCatalogo no implementado")
    
    @abstractmethod
    def deleteCatalogo(self, catalogo: CatalogoVO):
        """
        Elimina un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto CatalogoVO para borrar.
        """
        raise NotImplementedError("Método deleteCatalogo no implementado")

    @abstractmethod
    def updateCatalogo(self, catalogo: CatalogoVO):
        """
        Actualiza el usuario que tenga el mismo dni que el que se le pasa en la base de datos.
        Parametros requeridos: El objeto CatalogoVO a actualizar.
        """
        raise NotImplementedError("Método updateCatalogo no implementado")