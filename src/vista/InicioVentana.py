import sys
# #sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\src')

import tkinter as tk
from tkinter import messagebox
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from vista.ElegirUsuarioRegistro import *
from vista.ElegirUsuario import *


class InicioVentana(QtWidgets.QMainWindow):
    def __init__(self, controlador = None):
        # Importamos el .ui
        super(InicioVentana, self).__init__()
        uic.loadUi('src/vista/ui/Principal.ui', self)
        self.setWindowTitle("Museo: ")
        self.setWindowIcon(QIcon('src/vista/Imagenes/logomuseo.png'))  # Reemplaza con la ruta a tu logo
        # Almacena una referencia al controlador
        self.coordinador = controlador
        # "EnviarBoton" es el nombre que se le ha dado al objeto en el .ui
        self.BotonRegistrarse.clicked.connect(self.go_to_window_registro)
        self.BotonInicioS.clicked.connect(self.go_to_window_inicio)

        self.show()

    def go_to_window_registro(self):
        self.ventana_registro = ElegirUsuarioRegistro(ventana_anterior=self)
        self.ventana_registro.setCoordinador(self.coordinador)
        self.ventana_registro.show()
        self.hide()

    def go_to_window_inicio(self):
        self.ventana_inicio = ElegirUsuario(ventana_anterior=self)
        self.ventana_inicio.setCoordinador(self.coordinador)
        self.ventana_inicio.show()
        self.hide() 

    #-------------QUITAR DESPUES DE HABER HECHO LA PRUEBA-----------------------------
    # def go_to_window_objetos(self):
    #     self.ventana_inicio = LogicaPruebaScroll()
    #     self.ventana_inicio.setCoordinador(self.coordinador)
    #     self.ventana_inicio.show()
    #     self.hide()
    #---------------------------------------------------------------------------------- 

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