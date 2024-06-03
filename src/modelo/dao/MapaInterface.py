from typing import List
from abc import ABC, abstractmethod
import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')
from vo.MapaVO import MapaVO

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class MapaInterface(ABC):
    @abstractmethod
    def getInfoMapa(self) -> MapaVO:

        raise NotImplementedError("Método getUsuarios no implementado")
    
    