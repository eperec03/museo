import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\src')

import tkinter as tk
from tkinter import messagebox
from modelo.vo.ObjetosVO import ObjetosVO
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon

class ActualizarObjeto(QtWidgets.QMainWindow):
    def __init__(self, controlador = None, ventana_anterior=None):
        # Importamos el .ui
        super().__init__()
        uic.loadUi('src/vista/ui/ActualizarObjetos.ui', self)
        self.setWindowTitle("ACTUALIZAR OBJETOS")
        self.setWindowIcon(QIcon('src/vista/Imagenes/logomuseo.png'))  # Reemplaza con la ruta a tu logo
        # Almacena una referencia al controlador
        self.coordinador = controlador
        # "EnviarBoton" es el nombre que se le ha dado al objeto en el .ui
        self.BotonEditarObjeto.clicked.connect(self.actualizarObjeto)
        self.ventana_anterior=ventana_anterior
        self.BotonAtras.clicked.connect(self.go_back)

    def go_back(self):
        self.ventana_anterior.show()
        self.destroy()

    def setCoordinador(self, coord) -> None:
        self.coordinador = coord

    def limpiar(self):
        self.IDObjeto_entrada.clear()
        self.NombreObjeto_entrada.clear()
        self.Imagen_entrada.clear()
        self.Precio_entrada.clear()
        self.Tipo_entrada.clear()
        self.Inspiracion_entrada.clear()
        self.Existencias_entrada.clear()
        self.Agotado_entrada.clear()
        self.IDCatalogo_entrada.clear()

    def actualizarObjeto(self) -> None:
        try:
            Objeto = ObjetosVO(
                IDObjeto = self.IDObjeto_entrada.text(),
                NombreObjeto = self.NombreObjeto_entrada.text(),
                Imagen = self.Imagen_entrada.text(),
                FechaNac = self.Precio_entrada.text(),
                Tipo = self.Tipo_entrada.text(), 
                Inspiracion = self.Inspiracion_entrada.text(),
                Existencias = self.Existencias_entrada.text(),
                Agotado = self.Tipo_entrada.text(), 
                IdCatalogo = self.IDCatalogo_entrada.text()
                )
            self.coordinador.actualizarObjeto(Objeto)
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
