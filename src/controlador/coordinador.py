import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src')

from modelo.vo.UsuariosVO import *
from modelo.vo.ClienteEstandarVO import *
from modelo.vo.JuegosVO import *
from modelo.vo.UsuariosVO import *
from modelo.vo.ClienteEstandarVO import *
from modelo.vo.JuegosVO import *
from modelo.vo.ArtistasVO import *
from modelo.vo.ObrasVO import *
from modelo.vo.ObjetosVO import *
from modelo.vo.AudioguiasVO import *
from modelo.vo.ExposicionesVO import *
from modelo.vo.JuegosVO import *
from modelo.vo.SalasVO import *
from modelo.vo.CatalogoVO import *


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
      self._obtener_todos_objetos=None

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

   def registrarEditor(self, usuario: EditorVO) -> None:
      self._model.validar_registroEditor(usuario)

   def eliminarUsuario(self, usuario: ClientePremiumVO) -> None:
      self._model.eliminar_registro(usuario)

   def actualizarUsuario(self, usuario: ClientePremiumVO) -> None:
      self._model.actualizar_registro(usuario)

   def registrarEntrada(self, entrada: ClienteEstandarVO) -> bool:
      if self._model.validar_entrada(entrada):
         return True      

   def validarUsuario(self, usuario: ClientePremiumVO) -> bool:
      if self._model.comprobar_cliente(usuario):
         return True
      
   def validarEditores(self, editores: EditorVO) -> bool:
      if self._model.comprobar_editor(editores):
         return True
      
   def validarJuego(self, juego: JuegosObrasVO, obra:ObrasVO) -> str:
      return self._model.comprobar_juego(juego, obra)
      
   # def validarObra(self, obra: ObrasVO) -> bool:
   #    if self._model.comprobar_obra(obra):
   #       return True

   def registrarEditor(self, usuario: EditorVO) -> None:
      self._model.validar_registro(usuario)

   def obtener_todos_objetos(self):
      return self._model.select_objetos()

   def obtener_todos_exposiciones(self):
      return self._model.select_exposiciones()

   def obtener_artista(self,obra):
      return self._model.select_artista_nombre(obra)

   def actualizarSala(self, sala: SalasVO) -> None:
      self._model.actualizar_sala(sala)

   def actualizarArtista(self, artista: ArtistasVO) -> None:
      self._model.actualizar_artista(artista)

   def actualizarObjeto(self, objeto: ObjetosVO) -> None:
      self._model.actualizar_objeto(objeto)

   def actualizarObras(self, obra: ObrasVO) -> None:
      self._model.actualizar_obra(obra)

   def actualizarJuegos(self, juego: JuegosVO) -> None:
      self._model.actualizar_juego(juego)

   def actualizarCatalogo(self, catalogo: CatalogoVO) -> None:
      self._model.actualizar_catalogo(catalogo)

   def actualizarAudioguias(self, audioguia: AudioguiasVO) -> None:
      self._model.actualizar_audioguia(audioguia)

   def actualizarExposiciones(self, exposicion: ExposicionesVO) -> None:
      self._model.actualizar_exposicion(exposicion)

   def obtener_todas_obras(self):
      return self._model.select_obras()

   def eliminarExposiciones(self, exposicion: ExposicionesVO) -> None:
      self._model.eliminar_exposicion(exposicion)

   def eliminarSala(self, sala: SalasVO) -> None:
      self._model.eliminar_sala(sala)

   def eliminarArtista(self, artista: ArtistasVO) -> None:
      self._model.eliminar_artista(artista)

   def eliminarObjeto(self, objeto: ObjetosVO) -> None:
      self._model.eliminar_objeto(objeto)

   def eliminarObras(self, obra: ObrasVO) -> None:
      self._model.eliminar_obra(obra)

   def eliminarJuegos(self, juego: JuegosVO) -> None:
      self._model.eliminar_juego(juego)

   def eliminarCatalogo(self, catalogo: CatalogoVO) -> None:
      self._model.eliminar_catalogo(catalogo)

   def eliminarAudioguias(self, audioguia: AudioguiasVO) -> None:
      self._model.eliminar_audioguia(audioguia)
   
   def crearArtistas(self, artista: ArtistasVO) -> None:
      self._model.crear_artistas(artista)
   
   def crearAudioguia(self, audio: AudioguiasVO) -> None:
      self._model.crear_audioguias(audio)

   def crearExposiciones(self, exposicion: ExposicionesVO) -> None:
      self._model.crear_exposiciones(exposicion)

   def crearJuegos(self, juego: JuegosObrasVO) -> None:
      self._model.crear_juegos(juego)

   def crearObjetos(self, objeto:ObjetosVO) -> None:
      self._model.crear_objetos(objeto)

   def crearObras(self, obras:ObrasVO) -> None:
      self._model.crear_obras(obras)
