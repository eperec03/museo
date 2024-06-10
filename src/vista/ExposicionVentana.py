import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\src')

import tkinter as tk
from tkinter import messagebox
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QTableWidget, QMainWindow, QApplication, QWidget, QAction, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QHeaderView, QLabel, QScrollArea
from PyQt5.QtGui import QIcon
from vista.MapaVentana import *
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, Qt

class VentanaSala1(QtWidgets.QMainWindow):
    def __init__(self, controlador=None):
        super(VentanaSala1, self).__init__()
        uic.loadUi('src/vista/ui/Sala1.ui', self)
        self.setWindowTitle("Museo: ")
        self.setWindowIcon(QIcon('src/vista/Imagenes/logomuseo.png'))  

        # Almacena una referencia al controlador
        self.coordinador = controlador

        # Llama al método para crear la tabla y configurar la interfaz de usuario
        self.initUI()

    def initUI(self):
        # Crear una tabla
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(4)

        # Añadir títulos a las columnas
        self.tableWidget.setHorizontalHeaderLabels(["Obra", "Descripción", "Imagen"])

        self.tableWidget.setItem(0, 0, QTableWidgetItem("Obra 1"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Descripción 1"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Imagen 1"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Obra 2"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("Descripción 2"))
        self.tableWidget.setItem(1, 2, QTableWidgetItem("Imagen 2"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Obra 3"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("Descripción 3"))
        self.tableWidget.setItem(2, 2, QTableWidgetItem("Imagen 3"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("Obra 4"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("Descripción 4"))
        self.tableWidget.setItem(3, 2, QTableWidgetItem("Imagen 4"))

        # Hace que las celdas no sean editables
        for row in range(self.tableWidget.rowCount()):
            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, column)
                if item is not None:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)

        # Ajustar columnas para llenar el espacio disponible
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        # Ajustar el tamaño de la tabla
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 100, 100))

        # Envolver la tabla en un QScrollArea para hacerla scrollable
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.tableWidget)
        scroll_area.setMinimumSize(400, 200)
        scroll_area.setGeometry(0, 0, 100, 100)


        # Buscar el layout principal definido en el archivo .ui
        central_widget = self.findChild(QtWidgets.QWidget, "centralwidget")
        if central_widget is None:
            central_widget = QtWidgets.QWidget(self)
            self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout(central_widget)
        central_widget.setLayout(layout)

        # Agregar etiquetas (o cualquier otro widget) si las tienes
        label1 = QLabel("Etiqueta 1", self)
        layout.addWidget(label1)

        label2 = QLabel("Etiqueta 2", self)
        layout.addWidget(label2)

        # Añadir el QScrollArea al layout
        layout.addWidget(scroll_area)

        # Aplica estilos a la tabla
        self.applyStyles()

    def applyStyles(self):
        self.tableWidget.setStyleSheet("""
            QTableWidget {
                border: 2px solid #DAA520;  /* Color dorado */
                border-radius: 15px;  /* Bordes redondeados */
                background-color: #F0F0F0;
                gridline-color: #DADADA;
            }
            QHeaderView::section {
                background-color: #FFD700;  /* Color oro suave */
                color: #333333;
                padding: 4px;
                border: 1px solid #DAA520;  /* Color dorado */
            }
            QTableWidget::item {
                padding: 5px;
                border: none;
                background-color: #FFF8DC;  /* Color oro suave */
                color: #333333;
            }
            QTableWidget::item:selected {
                background-color: #B0C4DE;
                color: #000000;
            }
        """)

    # Slot para manejar la señal doubleClicked
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    def go_to_window_mapa(self):
        self.ventana_registro = MapaVentana()
        self.ventana_registro.setCoordinador(self.coordinador)
        self.ventana_registro.show()
        self.hide()

    def setCoordinador(self, coord) -> None:
        self.coordinador = coord

    #############################Listeners##############################

    def mostrar_advertencia(ex):
        mensaje = QMessageBox()
        mensaje.setIcon(QMessageBox.Warning)
        mensaje.setText("Error")
        mensaje.setInformativeText(str(ex))
        mensaje.setWindowTitle("Advertencia")
        mensaje.exec

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VentanaSala1()
    ex.show()  # ¡Asegúrate de mostrar la ventana!
    sys.exit(app.exec_())
