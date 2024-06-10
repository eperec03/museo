import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\src')

import tkinter as tk
from tkinter import messagebox
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from vista.MenuEditor import *
from vista.ActualizaExposiciones import *
from vista.CrearExposiciones import *
from vista.EliminarExposiciones import *

class EditarExposiciones(QtWidgets.QMainWindow):
    def __init__(self, controlador = None,ventana_anterior=None):
        # Importamos el .ui
        super().__init__()
        uic.loadUi('src/vista/ui/MenuEdicionExposiciones.ui', self)
        self.setWindowTitle("EDICIÓN DE EXPOSICIONES")
        self.setWindowIcon(QIcon('src/vista/Imagenes/logomuseo.png'))  # Reemplaza con la ruta a tu logo
        # Almacena una referencia al controlador
        self.coordinador = controlador
        # "EnviarBoton" es el nombre que se le ha dado al objeto en el .ui
        self.ventana_anterior=ventana_anterior
        self.BotonAtras.clicked.connect(self.go_back)
        self.BotonCrear.clicked.connect(self.go_crear)
        self.BotonEliminar.clicked.connect(self.go_eliminar)
        self.BotonActualizar.clicked.connect(self.go_actualizar)
        
        self.show()

    def go_back(self):
        self.ventana_anterior.show()    
        self.destroy()      

    def go_crear(self):
        self.ventana_crear = CrearExposicion(ventana_anterior=self)
        self.ventana_crear.setCoordinador(self.coordinador)
        self.ventana_crear.show()
        self.hide()

    def go_eliminar(self):
        self.ventana_eliminar = EliminarExposiciones(ventana_anterior=self)
        self.ventana_eliminar.setCoordinador(self.coordinador)
        self.ventana_eliminar.show()
        self.hide()

    def go_actualizar(self):
        self.ventana_actualizar = ActualizarExposicion(ventana_anterior=self)
        self.ventana_actualizar.setCoordinador(self.coordinador)
        self.ventana_actualizar.show()
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

