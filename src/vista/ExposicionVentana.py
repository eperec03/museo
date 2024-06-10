import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\src')
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy, QApplication
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSlot
from controlador.coordinador import Coordinador
from modelo.logica import Logica

class VentanaExposiciones(QtWidgets.QMainWindow):
    def __init__(self, controlador=None):
        super(VentanaExposiciones, self).__init__()
        uic.loadUi('src/vista/ui/VentanaExposiciones.ui', self)
        self.setWindowTitle("EXPOSICIONES")
        self.setWindowIcon(QIcon('src/vista/Imagenes/logomuseo.png'))  

        # Almacena una referencia al controlador
        self.coordinador = controlador

        # Llama al método para crear la tabla y configurar la interfaz de usuario
        self.initUI()

    def initUI(self):
        # Crear una tabla
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(4)  # Aquí tiene que haber el número de exposiciones que haya en la BD

        # Añadir títulos a las columnas
        self.tableWidget.setHorizontalHeaderLabels(["Título", "Descripción", "Imagen"])

        exposiciones = self.coordinador.obtener_todos_exposiciones()
        print(f"Fetched {len(exposiciones)} objects from the database.")

        layout = QVBoxLayout()

        for row_index, exposicion in enumerate(exposiciones):
            Titulo = exposicion.getTitulo()
            Imagen = exposicion.getImagen()
            Descripcion = exposicion.getDescripcion()

            # Crear widgets de QLabel para Título y Descripción
            titulo_item = QTableWidgetItem(Titulo)
            descripcion_item = QTableWidgetItem(Descripcion)

            self.tableWidget.setItem(row_index, 0, titulo_item)
            self.tableWidget.setItem(row_index, 1, descripcion_item)

            if Imagen:
                imagen_label = QLabel()
                pixmap = QPixmap(Imagen)
                imagen_label.setPixmap(pixmap)
                imagen_label.setFixedSize(100, 100)
                imagen_label.setScaledContents(True)
                self.tableWidget.setCellWidget(row_index, 2, imagen_label)
            else:
                print("Error: Image path is None for object:", Titulo)

        # Hace que las celdas no sean editables
        for row in range(self.tableWidget.rowCount()):
            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, column)
                if item is not None:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)

        # Ajustar columnas para llenar el espacio disponible
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Ajustar el tamaño de la tabla
        self.tableWidget.setMinimumSize(1000, 200)
        self.tableWidget.setMaximumSize(1000, 800)

        # Buscar el layout principal definido en el archivo .ui
        central_widget = self.findChild(QtWidgets.QWidget, "centralwidget")
        if not central_widget:
            central_widget = QtWidgets.QWidget(self)
            self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        central_widget.setLayout(main_layout)

        # Añadir espaciadores para centrar verticalmente
        main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Crear un layout horizontal para centrar la tabla
        h_layout = QHBoxLayout()

        # Añadir espacios vacíos a la izquierda y derecha
        h_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        h_layout.addWidget(self.tableWidget)
        h_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Añadir el layout horizontal al layout principal
        main_layout.addLayout(h_layout)

        # Añadir espaciadores para centrar verticalmente
        main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Aplica estilos a la tabla
        self.applyStyles()

    def applyStyles(self):
        self.tableWidget.setStyleSheet("""
            QTableWidget {
                border: 2px solid rgb(208, 223, 232);  
                border-radius: 15px;  
                background-color: rgb(67, 157, 175);
                gridline-color: #DADADA;
            }
            QHeaderView::section {
                background-color: rgb(67, 157, 175); 
                color: #333333;
                padding: 4px;
                border: 1px solid rgb(208, 223, 232); 
            }
            QTableWidget::item {
                padding: 5px;
                border: none;
                background-color: rgb(67, 157, 175);  
                color: #333333;
            }
            QTableWidget::item:selected {
                background-color: rgb(67, 157, 175);
                color: #000000;
            }
        """)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    def setCoordinador(self, coord) -> None:
        self.coordinador = coord

    @staticmethod
    def mostrar_advertencia(ex):
        mensaje = QMessageBox()
        mensaje.setIcon(QMessageBox.Warning)
        mensaje.setText("Error")
        mensaje.setInformativeText(str(ex))
        mensaje.setWindowTitle("Advertencia")
        mensaje.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = Coordinador()
    logica = Logica()
    c.setModel(logica)
    ex = VentanaExposiciones(controlador=c)
    ex.show()  
    sys.exit(app.exec_())
