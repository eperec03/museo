import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')

import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QScrollArea, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import uic
from controlador.coordinador import Coordinador
from modelo.logica import Logica

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
        self.load_data()

    def setCoordinador(self, coord) -> None:
        self.coordinador = coord
        
    def load_data(self):
        obras = self.coordinador.obtener_todas_obras()
        print(f"Fetched {len(obras)} objects from the database.")

        layout = QVBoxLayout()

        for obra in obras:
            artista = self.coordinador.obtener_artista(obra.getIdArtista())
            Titulo = obra.getTitulo()
            Imagen = obra.getImagen()  # Esta debería ser la ruta de la imagen
            print(Imagen)
            NombreArtista = artista.getNombreArtista() if artista else "Desconocido"

            obra_widget = QWidget()
            obra_layout = QHBoxLayout()

            if Imagen is not None:
                # Verificar la ruta de la imagen y tratar de cargar la imagen
                print(f"Trying to load image at path: {Imagen}")
                try:
                    pixmap = QPixmap(Imagen)
                    if pixmap.isNull():
                        print(f"Error: Cannot load image at path: {Imagen}")
                        # Usa una imagen de respaldo si la imagen no se puede cargar
                        Imagen = 'src/vista/Imagenes/placeholder.png'
                        pixmap = QPixmap(Imagen)
                        if pixmap.isNull():
                            print(f"Error: Cannot load placeholder image at path: {Imagen}")
                            continue

                    imagen_label = QLabel()
                    imagen_label.setPixmap(pixmap)
                    imagen_label.setFixedSize(100, 100)
                    imagen_label.setScaledContents(True)

                    texto_label = QLabel(f"Título: {Titulo}")
                    artista_label = QLabel(f"Artista: {NombreArtista}")
                    
                    texto_label.setStyleSheet("font-size: 16px; font-weight: bold; margin-left: 10px;")
                    artista_label.setStyleSheet("font-size: 14px; color: green; margin-left: 10px;")

                    boton_info = QPushButton("Más Información")
                    boton_info.clicked.connect(lambda _, obj=obra: self.mostrar_info(obj))
                    
                    obra_layout.addWidget(imagen_label)
                    obra_layout.addWidget(texto_label)
                    obra_layout.addWidget(artista_label)
                    obra_layout.addWidget(boton_info)
                    obra_widget.setLayout(obra_layout)

                    layout.addWidget(obra_widget)
                except Exception as e:
                    print(f"Exception occurred while loading image: {e}")
            else:
                print("Error: Image path is None for object:", Titulo)

        self.scrollAreaWidgetContents.setLayout(layout)



    def mostrar_info(self, obra):
        # Aquí puedes definir qué hacer cuando se haga clic en el botón "Más Información"
        print(f"Mostrando más información sobre el obra: {obra.getTitulo()}")

    def refresh_data(self):
        layout = self.scrollAreaWidgetContents.layout()
        if layout:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        self.load_data()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = Coordinador()
    logica = Logica()
    c.setModel(logica)
    ex = VentanaSala1(controlador=c)
    ex.show()
    sys.exit(app.exec_())
