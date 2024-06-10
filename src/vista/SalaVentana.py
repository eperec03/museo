import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')

import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QScrollArea, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import uic
from controlador.coordinador import Coordinador
from modelo.logica import Logica
from vista.VisualizarObras import *

class VentanaSala1(QMainWindow):
    def __init__(self, controlador=None, ventana_anterior=None):
        super(VentanaSala1, self).__init__()
        uic.loadUi('src/vista/ui/Sala1.ui', self)
        self.setWindowTitle("Sala 1")
        self.setWindowIcon(QIcon('src/vista/Imagenes/logomuseo.png'))
        self.coordinador = controlador
        try:
            self.scrollArea = self.findChild(QScrollArea, 'scrollArea')
            self.scrollAreaWidgetContents = QWidget()
            self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        except Exception as e:
            print(f"Error finding scroll area or its contents: {e}")
            return
        self.ventana_anterior=ventana_anterior
        self.BotonAtras.clicked.connect(self.go_back)
        self.load_data()

    def go_back(self):
        self.ventana_anterior.show()
        self.destroy()
        
    def setCoordinador(self, coord) -> None:
        self.coordinador = coord
        
    def load_data(self):
        obras = self.coordinador.obtener_todas_obras_1()
        print(f"Fetched {len(obras)} objects from the database.")

        layout = QVBoxLayout()

        for obra in obras:
            artista = self.coordinador.obtener_artista(obra.getIdArtista())
            Titulo = obra.getTitulo()
            Imagen = obra.getImagen()
            NombreArtista = artista.getNombreArtista() if artista else "Desconocido"

            obra_widget = QWidget()
            obra_layout = QHBoxLayout()

            if Imagen is not None:
                pixmap = QPixmap(Imagen)
                imagen_label = QLabel()
                imagen_label.setPixmap(pixmap)
                imagen_label.setFixedSize(100, 100)
                imagen_label.setScaledContents(True)

                texto_label = QLabel(f"Título: {Titulo}")
                artista_label = QLabel(f"Artista: {NombreArtista}")
                
                texto_label.setStyleSheet("font-size: 16px; font-weight: bold; margin-left: 10px;")
                artista_label.setStyleSheet("font-size: 14px; margin-left: 10px;")

                boton_info = QPushButton("Más Información")
                boton_info.clicked.connect(lambda _, obj=obra: self.mostrar_info(obj))
                
                obra_layout.addWidget(imagen_label)
                obra_layout.addWidget(texto_label)
                obra_layout.addWidget(artista_label)
                obra_layout.addWidget(boton_info)
                obra_widget.setLayout(obra_layout)

                layout.addWidget(obra_widget)
            else:
                print("Error: Image path is None for object:", Titulo)

        self.scrollAreaWidgetContents.setLayout(layout)
        self.boton_info.clicked.connect(self.mostrar_info(self.obra))

    def mostrar_info(self, obra):
        self.ventana_obra = VentanaVisualizarObra(ventana_anterior=self)
        self.ventana_obra.setCoordinador(self.coordinador)
        self.ventana_obra.show()
        self.hide()

