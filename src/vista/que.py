from PyQt5.QtWidgets import QWidget, QVBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap, QPalette,QBrush
from PyQt5.uic import loadUi
from PyQt5.QtCore import QFile
class CustomWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.widget = loadUi(r"C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\vista\ui\Principal.ui")  # Cambia la ruta al archivo .ui
                # Establecer imagen de fondo
        bg_image = QPainter(r"C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\vista\Imagenes\foto.jpg")  # Cambia la ruta a tu imagen de fondo
        palette = self.widget.palette()
        brush = QBrush(bg_image)
        palette.setBrush(QPalette.Background, brush)
        self.widget.setAutoFillBackground(True)
        self.widget.setPalette(palette)
        
        # Agregar el widget al diseño
        layout = QVBoxLayout(self)
        layout.addWidget(self.widget)



from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtGui import QMovie, QPalette, QPainter
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtGui import QMovie, QBrush
from PyQt5.QtCore import QTimer

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtGui import QMovie, QBrush
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QMovie

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt

# class CustomWidget(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
        
#         # Establecer el formulario .ui
#         self.widget = loadUi(r"C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\vista\ui\Principal.ui")  # Cambia la ruta al archivo .ui
        
#         # Cargar el GIF como QLabel
#         self.label = QLabel(self)
#         self.label.setAlignment(Qt.AlignCenter)
#         self.label.setScaledContents(True)  # Escalar contenido
        
#         # Establecer el GIF como contenido del QLabel
#         self.movie = QMovie(r"C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\vista\Imagenes\museo.gif")  # Cambia la ruta a tu GIF
#         self.label.setMovie(self.movie)
#         self.movie.start()
        
#         # Configurar el diseño del widget
#         layout = QVBoxLayout(self)
#         layout.addWidget(self.widget)
#         layout.addWidget(self.label)
        
# if __name__ == "__main__":
#     import sys
#     from PyQt5.QtWidgets import QApplication
    
#     app = QApplication(sys.argv)
#     window = CustomWidget()
#     window.show()
#     sys.exit(app.exec_())



        
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    window = CustomWidget()
    window.show()
    sys.exit(app.exec_())
