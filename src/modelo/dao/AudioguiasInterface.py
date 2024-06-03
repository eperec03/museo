from typing import List
from abc import ABC, abstractmethod
import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')
from vo.AudioguiasVO import AudioguiasVO

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class AudioguiasInterface(ABC):
    @abstractmethod
    def getAudioguias(self) -> List[AudioguiasVO]:
        """
        Recupera todas las audioguia de la base de datos.        
        Devuelve: List[AudioguiasVO]: Una lista de objetos AudioguiasVO.
        """
        raise NotImplementedError("Método getAudioguias no implementado")
    
    @abstractmethod
    def getAudioguia(self,id) ->AudioguiasVO:
        """
        Recupera la audioguia de la base de datos cuyo identificador es id.        
        Devuelve: objeto AudioguiasVO.
        """
        raise NotImplementedError("Método getAudioguia no implementado")
    
    @abstractmethod
    def insertAudioguia(self, audioguia: AudioguiasVO):
        """
        Inserta un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto AudioguiasVO a insertar.
        Devuelve: int: 1 si fue exitoso
        """
        raise NotImplementedError("Método insertAudioguia no implementado")
    
    @abstractmethod
    def deleteAudioguia(self, audioguia: AudioguiasVO):
        """
        Elimina un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto AudioguiasVO para borrar.
        """
        raise NotImplementedError("Método deleteAudioguia no implementado")

    @abstractmethod
    def updateAudioguia(self, audioguia: AudioguiasVO):
        """
        Actualiza el usuario que tenga el mismo dni que el que se le pasa en la base de datos.
        Parametros requeridos: El objeto AudioguiasVO a actualizar.
        """
        raise NotImplementedError("Método updateAudioguia no implementado")