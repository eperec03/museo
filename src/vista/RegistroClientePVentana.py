import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\src')

import tkinter as tk
from tkinter import messagebox
from modelo.vo.UsuariosVO import ClientePremiumVO
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon

class RegistroClientePVentana(QtWidgets.QMainWindow):
    def __init__(self, controlador = None, ventana_anterior=None):
        # Importamos el .ui
        super(RegistroClientePVentana, self).__init__()
        uic.loadUi('src/vista/ui/RegistroCliP.ui', self)
        self.setWindowTitle("REGISTRO DE CLIENTE PREMIUM")
        self.setWindowIcon(QIcon('src/vista/Imagenes/logomuseo.png'))  # Reemplaza con la ruta a tu logo
        # Almacena una referencia al controlador
        self.coordinador = controlador
        # "EnviarBoton" es el nombre que se le ha dado al objeto en el .ui
        self.enviarBoton.clicked.connect(self.registrarPersona)
        self.ventana_anterior=ventana_anterior
        self.BotonAtras.clicked.connect(self.go_back)

    def go_back(self):
        self.ventana_anterior.show()
        self.destroy()

    def setCoordinador(self, coord) -> None:
        self.coordinador = coord

    def limpiar(self):
        self.lineDni.clear()
        self.lineNombre.clear()
        self.lineTfno.clear()
        self.lineEmail.clear()
        self.lineTitular.clear()
        self.lineNumTarj.clear()
        self.lineCvv.clear()
        self.lineCad.clear()
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

    def registrarPersona(self) -> None:
        try:
            persona = ClientePremiumVO(
                DNI = self.lineDni.text(),
                UsuNombreCompleto = self.lineNombre.text(),
                Usutfno = self.lineTfno.text(),
                UsuEmail = self.lineEmail.text(),
                UsuTitularMP = self.lineTitular.text(), 
                UsuNumTarjMP = self.lineNumTarj.text(),
                UsuCvvMP = self.lineCvv.text(), 
                UsuCadMP = self.lineCad.text(), 
                UsuContrasenna = self.lineContrasenna.text(), 
            )
            self.coordinador.registrarUsuario(persona)
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
