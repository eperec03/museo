import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\src')

import tkinter as tk
from tkinter import messagebox
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QTableWidget, QMainWindow, QApplication, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, Qt

class VentanaExposiciones(QtWidgets.QMainWindow):
    def __init__(self, controlador=None):
        super(VentanaSala1, self).__init__()
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
        self.tableWidget.setRowCount(4) #aqui tiene que haber el numero de exposiciones que haya en la bd

        # Añadir títulos a las columnas
        self.tableWidget.setHorizontalHeaderLabels(["Título", "Descripción", "Imagen"])

        exposiciones = self.coordinador.obtener_todos_exposiciones()
        print(f"Fetched {len(exposiciones)} objects from the database.")

        layout = QVBoxLayout()

        for exposicion in exposiciones:
            Titulo = exposicion.getTitulo()
            Imagen = exposicion.getImagen()
            Descripcion = exposicion.getDescripcion()
            # exposicion_widget = QWidget()
            # exposicion_layout = QHBoxLayout()

            if Imagen is not None:
                pixmap = QPixmap(Imagen)
                imagen_label = QLabel()
                imagen_label.setPixmap(pixmap)
                imagen_label.setFixedSize(100, 100)
                imagen_label.setScaledContents(True)

                titulo_label = QLabel(f"{Titulo}")
                descripcion_label = QLabel(f"{Descripcion}")
                
                titulo_label.setStyleSheet("font-size: 16px; font-weight: bold; margin-left: 10px;")
                descripcion_label.setStyleSheet("font-size: 14px; margin-left: 10px;")
                
                self.tableWidget.setItem(exposiciones.index(exposicion), 0, QTableWidgetItem(titulo_label))
                self.tableWidget.setItem(exposiciones.index(exposicion), 1, QTableWidgetItem(descripcion_label))
                self.tableWidget.setItem(exposiciones.index(exposicion), 2, QTableWidgetItem(imagen_label))

                # objeto_layout.addWidget(imagen_label)
                # objeto_layout.addWidget(titulo_label)
                # objeto_layout.addWidget(descripcion_label)
                # objeto_layout.addWidget(boton_info)
                # objeto_widget.setLayout(objeto_layout)

                # layout.addWidget(objeto_widget)
            else:
                print("Error: Image path is None for object:", NombreObjeto)


        # self.tableWidget.setItem(0, 0, QTableWidgetItem("Obra 1"))
        # self.tableWidget.setItem(0, 1, QTableWidgetItem("Descripción 1"))
        # self.tableWidget.setItem(0, 2, QTableWidgetItem("Imagen 1"))
        # self.tableWidget.setItem(1, 0, QTableWidgetItem("Obra 2"))
        # self.tableWidget.setItem(1, 1, QTableWidgetItem("Descripción 2"))
        # self.tableWidget.setItem(1, 2, QTableWidgetItem("Imagen 2"))
        # self.tableWidget.setItem(2, 0, QTableWidgetItem("Obra 3"))
        # self.tableWidget.setItem(2, 1, QTableWidgetItem("Descripción 3"))
        # self.tableWidget.setItem(2, 2, QTableWidgetItem("Imagen 3"))
        # self.tableWidget.setItem(3, 0, QTableWidgetItem("Obra 4"))
        # self.tableWidget.setItem(3, 1, QTableWidgetItem("Descripción 4"))
        # self.tableWidget.setItem(3, 2, QTableWidgetItem("Imagen 4"))

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
        if (central_widget is None):
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
    ex.show()  
    sys.exit(app.exec_())
