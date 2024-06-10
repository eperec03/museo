import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src')

import tkinter as tk

from tkinter import messagebox

from modelo.dao.ClientePremiumDAO import *
from modelo.dao.EditoresDAO import *
from modelo.dao.ObrasDAO import *
from modelo.dao.ClienteEstandarDAO import *
from dao.ObjetosDAO import *
from dao.JuegosObrasDAO import *
from dao.ArtistasDAO import *

from modelo.vo.UsuariosVO import *
from modelo.vo.ClienteEstandarVO import *
from modelo.vo.JuegosVO import *
from dao.JuegosObrasDAO import *
from modelo.vo.ArtistasVO import *
from modelo.dao.ArtistasDAO import *
from modelo.vo.ObrasVO import *
from modelo.dao.ObrasDAO import *
from modelo.vo.ObjetosVO import *
from modelo.dao.ObjetosDAO import *
from modelo.vo.AudioguiasVO import *
from modelo.dao.AudioguiasDAO import *
from modelo.vo.ExposicionesVO import *
from modelo.dao.ExposicionesDAO import *
from modelo.vo.JuegosVO import *
from modelo.dao.JuegosDAO import *
from modelo.vo.SalasVO import *
from modelo.dao.SalasDAO import *
from modelo.vo.CatalogoVO import *
from modelo.dao.CatalogoDAO import *
from modelo.vo.SubastasVO import *
from modelo.dao.SubastasDAO import *

from controlador.coordinador import Coordinador
from dao.ObrasDAO import *

