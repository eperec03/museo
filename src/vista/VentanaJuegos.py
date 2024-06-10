import sys
# #sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\src')
import os

import subprocess
import tkinter as tk
from tkinter import messagebox
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from vista.MapaVentana import *
from modelo.vo.JuegosVO import *
from modelo.vo.ObrasVO import *

paths = [
    r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\vista\JuegoSerpiente.py',
    r'C:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src\vista\JuegoSerpiente.py'
]

class VentanaJuegos(QtWidgets.QMainWindow):
    def __init__(self, controlador = None, ventana_anterior=None):
        # Importamos el .ui
        super(VentanaJuegos, self).__init__()
        uic.loadUi('src/vista/ui/VentanaJuegos.ui', self)
        self.setWindowTitle("Museo: ")
        self.setWindowIcon(QIcon('src/vista/Imagenes/logomuseo.png'))  # Reemplaza con la ruta a tu logo
        # Almacena una referencia al controlador
        self.coordinador = controlador
        # "EnviarBoton" es el nombre que se le ha dado al objeto en el .ui
        # self.enviarBotonJuego1.clicked.connect(self.go_to_snake)
        self.botonJugar.clicked.connect(self.validar_juego)
        # self.BotonInicioS.clicked.connect(self.go_to_window_inicio)
        self.ventana_anterior=ventana_anterior
        self.BotonAtras.clicked.connect(self.go_back)

    def go_back(self):
        self.ventana_anterior.show()
        self.destroy()

    def go_to_snake(self, ruta):
        subprocess.run(["python", ruta])

    # def go_to_window_inicio(self):
    #     self.ventana_inicio = ElegirUsuario()
    #     self.ventana_inicio.setCoordinador(self.coordinador)
    #     self.ventana_inicio.show()
    #     self.hide()       

    def setCoordinador(self, coord) -> None:
        self.coordinador = coord

    #############################Listeners##############################


    def validar_juego(self) -> None:
        try:
            juegos = JuegosObrasVO(
                Nombre = self.lineNombre.text(),
            )
            obra = ObrasVO(
                Titulo = self.lineObra.text(),
            )
            a = self.coordinador.validarJuego(juegos, obra)
            if a is not None:           
                self.go_to_snake(ruta=a)
                    
        except Exception as ex:
            print(ex)
            self.mostrar_advertencia(ex)


    def mostrar_advertencia(ex):
        mensaje = QMessageBox()
        mensaje.setIcon(QMessageBox.Warning)
        mensaje.setText("Error")
        mensaje.setInformativeText(str(ex))
        mensaje.setWindowTitle("Advertencia")
        mensaje.exec_()