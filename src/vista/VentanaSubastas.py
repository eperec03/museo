import os
import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\src')
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy, QApplication, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSlot
from controlador.coordinador import Coordinador
from modelo.logica import Logica

class VentanaSubastas(QtWidgets.QMainWindow):
    def __init__(self, controlador=None, ventana_anterior=None):
        super().__init__()
        uic.loadUi('src/vista/ui/VentanaSubastas.ui', self)
        self.setWindowTitle("SUBASTAS")
        self.setWindowIcon(QIcon('src/vista/Imagenes/logomuseo.png'))
        self.ventana_anterior = ventana_anterior
        # Almacena una referencia al controlador
        self.coordinador = controlador
        self.BotonAtras.clicked.connect(self.go_back)
        # Llama al método para crear la tabla y configurar la interfaz de usuario
        self.initUI()

    def setCoordinador(self, coord) -> None:
        self.coordinador = coord

    def go_back(self):
        self.ventana_anterior.show()
        self.destroy()

    def initUI(self):
        # Crear una tabla
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(3)

        # Añadir títulos a las columnas
        self.tableWidget.setHorizontalHeaderLabels(["Título", "Descripción", "Fecha"])

        subastas = self.coordinador.obtener_todos_subastas()
        print(f"Fetched {len(subastas)} objects from the database.")
        self.tableWidget.setRowCount(len(subastas))
        layout = QVBoxLayout()

        for row_index, subasta in enumerate(subastas):
            Titulo = subasta.getTitulo()
            Fecha = subasta.getFecha()
            Descripcion = subasta.getDescripcion()

            # Crear widgets de QLabel para Título y Descripción
            titulo_item = QTableWidgetItem(Titulo)
            descripcion_item = QTableWidgetItem(Descripcion)
            fecha_item = QTableWidgetItem(Fecha)

            self.tableWidget.setItem(row_index, 0, titulo_item)
            self.tableWidget.setItem(row_index, 1, descripcion_item)
            self.tableWidget.setItem(row_index, 2, fecha_item)


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
        self.tableWidget.setMinimumSize(1000, 500)
        self.tableWidget.setMaximumSize(1500, 500)

        # Ajustar el tamaño de las filas
        self.tableWidget.verticalHeader().setDefaultSectionSize(100)

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
                border: 2px solid rgb(255, 250, 255);  
                border-radius: 15px;  
                background-color: rgb(67, 157, 175);
                gridline-color: #DADADA;
            }
            QHeaderView::section {
                background-color: rgb(67, 157, 175); 
                color: #333333;
                padding: 4px;
                border: 1px solid rgb(255, 250, 255); 
            }
            QTableWidget::item {
                padding: 5px;
                border: none;
                background-color: rgb(250, 255, 255);  
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

    @staticmethod
    def mostrar_advertencia(ex):
        mensaje = QMessageBox()
        mensaje.setIcon(QMessageBox.Warning)
        mensaje.setText("Error")
        mensaje.setInformativeText(str(ex))
        mensaje.setWindowTitle("Advertencia")
        mensaje.exec()
