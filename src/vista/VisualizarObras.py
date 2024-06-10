import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QScrollArea, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import uic
from controlador.coordinador import Coordinador
from modelo.logica import Logica

class VentanaVisualizarObra(QMainWindow):
    def __init__(self, controlador=None, ventana_anterior=None, obra=None):
        super().__init__()
        uic.loadUi('src/vista/ui/VisualizarObras.ui', self)
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
        self.obra=obra

    def go_back(self):
        self.ventana_anterior.show()
        self.destroy()
        
    def setCoordinador(self, coord) -> None:
        self.coordinador = coord
        
    def load_data(self):
        layout = QVBoxLayout()

        artista = self.coordinador.obtener_artista(self.obra.getIdArtista())

        Titulo = self.obra.getTitulo()
        Imagen = self.obra.getImagen()
        Descripcion = self.obra.getDescripcion()
        Fecha = self.obra.getFecha()
        NombreArtista = artista.getNombreArtista() if artista else "Desconocido"
        DescripcionArt = artista.getDescripcion()

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
            desc1_label = QLabel(f"Cuadro: {Descripcion}")
            desc2_label = QLabel(f"Info artista: {DescripcionArt}")
            fecha_label = QLabel(f"Fecha cuadro: {Fecha}")
            
            texto_label.setStyleSheet("font-size: 16px; font-weight: bold; margin-left: 10px;")
            artista_label.setStyleSheet("font-size: 14px; margin-left: 10px;")
            desc1_label.setStyleSheet("font-size: 14px; margin-left: 10px;")
            desc2_label.setStyleSheet("font-size: 14px; margin-left: 10px;")
            fecha_label.setStyleSheet("font-size: 14px; margin-left: 10px;")

            boton_info = QPushButton("Más Información")
            boton_info.clicked.connect(lambda _, obj=self.obra: self.mostrar_info(obj))
            
            obra_layout.addWidget(imagen_label)
            obra_layout.addWidget(texto_label)
            obra_layout.addWidget(artista_label)
            obra_layout.addWidget(desc1_label)
            obra_layout.addWidget(desc2_label)
            obra_layout.addWidget(fecha_label)
            obra_widget.setLayout(obra_layout)

            layout.addWidget(obra_widget)
        else:
            print("Error: Image path is None for object:", Titulo)
            
        self.scrollAreaWidgetContents.setLayout(layout)


