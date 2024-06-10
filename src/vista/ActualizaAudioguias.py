import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\src')

import tkinter as tk
from tkinter import messagebox
from modelo.vo.AudioguiasVO import AudioguiasVO
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon

class ActualizarAudioguia(QtWidgets.QMainWindow):
    def __init__(self, controlador = None, ventana_anterior=None):
        # Importamos el .ui
        super().__init__()
        uic.loadUi('src/vista/ui/ActualizarAudioguias.ui', self)
        self.setWindowTitle("ACTUALIZAR AUDIOGUÍAS")
        self.setWindowIcon(QIcon('src/vista/Imagenes/logomuseo.png'))  # Reemplaza con la ruta a tu logo
        # Almacena una referencia al controlador
        self.coordinador = controlador
        # "EnviarBoton" es el nombre que se le ha dado al objeto en el .ui
        self.BotonEditarAudioguia.clicked.connect(self.actualizarAudioguia)
        self.ventana_anterior=ventana_anterior
        self.BotonAtras.clicked.connect(self.go_back)

    def go_back(self):
        self.ventana_anterior.show()
        self.destroy()

    def setCoordinador(self, coord) -> None:
        self.coordinador = coord

    def limpiar(self):
        self.IDAudioguia_entrada.clear()
        self.Titulo_entrada.clear()
        self.IDObra_entrada.clear()
        self.Audio_entrada.clear()
        self.Duracion_entrada.clear()

    def actualizarAudioguia(self) -> None:
        try:
            Audioguia = AudioguiasVO(
                IDAudioguia = self.IDAudioguia_entrada.text(),
                Titulo = self.NombreAudioguia_entrada.text(),
                IDObra = self.IDObra_entrada.text(),
                Audio = self.Audio_entrada.text(),
                Duracion = self.Duracion_entrada.text()
                )
            self.coordinador.actualizarAudioguia(Audioguia)
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