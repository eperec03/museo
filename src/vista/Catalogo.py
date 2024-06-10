import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')

import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QScrollArea, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import uic
from controlador.coordinador import Coordinador
from modelo.logica import Logica

class VentanaCatalogo(QMainWindow):
    def __init__(self, controlador=None, ventana_anterior=None):
        super(VentanaCatalogo, self).__init__()
        uic.loadUi('src/vista/ui/Catalogo.ui', self)
        self.setWindowTitle("Catalogo")
        self.setWindowIcon(QIcon('src/vista/Imagenes/logomuseo.png'))
        self.coordinador = controlador
        self.ventana_anterior = ventana_anterior
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
        objetos = self.coordinador.obtener_todos_objetos()
        print(f"Fetched {len(objetos)} objects from the database.")

        layout = QVBoxLayout()

        for objeto in objetos:
            NombreObjeto = objeto.getNombreObjeto()
            Imagen = objeto.getImagen()
            Precio = objeto.getPrecio()
            objeto_widget = QWidget()
            objeto_layout = QHBoxLayout()

            if Imagen is not None:
                pixmap = QPixmap(Imagen)
                imagen_label = QLabel()
                imagen_label.setPixmap(pixmap)
                imagen_label.setFixedSize(100, 100)
                imagen_label.setScaledContents(True)

                texto_label = QLabel(f"{NombreObjeto}")
                precio_label = QLabel(f"Precio: ${Precio:.2f}")
                
                texto_label.setStyleSheet("font-size: 16px; font-weight: bold; margin-left: 10px;")
                precio_label.setStyleSheet("font-size: 14px; color: green; margin-left: 10px;")

                boton_info = QPushButton("Más Información")
                boton_info.clicked.connect(lambda _, obj=objeto: self.mostrar_info(obj))
                
                objeto_layout.addWidget(imagen_label)
                objeto_layout.addWidget(texto_label)
                objeto_layout.addWidget(precio_label)
                objeto_layout.addWidget(boton_info)
                objeto_widget.setLayout(objeto_layout)

                layout.addWidget(objeto_widget)
            else:
                print("Error: Image path is None for object:", NombreObjeto)

        self.scrollAreaWidgetContents.setLayout(layout)

    def mostrar_info(self, objeto):
        # Aquí puedes definir qué hacer cuando se haga clic en el botón "Más Información"
        print(f"Mostrando más información sobre el objeto: {objeto.getNombreObjeto()}")

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
    ex = VentanaCatalogo(controlador=c)
    ex.show()
    sys.exit(app.exec_())
