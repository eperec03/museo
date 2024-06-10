import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\src')

import tkinter as tk
from tkinter import messagebox
from modelo.vo.SalasVO import *
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from vista.ServiciosVentana import *
from vista.SalaVentana import *
from vista.SalaVentana_2 import *


class MapaVentana(QtWidgets.QMainWindow):
    def __init__(self, controlador = None, ventana_anterior=None):
        super(MapaVentana, self).__init__()
        uic.loadUi('src/vista/ui/VentanaMapa.ui', self)
        self.setWindowTitle("MAPA")
        self.setWindowIcon(QIcon('src/vista/Imagenes/logomuseo.png'))  
        self.coordinador = controlador
        # self.enviarBoton.clicked.connect(self.registrarEntrada)
        self.ventana_anterior = ventana_anterior
        self.BotonAtras.clicked.connect(self.go_back)
        self.boton_sala1.clicked.connect(self.go_to_sala1)
        self.mini_sala1.clicked.connect(self.go_to_sala1)
        self.boton_sala2.clicked.connect(self.go_to_sala2)
        self.mini_sala2.clicked.connect(self.go_to_sala2)



    def go_back(self):
        self.ventana_anterior.show()
        self.destroy()

    def go_to_sala1(self):
        self.ventana_servicios = VentanaSala1(controlador=self.coordinador, ventana_anterior=self)
        self.ventana_servicios.setCoordinador(self.coordinador)
        self.ventana_servicios.show()
        self.hide()

    def go_to_sala2(self):
        self.ventana_servicios = VentanaSala2(controlador=self.coordinador, ventana_anterior=self)
        self.ventana_servicios.setCoordinador(self.coordinador)
        self.ventana_servicios.show()
        self.hide()

    def setCoordinador(self, coord) -> None:
        self.coordinador = coord

    def limpiar(self):
        self.lineEntrada.clear()

    # def setVisible(self, visible: bool) -> None:
    #     if visible:
    #         self.root.mainloop()
    #     else:
    #         self.root.destroy()

    # def setCoordinador(self, coord) -> None:
    #     self.coordinador = coord

    #############################Listeners##############################

    def mostrar_advertencia(ex):
        mensaje = QMessageBox()
        mensaje.setIcon(QMessageBox.Warning)
        mensaje.setText("Error")
        mensaje.setInformativeText(str(ex))
        mensaje.setWindowTitle("Advertencia")
        mensaje.exec_()