import sys
# #sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\src')

import tkinter as tk
from tkinter import messagebox
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from vista.InicioEditoresVentana import *
from vista.InicioClientePVentana import *
from vista.RegistroEntradaVentana import RegistroEntradaVentana
# from vista.InicioVentana import *

class ElegirUsuario(QtWidgets.QMainWindow):
    def __init__(self, controlador = None,ventana_anterior=None):
        super(ElegirUsuario, self).__init__()
        uic.loadUi('src/vista/ui/TipoUsuario.ui', self)
        self.setWindowTitle("Identifícate ")
        self.setWindowIcon(QIcon('src/vista/Imagenes/logomuseo.png'))
        self.coordinador = controlador
        self.BotonCliE.clicked.connect(self.go_to_window_estandar)
        self.BotonCliP.clicked.connect(self.go_to_window_premium)
        self.BotonEditores.clicked.connect(self.go_to_window_editor)
        self.ventana_anterior=ventana_anterior
        self.BotonAtras.clicked.connect(self.go_back)
        self.show()

    def go_to_window_estandar(self):
        self.ventana_Cliestandar = RegistroEntradaVentana(ventana_anterior=self)
        self.ventana_Cliestandar.setCoordinador(self.coordinador)
        self.ventana_Cliestandar.show()
        self.hide()

    def go_to_window_premium(self):
        self.ventana_CliPremium = InicioClientePVentana(ventana_anterior=self)
        self.ventana_CliPremium.setCoordinador(self.coordinador)
        self.ventana_CliPremium.show()
        self.hide()

    def go_to_window_editor(self):
        self.ventana_editor = InicioEditorVentana(ventana_anterior=self)
        self.ventana_editor.setCoordinador(self.coordinador)
        self.ventana_editor.show()
        self.hide()

        
    def go_back(self):
        self.ventana_anterior.show()    
        self.destroy()

    def setCoordinador(self, coord) -> None:
        self.coordinador = coord

    #############################Listeners##############################



    def mostrar_advertencia(ex):
        mensaje = QMessageBox()
        mensaje.setIcon(QMessageBox.Warning)
        mensaje.setText("Error")
        mensaje.setInformativeText(str(ex))
        mensaje.setWindowTitle("Advertencia")
        mensaje.exec_()