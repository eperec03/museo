from typing import List
from abc import ABC, abstractmethod
import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')
from vo.TarifasVO import TarifasVO

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class TarifasInterface(ABC):
    @abstractmethod
    def getTarifas(self) -> List[TarifasVO]:
        """
        Recupera todas las Tarifa de la base de datos.        
        Devuelve: List[TarifasVO]: Una lista de objetos TarifasVO.
        """
        raise NotImplementedError("Método getTarifas no implementado")
    
    @abstractmethod
    def getTarifa(self,id) ->TarifasVO:
        """
        Recupera la Tarifa de la base de datos cuyo identificador es id.        
        Devuelve: objeto TarifasVO.
        """
        raise NotImplementedError("Método getTarifa no implementado")
    
    @abstractmethod
    def insertTarifa(self, Tarifa: TarifasVO):
        """
        Inserta un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto TarifasVO a insertar.
        Devuelve: int: 1 si fue exitoso
        """
        raise NotImplementedError("Método insertTarifa no implementado")
    
    @abstractmethod
    def deleteTarifa(self, Tarifa: TarifasVO):
        """
        Elimina un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto TarifasVO para borrar.
        """
        raise NotImplementedError("Método deleteTarifa no implementado")

    @abstractmethod
    def updateTarifa(self, Tarifa: TarifasVO):
        """
        Actualiza el usuario que tenga el mismo dni que el que se le pasa en la base de datos.
        Parametros requeridos: El objeto TarifasVO a actualizar.
        """
        raise NotImplementedError("Método updateTarifa no implementado")