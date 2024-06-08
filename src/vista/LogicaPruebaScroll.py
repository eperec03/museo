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

class ObjetosWindow(QtWidgets.QMainWindow):
    def __init__(self, controlador = None, ventana_anterior = None ):
        super().__init__()
        uic.loadUi('src/vista/ui/PruebaScroll.ui', self)
        self.setWindowTitle("CATALOGO")
        self.setWindowIcon(QIcon('src/vista/Imagenes/logomuseo.png'))  
        self.coordinador = controlador
        
        self.ventana_anterior = ventana_anterior
        self.BotonHome.clicked.connect(self.go_back)

        #self.setupUi(self)
        self.load_data()

    def go_back(self):
        self.ventana_anterior.show()
        self.destroy()

    def setCoordinador(self, coord) -> None:
        self.coordinador = coord

    def load_data(self):
        conexion = self.getConnection()
        conn = None
        cursor = None
        try:
            if conexion:
                conn = conexion
            else:
                # Obtener todas las obras de arte
                cursor.execute('SELECT * FROM objetos')
                obras = cursor.fetchall()

                # Crear un layout para el widget contenedor
                layout = QVBoxLayout()

                # Añadir una etiqueta para cada obra de arte
                for objeto in objetos:
                    IDObjeto, NombreObjeto, Imagen, Precio, Tipo, Inspiracion, Existencias, Agotado, IDCatalogo = objeto
                    # Crear un widget contenedor para la imagen y el texto
                    obra_widget = QWidget()
                    obra_layout = QHBoxLayout()

                    # Añadir la imagen
                    pixmap = QPixmap(Imagen)
                    imagen_label = QLabel()
                    imagen_label.setPixmap(pixmap)
                    imagen_label.setFixedSize(100, 100)  # Ajustar el tamaño de la imagen si es necesario
                    imagen_label.setScaledContents(True)

                    # Añadir el texto
                    texto_label = QLabel(f"{NombreObjeto}")

                    # Añadir imagen y texto al layout del contenedor
                    obra_layout.addWidget(imagen_label)
                    obra_layout.addWidget(texto_label)
                    obra_widget.setLayout(obra_layout)

                    # Añadir el contenedor al layout principal
                    layout.addWidget(obra_widget)

                # Configurar el widget contenedor
                self.scrollAreaWidgetContents.setLayout(layout)

                # Cerrar la conexión
                conn.close()


    def mostrar_advertencia(ex):
        mensaje = QMessageBox()
        mensaje.setIcon(QMessageBox.Warning)
        mensaje.setText("Error")
        mensaje.setInformativeText(str(ex))
        mensaje.setWindowTitle("Advertencia")
        mensaje.exec_()



