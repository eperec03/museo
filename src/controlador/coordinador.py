import sys
#sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src')

from modelo.vo.UserVO import UserVO
from vista.RegistroUsuarioVentana import RegistroUsuarioVentana

class Coordinador:
    def __init__(self):
      self._model = None
      #Puede tener tantas referencias a ventanas como controle
      self._viewRegistro = None
      
    def getModel(self):
       return self._model
    
    def setModel(self, model):
       self._model = model
    
    #Se añade para cada ventana
    def getViewRegistro(self):
       return self._viewRegistro
    
    def setViewRegistro(self, view):
       self._viewRegistro = view
    
    ##############################################

    def registrarUsuario(self, usuario: UserVO) -> None:
       self._model.validar_registro(usuario)
       #aqui van los metodos de lo que hacen los 'botones'
      