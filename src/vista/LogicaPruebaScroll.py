import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('src/vista/ui/PruebaScroll.ui', self)
        self.setupUi(self)
        self.load_data()

        # Conectar el botón de refrescar a la función
        self.refreshButton.clicked.connect(self.refresh_data)

    def load_data(self):
        # Conectar a la base de datos SQLite
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


    def refresh_data(self):
        # Limpiar el layout actual
        for i in reversed(range(self.scrollAreaWidgetContents.layout().count())):
            self.scrollAreaWidgetContents.layout().itemAt(i).widget().setParent(None)

        # Recargar los datos
        self.load_data()




