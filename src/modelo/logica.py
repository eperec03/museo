import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src')

import tkinter as tk
from tkinter import messagebox
from modelo.vo.UsuariosVO import *
from modelo.dao.ClientePremiumDAO import *
from modelo.dao.EditoresDAO import *
from modelo.vo.ClienteEstandarVO import *
from modelo.dao.ClienteEstandarDAO import *
from controlador.coordinador import Coordinador
from dao.ObjetosDAO import *
from modelo.vo.JuegosVO import *
from dao.JuegosObrasDAO import *

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
    
    def validar_registro_editor(self, mi_persona: EditorVO):
        #habría que poner más cosas para validar el registtro?
        if '@' in mi_persona.get_UsuEmail():
            mi_persona_dao = EditorDAO()
            mi_persona_dao.insertUsuario(mi_persona)
        else:
            messagebox.showwarning("Advertencia", "El email no es válido")