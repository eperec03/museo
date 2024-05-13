import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src')

from modelo.vo.UserVO import UserVO
from vista.RegistroUsuarioVentana import RegistroUsuarioVentana

class Coordinador:
    def __init__(self):
      self._model = None
      #Puede tener tantas referencias a ventanas como controle
      self._viewRegistro = None
      self._viewEliminarUsuario = None
      self._viewActualizarUsuario = None
      
    def getModel(self):
       return self._model
    
    def setModel(self, model):
       self._model = model
    
    #Se añade para cada ventana
    def getViewRegistro(self):
       return self._viewRegistro
    
    def setViewRegistro(self, view):
       self._viewRegistro = view
    
    def getViewEliminarUsuario(self):
       return self._viewEliminarUsuario

    def setViewEliminarUsuario(self, view):
       self._viewEliminarUsuario = view

    def getViewActualizarUsuario(self):
       return self._viewActualizarUsuario

    def setViewActualizarUsuario(self, view):
       self._viewActualizarUsuario = view
    
    ##############################################

    def registrarUsuario(self, usuario: UserVO) -> None:
       self._model.validar_registro(usuario)
       #aqui van los metodos de lo que hacen los 'botones'

    def eliminarUsuario(self, usuario: UserVO) -> None:
       self._model.eliminar_registro(usuario)

    def actualizarUsuario(self, usuario: UserVO) -> None:
       self._model.actualizar_registro(usuario)
    
      