import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\src')

import tkinter as tk
from tkinter import messagebox
from modelo.vo.UsuariosVO import *
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from vista.MenuEditor import *

class InicioEditorVentana(QtWidgets.QMainWindow):
    def __init__(self, controlador = None,ventana_anterior=None):
        # Importamos el .ui
        super(InicioEditorVentana, self).__init__()
        uic.loadUi('src/vista/ui/InicioEditores.ui', self)
        self.setWindowTitle("INICIO DE EDITORES")
        self.setWindowIcon(QIcon('src/vista/Imagenes/logomuseo.png'))  # Reemplaza con la ruta a tu logo
        # Almacena una referencia al controlador
        self.coordinador = controlador
        # "EnviarBoton" es el nombre que se le ha dado al objeto en el .ui
        self.ventana_anterior=ventana_anterior
        self.BotonAtras.clicked.connect(self.go_back)
        self.enviarBoton.clicked.connect(self.validarCliente)
        self.show()

    def go_back(self):
        self.ventana_anterior.show()    
        self.destroy()

    def go_to_window_servicios(self):
        self.ventana_servicios = MenuEditor(ventana_anterior=self)
        self.ventana_servicios.setCoordinador(self.coordinador)
        self.ventana_servicios.show()
        self.hide()        

    def setCoordinador(self, coord) -> None:
        self.coordinador = coord

    def limpiar(self):
        self.lineDni.clear()
        self.lineContrasenna.clear()
        # self.lineFecha.clear()

    # def setVisible(self, visible: bool) -> None:
    #     if visible:
    #         self.root.mainloop()
    #     else:
    #         self.root.destroy()

    # def setCoordinador(self, coord) -> None:
    #     self.coordinador = coord

    #############################Listeners##############################

    def validarEditor(self) -> None:
        try:
            persona = EditorVO(
                DNI = self.lineDni.text(),
                UsuContrasenna = self.lineContrasenna.text(), 
            )
            if self.coordinador.validarEditores(persona) == True:
                self.go_to_window_servicios()
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
