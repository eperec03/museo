import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\src')

import tkinter as tk
from tkinter import messagebox
from modelo.vo.ClienteEstandarVO import ClienteEstandarVO
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from vista.ServiciosVentana import *

class RegistroEntradaVentana(QtWidgets.QMainWindow):
    def __init__(self, controlador = None,ventana_anterior=None):
        super(RegistroEntradaVentana, self).__init__()
        uic.loadUi('src/vista/ui/RegistroEntrada.ui', self)
        self.setWindowTitle("REGISTRO SIN CUENTA")
        self.setWindowIcon(QIcon('src/vista/Imagenes/logomuseo.png'))  
        self.coordinador = controlador
        self.enviarBoton.clicked.connect(self.registrarEntrada)
        self.ventana_anterior=ventana_anterior
        self.BotonAtras.clicked.connect(self.go_back)

    def go_back(self):
        self.ventana_anterior.show()
        self.destroy()

    def go_to_ventana_servicios(self):
        self.ventana_servicios = VentanaServicio(ventana_anterior=self)
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

    def registrarEntrada(self) -> None:
        try:
            persona = ClienteEstandarVO(
                NumEntrada = self.lineEntrada.text()
            )
            if self.coordinador.registrarEntrada(persona)==True:
                self.go_to_ventana_servicios()
            self.limpiar()
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
