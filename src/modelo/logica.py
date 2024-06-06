import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src')

import tkinter as tk
from tkinter import messagebox
from modelo.vo.ClientePremiumVO import *
from modelo.dao.ClientePremiumDAO import *
from modelo.vo.ClienteEstandarVO import *
from modelo.dao.ClienteEstandarDAO import *
from controlador.coordinador import Coordinador

class Logica:
    def __init__(self):
        self._mi_coordinador = None

    def set_coordinador(self, mi_coordinador: Coordinador) -> None:
        self._mi_coordinador = mi_coordinador

    def validar_registro(self, mi_persona: ClientePremiumVO):
        #habría que poner más cosas para validar el registtro?
        if '@' in mi_persona.getEmail():
            mi_persona_dao = ClientePremiumDAO()
            mi_persona_dao.getUsuarios()                  
            mi_persona_dao.insertUsuario(mi_persona)
        else:
            messagebox.showwarning("Advertencia", "El email no es válido")

    def eliminar_registro(self, mi_persona: ClientePremiumVO):
        mi_persona_dao=ClientePremiumDAO()
        error=1
        if mi_persona.getDNI() == mi_persona_dao.getUsuario(mi_persona.getDNI()).getDNI():            
                mi_persona_dao.eliminateUsuario(mi_persona)
                error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe nadie con ese DNI")

    def actualizar_registro(self, mi_persona: ClientePremiumVO):
        mi_persona_dao=ClientePremiumDAO()
        error=1
        for i in range (len(mi_persona_dao.getUsuarios)):
            if mi_persona.DNI() == mi_persona_dao.getUsuarios[i].getDNI():            
                mi_persona_dao.updateUsuario(mi_persona)
                error=0
        if error==1:
            messagebox.showwarning("Advertencia", "No existe nadie con ese DNI")


    def validar_entrada(self, mi_entrada: ClienteEstandarVO):
        #habría que poner más cosas para validar el registtro?
        mi_entrada_dao = ClienteEstandarDAO()
        mi_entrada_dao.getEntradas()                  
        mi_entrada_dao.insertEntrada(mi_entrada)