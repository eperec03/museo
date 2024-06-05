from typing import List
from abc import ABC, abstractmethod
import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')
from vo.ArtistasVO import ArtistasVO

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class ArtistasInterface(ABC):
    @abstractmethod
    def getArtistas(self) -> List[ArtistasVO]:
        """
        Recupera todas las Artista de la base de datos.        
        Devuelve: List[ArtistasVO]: Una lista de objetos ArtistasVO.
        """
        raise NotImplementedError("Método getArtistas no implementado")
    
    @abstractmethod
    def getArtista(self,id) ->ArtistasVO:
        """
        Recupera la Artista de la base de datos cuyo identificador es id.        
        Devuelve: objeto ArtistasVO.
        """
        raise NotImplementedError("Método getArtista no implementado")
    
    @abstractmethod
    def insertArtista(self, artista: ArtistasVO):
        """
        Inserta un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto ArtistasVO a insertar.
        Devuelve: int: 1 si fue exitoso
        """
        raise NotImplementedError("Método insertArtista no implementado")
    
    @abstractmethod
    def deleteArtista(self, artista: ArtistasVO):
        """
        Elimina un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto ArtistasVO para borrar.
        """
        raise NotImplementedError("Método deleteArtista no implementado")

    @abstractmethod
    def updateArtista(self, artista: ArtistasVO):
        """
        Actualiza el usuario que tenga el mismo dni que el que se le pasa en la base de datos.
        Parametros requeridos: El objeto ArtistasVO a actualizar.
        """
        raise NotImplementedError("Método updateArtista no implementado")