from typing import List
from abc import ABC, abstractmethod
import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')
from vo.ObrasSubastadasVO import ObrasSubastadasVO

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class ObrasInterface(ABC):
    @abstractmethod
    def getObrasSubastadas(self) -> List[ObrasSubastadasVO]:
        """
        Recupera todas las Obra de la base de datos.        
        Devuelve: List[ObrasSubastadasVO]: Una lista de objetos ObrasSubastadasVO.
        """
        raise NotImplementedError("Método getObrasSubatadas no implementado")
    
    @abstractmethod
    def getObraSubastada(self,id) ->ObrasSubastadasVO:
        """
        Recupera la Obra de la base de datos cuyo identificador es id.        
        Devuelve: objeto ObrasSubastadasVO.
        """
        raise NotImplementedError("Método getObraSubatada no implementado")
    
    @abstractmethod
    def insertObraSubastada(self, obraSub: ObrasSubastadasVO):
        """
        Inserta un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto ObrasSubastadasVO a insertar.
        Devuelve: int: 1 si fue exitoso
        """
        raise NotImplementedError("Método insertObraSubastada no implementado")
    
    @abstractmethod
    def deleteObraSubastada(self, obraSub: ObrasSubastadasVO):
        """
        Elimina un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto ObrasSubastadasVO para borrar.
        """
        raise NotImplementedError("Método deleteObraSubastada no implementado")

    @abstractmethod
    def updateObraSubastada(self, obraSub: ObrasSubastadasVO):
        """
        Actualiza el usuario que tenga el mismo dni que el que se le pasa en la base de datos.
        Parametros requeridos: El objeto ObrasSubastadasVO a actualizar.
        """
        raise NotImplementedError("Método updateObraSubastada no implementado")