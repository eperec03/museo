import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\src')

import tkinter as tk
from tkinter import messagebox
from modelo.vo.JuegosVO import JuegosVO
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon

class ActualizarJuego(QtWidgets.QMainWindow):
    def __init__(self, controlador = None, ventana_anterior=None):
        # Importamos el .ui
        super().__init__()
        uic.loadUi('src/vista/ui/ActualizarJuegos.ui', self)
        self.setWindowTitle("ACTUALIZAR JUEGOS")
        self.setWindowIcon(QIcon('src/vista/Imagenes/logomuseo.png'))  # Reemplaza con la ruta a tu logo
        # Almacena una referencia al controlador
        self.coordinador = controlador
        # "EnviarBoton" es el nombre que se le ha dado al objeto en el .ui
        self.BotonEditarJuego.clicked.connect(self.actualizarJuego)
        self.ventana_anterior=ventana_anterior
        self.BotonAtras.clicked.connect(self.go_back)

    def go_back(self):
        self.ventana_anterior.show()
        self.destroy()

    def setCoordinador(self, coord) -> None:
        self.coordinador = coord

    def limpiar(self):
        self.IDJuego_entrada.clear()
        self.Nombre_entrada.clear()
        self.Descripcion_entrada.clear()
        self.Dificultad_entrada.clear()
        self.Ruta_entrada.clear()

    def actualizarJuego(self) -> None:
        try:
            Juego = JuegosVO(
                IDJuego = self.IDJuego_entrada.text(),
                Nombre = self.Nombre_entrada.text(),
                Descripcion = self.Descripcion_entrada.text(),
                Dificultad = self.Dificultad_entrada.text(),
                ruta = self.Ruta_entrada.text()
                )
            self.coordinador.actualizarJuegos(Juego)
            self.limpiar()
        except Exception as ex:
            print(ex)
            self.mostrar_advertencia(ex)

    def mostrar_advertencia(ex):
        mensaje = QMessageBox()
        mensaje.setIcon(QMessageBox.warning)
        mensaje.setText("Error")
        mensaje.setInformativeText(str(ex))
        mensaje.setWindowTitle("Advertencia")
        mensaje.exec_()
