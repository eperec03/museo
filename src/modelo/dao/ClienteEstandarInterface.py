from typing import List
from abc import ABC, abstractmethod

import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\modelo')

from vo.ClientesEstandarVO import ClienteEstandarVO

class ClienteEInterface(ABC):
    @abstractmethod
    def getEntradas(self) -> List[ClienteEstandarVO]:
        raise NotImplementedError("Método getUsuarios no implementado")
    
    @abstractmethod
    def insertEntrada(self, entrada: ClienteEstandarVO):
        raise NotImplementedError("Método insertEntrada no implementado")
    
    # @abstractmethod
    # def eliminateUsuario(self, usuarios: ClienteEstandarVO):
    #     raise NotImplementedError("Método eliminateUsuario no implementado")

    # @abstractmethod
    # def updateUsuario(self, usuarios: ClienteEstandarVO):
    #     raise NotImplementedError("Método updateUsuario no implementado")