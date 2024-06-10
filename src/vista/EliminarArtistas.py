import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\src')

import tkinter as tk
from tkinter import messagebox
from modelo.vo.ArtistasVO import ArtistasVO
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon

class EliminarArtista(QtWidgets.QMainWindow):
    def __init__(self, controlador = None, ventana_anterior=None):
        # Importamos el .ui
        super().__init__()
        uic.loadUi('src/vista/ui/EliminarArtistas.ui', self)
        self.setWindowTitle("ELIMINAR ARTISTAS")
        self.setWindowIcon(QIcon('src/vista/Descripciones/logomuseo.png'))  # Reemplaza con la ruta a tu logo
        # Almacena una referencia al controlador
        self.coordinador = controlador
        # "EnviarBoton" es el nombre que se le ha dado al objeto en el .ui
        self.BotonEditarArtista.clicked.connect(self.eliminarArtista)
        self.ventana_anterior=ventana_anterior
        self.BotonAtras.clicked.connect(self.go_back)

    def go_back(self):
        self.ventana_anterior.show()
        self.destroy()

    def setCoordinador(self, coord) -> None:
        self.coordinador = coord

    def limpiar(self):
        self.NombreArtista_entrada.clear()

    def eliminarArtista(self) -> None:
        try:
            Artista = ArtistasVO(
                NombreArtista = self.NombreArtista_entrada.text(),
                )
            self.coordinador.eliminarArtistas(Artista)
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
