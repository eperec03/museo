import sys
# #sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\src')

import tkinter as tk
from tkinter import messagebox
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from vista.RegistroClientePVentana import *
# from vista.InicioVentana import *

class ElegirUsuarioRegistro(QtWidgets.QMainWindow):
    def __init__(self, controlador = None):
        # Importamos el .ui
        super(ElegirUsuarioRegistro, self).__init__()
        uic.loadUi('src/vista/ui/TipoUsuarioRegistro.ui', self)
        self.setWindowTitle("Identifícate ")
        self.setWindowIcon(QIcon('src/vista/Imagenes/logomuseo.png'))  # Reemplaza con la ruta a tu logo
        # Almacena una referencia al controlador
        self.coordinador = controlador
        # "EnviarBoton" es el nombre que se le ha dado al objeto en el .ui
        self.BotonCliP.clicked.connect(self.go_to_window_premium)
        # self.BotonAtras.clicked.connect(self.go_back)
        self.show()

    def go_to_window_premium(self):
        self.ventana_Cliestandar = RegistroClientePVentana()
        self.ventana_Cliestandar.setCoordinador(self.coordinador)
        self.ventana_Cliestandar.show()
        self.hide()
        
    # def go_back(self):
    #     self.ventana_anterior = InicioVentana()
    #     self.ventana_anterior.setCoordinador(self.coordinador)
    #     self.ventana_anterior.show()
    #     self.delete()

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