class Logica:
    def __init__(self):
        self._mi_coordinador = None

    def set_coordinador(self, mi_coordinador: Coordinador) -> None:
        self._mi_coordinador = mi_coordinador

    def validar_registro(self, mi_persona: ClientePremiumVO):
        #habría que poner más cosas para validar el registtro?
        if '@' in mi_persona.get_UsuEmail():
            mi_persona_dao = ClientePremiumDAO()
            mi_persona_dao.getClientesP()                  
            mi_persona_dao.insertClienteP(mi_persona)
        else:
            messagebox.showwarning("Advertencia", "El email no es válido")

    def eliminar_registro(self, mi_persona: ClientePremiumVO):
        mi_persona_dao=ClientePremiumDAO()
        error=1
        if mi_persona.get_DNI() == mi_persona_dao.getClienteP(mi_persona.get_DNI()).get_DNI():            
                mi_persona_dao.eliminateClienteP(mi_persona)
                error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe nadie con ese DNI")

    def actualizar_registro(self, mi_persona: ClientePremiumVO):
        mi_persona_dao=ClientePremiumDAO()
        error=1
        for i in range (len(mi_persona_dao.getUsuarios)):
            if mi_persona.DNI() == mi_persona_dao.getUsuarios[i].get_DNI():            
                mi_persona_dao.updateClienteP(mi_persona)
                error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe nadie con ese DNI")

    # def comprobar_entrada(self, mi_e)

    def validar_entrada(self, mi_entrada: ClienteEstandarVO):
        #habría que poner más cosas para validar el registtro?
        mi_entrada_dao = ClienteEstandarDAO()
        if len(mi_entrada_dao.getEntrada(mi_entrada.getNumEntrada()))==0:            
            messagebox.showwarning("Advertencia", "Número de entrada incorrecto")            
        else:
            return True

    def comprobar_cliente(self, mi_persona: ClientePremiumVO):
        mi_persona_dao=ClientePremiumDAO()
        error=1
        if len(mi_persona_dao.getClienteP(mi_persona.get_DNI()))==0:
            messagebox.showwarning("Advertencia", "No existe nadie con ese DNI")
        else:
            if mi_persona.get_UsuContrasenna() == mi_persona_dao.getClienteP(mi_persona.get_DNI())[0].get_UsuContrasenna():
                error=0
                return True
            if error==1:
                messagebox.showwarning("Advertencia", "Contraseña incorrecta")

    def comprobar_editor(self, editor: EditorVO):  
        editor_dao=EditorDAO()
        error=1
        if len(editor_dao.getEditor(editor.get_DNI()))==0:
            messagebox.showwarning("Advertencia", "No existe nadie con ese DNI")
        else:
            if editor.get_UsuContrasenna() == editor_dao.getEditor(editor.get_DNI())[0].get_UsuContrasenna():
                error=0
                return True
            if error==1:
                messagebox.showwarning("Advertencia", "Contraseña incorrecta")

    def actualizar_sala(self, sala: SalasVO):
        sala_dao=SalasDao()
        error=1
        if sala.getNumeroSala() == sala_dao.getSala(sala.getNumeroSala()).getNumeroSala():            
            sala_dao.updateSala(sala)
            error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe ese NumeroSala")

    def actualizar_catalogo(self, catalogo: CatalogoVO):
        catalogo_dao=CatalogoDao()
        error=1
        if catalogo.getTitulo() == catalogo_dao.getCatalogo(catalogo.getTitulo()).getTitulo():            
            catalogo_dao.updateCatalogo(catalogo)
            error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe ese IDCatalogo")

    def actualizar_juego(self, juego: JuegosVO):
        juego_dao=JuegosDao()
        error=1
        if juego.get_IDJuego() == juego_dao.getJuego(juego.get_Nombre()).get_IDJuego():            
            juego_dao.updateJuego(juego)
            error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe ese IDJuego")
    
    def actualizar_objeto(self, objeto: ObjetosVO):
        objeto_dao=ObjetosDao()
        error=1
        if objeto.getNombreObjeto() == objeto_dao.getObjeto(objeto.getNombreObjeto()).getNombreObjeto():            
            objeto_dao.updateObjeto(objeto)
            error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe ese IDObjeto")
    
    def actualizar_obra(self, obra: ObrasVO):
        obra_dao=ObrasDao()
        error=1
        if obra.getTitulo() == obra_dao.getObraTitulo(obra.getTitulo())[0].getTitulo():            
            obra_dao.updateObra(obra)
            error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe ese Titulo")
    
    def actualizar_artista(self, artista: ArtistasVO):
        artista_dao=ArtistasDao()
        error=1
        if artista.getNombreArtista() == artista_dao.getArtista(artista.getNombreArtista()).getNombreArtista():            
            artista_dao.updateArtista(artista)
            error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe ese nombre de artista.")

    def actualizar_audioguia(self, audioguia: AudioguiasVO):
        audioguia_dao=AudioguiasDao()
        error=1
        if audioguia.getTitulo() == audioguia_dao.getAudioguia(audioguia.getTitulo()).getTitulo():            
            audioguia_dao.updateAudioguia(audioguia)
            error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe ese título de audioguia.")

    def actualizar_exposicion(self, exposicion: ExposicionesVO):
        exposicion_dao=ExposicionesDao()
        error=1
        if exposicion.getTitulo() == exposicion_dao.getExposicion(exposicion.getTitulo()).getTitulo():            
            exposicion_dao.updateExposicion(exposicion)
            error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe ese título")


    def comprobar_juego(self, mi_juego: JuegosObrasVO, mi_obra: ObrasVO):
        mi_juego_dao = JuegosObrasDao()
        mi_obra_dao = ObrasDao()
        # print(mi_obra_dao.getObraTitulo(mi_obra.getTitulo()))
        if len(mi_obra_dao.getObraTitulo(mi_obra.getTitulo()))==0:
            messagebox.showwarning("Advertencia", "No existe esa obra")
        elif len(mi_juego_dao.getJuegoO(mi_juego.get_Nombre(), mi_obra_dao.getObraTitulo(mi_obra.getTitulo())[0].getIdObra()))==0:
            messagebox.showwarning("Advertencia", "No existe ese juego para esa obra")
        else:
            return mi_juego_dao.getJuegoO(mi_juego.get_Nombre(), mi_obra_dao.getObraTitulo(mi_obra.getTitulo())[0].getIdObra())[0].get_ruta()

    def select_objetos(self):
        a=ObjetosDao()
        return a.getObjetos()

    def select_exposiciones(self):
        a=ExposicionesDao()
        return a.getExposiciones()
    
    def select_subastas(self):
        a=SubastasDao()
        return a.getSubastas()
    
    def select_obras_1(self):
        a=ObrasDao()
        return a.getObrasFiltro(1)
    
    def select_obras_2(self):
        a=ObrasDao()
        return a.getObrasFiltro(2)
    
    def select_artista_nombre(self,id):
        a=ArtistasDao()
        return a.getArtistaNombre(id)
    
    
    def validar_registro_editor(self, mi_persona: EditorVO):
        #habría que poner más cosas para validar el registtro?
        if '@' in mi_persona.get_UsuEmail():
            mi_persona_dao = EditorDAO()
            mi_persona_dao.insertUsuario(mi_persona)
        else:
            messagebox.showwarning("Advertencia", "El email no es válido")

    def crear_artistas(self, artista: ArtistasVO):
        artista_dao = ArtistasDao()
        artista_dao.insertArtista(artista)

    def eliminar_obra(self, obra: ObrasVO):
        obra_dao=ObrasDao()
        error=1
        if obra.getTitulo() == obra_dao.getObraTitulo(obra.getTitulo())[0].getTitulo():            
            obra_dao.deleteObra(obra.getTitulo())
            error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe ese IDObra")

    def eliminar_sala(self, sala: SalasVO):
        sala_dao=SalasDao()
        error=1
        if sala.getNumeroSala() == sala_dao.getSala(sala.getNumeroSala()).getNumeroSala():            
            sala_dao.deleteSala(sala)
            error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe ese NumeroSala")

    def eliminar_catalogo(self, catalogo: CatalogoVO):
        catalogo_dao=CatalogoDao()
        error=1
        if catalogo.getTitulo() == catalogo_dao.getCatalogo(catalogo.getTitulo()).getTitulo():            
            catalogo_dao.deleteCatalogo(catalogo)
            error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe ese IDCatalogo")

    def eliminar_juego(self, juego: JuegosVO):
        juego_dao=JuegosDao()
        error=1
        print(juego.get_IDJuego())
        print(juego_dao.getJuego(juego.get_IDJuego()).get_IDJuego())
        if juego.get_IDJuego() == juego_dao.getJuego(juego.get_IDJuego()).get_IDJuego():            
            error=0
            print('h')
            juego_dao.deleteJuego(juego.get_IDJuego())
        else:
            messagebox.showwarning("Advertencia", "No existe ese IDJuego")
    
    def eliminar_objeto(self, objeto: ObjetosVO):
        objeto_dao=ObjetosDao()
        error=1
        if objeto.getNombreObjeto() == objeto_dao.getObjeto(objeto.getNombreObjeto()).getNombreObjeto():            
            objeto_dao.deleteObjeto(objeto.getNombreObjeto())
            error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe ese IDObjeto")
    
    def eliminar_artista(self, artista: ArtistasVO):
        artista_dao=ArtistasDao()
        error=1
        if artista.getNombreArtista() == artista_dao.getArtista(artista.getNombreArtista()).getNombreArtista():            
            artista_dao.deleteArtista(artista.getNombreArtista())
            error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe ese nombre de artista.")

    def eliminar_audioguia(self, audioguia: AudioguiasVO):
        audioguia_dao=AudioguiasDao()
        error=1
        if audioguia.getTitulo() == audioguia_dao.getAudioguia(audioguia.getTitulo()).getTitulo():            
            audioguia_dao.deleteAudioguia(audioguia.getTitulo())
            error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe ese título de audioguia.")

    def eliminar_exposicion(self, exposicion: ExposicionesVO):
        exposicion_dao=ExposicionesDao()
        error=1
        if exposicion.getTitulo() == exposicion_dao.getExposicion(exposicion.getTitulo()).getTitulo():            
            exposicion_dao.deleteExposicion(exposicion.getTitulo())
            error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe ese título")
 
    def crear_audioguias(self, audio: AudioguiasVO):
        audio_dao = AudioguiasDao()
        audio_dao.insertAudioguia(audio)

    def crear_exposiciones(self, exposicion: ExposicionesVO):
        exposicion_dao = ExposicionesDao()
        exposicion_dao.insertExposicion(exposicion)

    def crear_juegos(self, juego: JuegosObrasVO):
        juegos_dao = JuegosObrasDao()
        juegos_dao.insertJuegosObras(juego)

    def crear_objetos(self, objeto: ObjetosVO):
        objetos_dao = ObjetosDao()
        objetos_dao.insertObjeto(objeto)

    def crear_obras(self, obras: ObrasVO):
        obra_dao = ObrasDao()
        obra_dao.insertObra(obras)
