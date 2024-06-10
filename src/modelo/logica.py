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

from controlador.coordinador import Coordinador

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

    def actualizar_sala(self, sala: SalasVO):
        sala_dao=SalasDAO()
        error=1
        for i in range (len(sala_dao.getSalas)):
            if sala.NumeroSala() == sala_dao.getSalas[i].getNumeroSala():            
                sala_dao.updateSala(sala)
                error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe ese NumeroSala")

    def actualizar_catalogo(self, catalogo: CatalogoVO):
        catalogo_dao=CatalogoDAO()
        error=1
        for i in range (len(catalogo_dao.getCatalogo)):
            if catalogo.IdCatalogo() == catalogo_dao.getCatalogos[i].getIdCatalogo():            
                catalogo_dao.updateCatalogo(catalogo)
                error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe ese IDCatalogo")

    def actualizar_juego(self, juego: JuegosVO):
        juego_dao=JuegosDAO()
        error=1
        for i in range (len(juego_dao.getJuegos)):
            if juego.NumeroSala() == juego_dao.getJuegos[i].get_IDJuego():            
                juego_dao.updateJuego(juego)
                error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe ese IDJuego")
    
    def actualizar_objeto(self, objeto: ObjetosVO):
        objeto_dao=ObjetosDAO()
        error=1
        for i in range (len(objeto_dao.getObjetos)):
            if objeto.IdObjeto() == objeto_dao.getObjetos[i].getIdObjeto():            
                objeto_dao.updateObjeto(objeto)
                error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe ese IDObjeto")
    
    def actualizar_obra(self, obra: ObrasVO):
        obra_dao=ObrasDAO()
        error=1
        for i in range (len(obra_dao.getObras)):
            if obra.IdObra() == obra_dao.getObras[i].getIdObra():            
                obra_dao.updateObra(obra)
                error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe ese IDObra")
    
    def actualizar_artista(self, artista: ArtistasVO):
        artista_dao=ArtistasDAO()
        error=1
        for i in range (len(artista_dao.getArtistas)):
            if artista.IdArtista() == artista_dao.getArtistas[i].getIdArtista():            
                artista_dao.updateArtista(artista)
                error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe ese IDArtista")

    def actualizar_audioguia(self, audioguia: AudioguiasVO):
        audioguia_dao=AudioguiasDAO()
        error=1
        for i in range (len(audioguia_dao.getAudioguias)):
            if audioguia.IdAudio() == audioguia_dao.getAudioguias[i].getIdAudio():            
                audioguia_dao.updateAudioguia(audioguia)
                error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe ese IDAudioguia")

    def actualizar_exposicion(self, exposicion: ExposicionesVO):
        exposicion_dao=ExposicionesDAO()
        error=1
        for i in range (len(exposicion_dao.getExposiciones)):
            if exposicion.IdExposicion() == exposicion_dao.getExposiciones[i].getIdExposicion():            
                exposicion_dao.updateSala(exposicion)
                error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe ese IDExposicion")


    def comprobar_juego(self, mi_juego: JuegosObrasVO):
        mi_juego_dao = JuegosObrasDao()
        error=1
        if len(mi_juego_dao.getJuegoObras(mi_juego.get_Nombre()))==0:
            messagebox.showwarning("Advertencia", "No existe ese juego")
        else:
            return True


    def select_objetos(self):
        a=ObjetosDao()
        return a.getObjetos()
    
    def select_objetos(self):
        a=ObrasDao()
        return a.getObras()
    
    def select_artistas(self,id):
        a=ArtistasDao()
        return a.getArtista()
    
    
    def validar_registro_editor(self, mi_persona: EditorVO):
        #habría que poner más cosas para validar el registtro?
        if '@' in mi_persona.get_UsuEmail():
            mi_persona_dao = EditorDAO()
            mi_persona_dao.insertUsuario(mi_persona)
        else:
            messagebox.showwarning("Advertencia", "El email no es válido")