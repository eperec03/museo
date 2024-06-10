import sys
# #sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src')

import tkinter as tk
from tkinter import messagebox
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from vista.MapaVentana import *
from vista.ExposicionVentana import *
from vista.VentanaJuegos import *
from vista.VentanaSubastas import *
from vista.Catalogo import *

class VentanaServicioPremium(QtWidgets.QMainWindow):
    def __init__(self, controlador = None, ventana_anterior=None):
        # Importamos el .ui
        super(VentanaServicioPremium, self).__init__()
        uic.loadUi('src/vista/ui/VentanaServiciosPremium.ui', self)
        self.setWindowTitle("Museo: ")
        self.setWindowIcon(QIcon('src/vista/Imagenes/logomuseo.png'))  # Reemplaza con la ruta a tu logo
        # Almacena una referencia al controlador
        self.coordinador = controlador
        # "EnviarBoton" es el nombre que se le ha dado al objeto en el .ui
        self.BotonMapa.clicked.connect(self.go_to_window_mapa)
        self.BotonJuegos.clicked.connect(self.go_to_window_juegos)    
        self.BotonCatalogo.clicked.connect(self.go_to_window_objetos)
        self.BotonExposiciones.clicked.connect(self.go_to_window_exposiciones) 
        self.BotonSubastas.clicked.connect(self.go_to_window_subastas)
        self.ventana_anterior=ventana_anterior
        self.BotonAtras.clicked.connect(self.go_back)

    def go_back(self):
        self.ventana_anterior.show()
        self.destroy()

    def go_to_window_juegos(self):
        self.ventana_registro = VentanaJuegos(ventana_anterior=self)
        self.ventana_registro.setCoordinador(self.coordinador)
        self.ventana_registro.show()
        self.hide()

    def go_to_window_mapa(self):
        self.ventana_registro = MapaVentana(ventana_anterior=self)
        self.ventana_registro.setCoordinador(self.coordinador)
        self.ventana_registro.show()
        self.hide()

    def go_to_window_objetos(self):
        self.ventana_inicio = VentanaCatalogo(controlador=self.coordinador,ventana_anterior=self)
        self.ventana_inicio.show()
        self.hide()

    def go_to_window_exposiciones(self):
        self.ventana_registro = VentanaExposiciones(controlador=self.coordinador, ventana_anterior=self)
        self.ventana_registro.show()
        self.hide()

    def go_to_window_subastas(self):
        self.ventana_registro = VentanaSubastas(controlador=self.coordinador,ventana_anterior=self)
        self.ventana_registro.show()
        self.hide()   

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