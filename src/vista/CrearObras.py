import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\src')

import tkinter as tk
from tkinter import messagebox
from modelo.vo.ObrasVO import ObrasVO
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon

class CreaObras(QtWidgets.QMainWindow):
    def __init__(self, controlador = None, ventana_anterior=None):
        # Importamos el .ui
        super().__init__()
        uic.loadUi('src/vista/ui/CrearObras.ui', self)
        self.setWindowTitle("CREAR OBRAS")
        self.setWindowIcon(QIcon('src/vista/Imagenes/logomuseo.png'))  # Reemplaza con la ruta a tu logo
        # Almacena una referencia al controlador
        self.coordinador = controlador
        # "EnviarBoton" es el nombre que se le ha dado al Obra en el .ui
        self.BotonCrearObra.clicked.connect(self.crearObra)
        self.ventana_anterior=ventana_anterior
        self.BotonAtras.clicked.connect(self.go_back)

    def go_back(self):
        self.ventana_anterior.show()
        self.destroy()

    def setCoordinador(self, coord) -> None:
        self.coordinador = coord

    def limpiar(self):
        self.NombreObra_entrada.clear()
        self.Imagen_entrada.clear()
        self.Descripcion_entrada.clear()
        self.Fecha_entrada.clear()
        self.IDArtista_entrada.clear()
        self.NumSala_entrada.clear()

    def crearObra(self) -> None:
        try:
            Obra = ObrasVO(
                Titulo = self.NombreObra_entrada.text(),
                Imagen = self.Imagen_entrada.text(),
                Descripcion = self.Descripcion_entrada.text(),
                Fecha = self.Fecha_entrada.text(), 
                IdArtista = self.IDArtista_entrada.text(),
                NumSala = self.NumSala_entrada.text()
                )
            self.coordinador.crearObras(Obra)
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
