import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\src')

import tkinter as tk
from tkinter import messagebox
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from vista.RegistroEditoresVentana import *

class MenuEditor(QtWidgets.QMainWindow):
    def __init__(self, controlador = None,ventana_anterior=None):
        # Importamos el .ui
        super().__init__()
        uic.loadUi('src/vista/ui/MenuEdicion.ui', self)
        self.setWindowTitle("MENU EDICIÓN")
        self.setWindowIcon(QIcon('src/vista/Imagenes/logomuseo.png'))  # Reemplaza con la ruta a tu logo
        # Almacena una referencia al controlador
        self.coordinador = controlador
        # "EnviarBoton" es el nombre que se le ha dado al objeto en el .ui
        self.ventana_anterior=ventana_anterior
        self.BotonAtras.clicked.connect(self.go_back)
        self.BotonSalas.clicked.connect(self.go_salas)
        self.BotonCatalogo.clicked.connect(self.go_catalogo)
        self.BotonExposiciones.clicked.connect(self.go_exposiciones)
        self.BotonObjetos.clicked.connect(self.go_objetos)
        self.BotonJuegos.clicked.connect(self.go_juegos)
        self.BotonObras.clicked.connect(self.go_obras)
        self.BotonArtistas.clicked.connect(self.go_artistas)
        self.BotonAudioguias.clicked.connect(self.go_audioguias)
        
        self.show()

    def go_back(self):
        self.ventana_anterior.show()    
        self.destroy()       

    def go_salas(self):
        self.ventana_salas = EdicionSalas()
        self.ventana_salas.setCoordinador(self)
        self.ventana_salas.show()
        self.hide()

    def go_catalogo(self):
        self.ventana_catalogo = EdicionCatalogo()
        self.ventana_catalogo.setCoordinador(self)
        self.ventana_catalogo.show()
        self.hide()

    def go_exposiciones(self):
        self.ventana_exposiciones = MenuEdicionExposiciones()
        self.ventana_exposiciones.setCoordinador(self)
        self.ventana_exposiciones.show()
        self.hide()

    def go_objetos(self):
        self.ventana_objetos = MenuEdicionObjetos()
        self.ventana_objetos.setCoordinador(self)
        self.ventana_objetos.show()
        self.hide()

    def go_juegos(self):
        self.ventana_juegos = MenuEdicionJuegos()
        self.ventana_juegos.setCoordinador(self)
        self.ventana_juegos.show()
        self.hide()

    def go_obras(self):
        self.ventana_obras = MenuEdicionObras()
        self.ventana_obras.setCoordinador(self)
        self.ventana_obras.show()
        self.hide()

    def go_artistas(self):
        self.ventana_artistas = MenuEdicionArtistas()
        self.ventana_artistas.setCoordinador(self)
        self.ventana_artistas.show()
        self.hide()

    def go_audioguias(self):
        self.ventana_audioguias = MenuEdicionAudioguias()
        self.ventana_audioguias.setCoordinador(self)
        self.ventana_audioguias.show()
        self.hide()
    
    def setCoordinador(self, coord) -> None:
        self.coordinador = coord

    def mostrar_advertencia(ex):
        mensaje = QMessageBox()
        mensaje.setIcon(QMessageBox.Warning)
        mensaje.setText("Error")
        mensaje.setInformativeText(str(ex))
        mensaje.setWindowTitle("Advertencia")
        mensaje.exec_()
