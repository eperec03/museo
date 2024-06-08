import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src')

from modelo.vo.UsuariosVO import *
from modelo.vo.ClienteEstandarVO import *


class Coordinador:
    def __init__(self):
      self._model = None
      #Puede tener tantas referencias a ventanas como controle
      self._viewInicio = None
      self._viewRegistro = None
      self._viewEliminarUsuario = None
      self._viewActualizarUsuario = None
      self._viewRegistroEntrada = None
      self._viewTipoUsuario = None

      
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

    def getViewRegistroEntrada(self):
       return self._viewRegistroEntrada

    def setViewRegistroEntrada(self, view):
       self._viewRegistroEntrada = view

    def getViewInicio(self):
       return self._viewInicio

    def setViewInicio(self, view):
       self._viewInicio = view
    
    def getViewTipoUsuario(self):
       return self._viewTipoUsuario

    def setViewTipoUsuario(self, view):
       self._viewTipoUsuario = view
    ##############################################

    def registrarUsuario(self, usuario: ClientePremiumVO) -> None:
       self._model.validar_registro(usuario)
       #aqui van los metodos de lo que hacen los 'botones'

    def eliminarUsuario(self, usuario: ClientePremiumVO) -> None:
       self._model.eliminar_registro(usuario)

    def actualizarUsuario(self, usuario: ClientePremiumVO) -> None:
       self._model.actualizar_registro(usuario)
    
    def registrarEntrada(self, usuario: ClienteEstandarVO) -> bool:
       if self._model.validar_entrada(usuario):
          return True      
   
    def validarUsuario(self, usuario: ClientePremiumVO) -> bool:
       if self._model.comprobar_cliente(usuario):
         return True