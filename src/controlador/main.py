# En el cmd de Anaconda: pip install pyqt5
# Una vez isntalado en C:\Users\"user"\anaconda3\Library\bin executamos el designer.exe
# Para abrir un nuevo proyecto: Archivo -> Nuevo -> main Windows
# Arriba a la derecha borramos todo menos el central widget
# guardamos la ventana en la carpeta vista
import sys
ruta_modulo = r'ruta'
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')

from vista.RegistroUsuarioVentana import RegistroUsuarioVentana
from controlador.coordinador import Coordinador
from modelo.logica import Logica


if __name__ == "__main__":
    #root = tk.Tk()
    ventanaRegistro = RegistroUsuarioVentana()
    logica = Logica()
    controlador = Coordinador()

    # A cada ventada hay que asignarle un coordinador. Un mismo controlador puede controlar varias ventanas
    ventanaRegistro.setCoordinador(controlador)

    # Al coordinador hay que asignarle una ventana. Un coordinador puede tener referencias a varias ventanas
    controlador.setViewRegistro(ventanaRegistro)

    # Al coordinador también hay que asignarle la lógica del modelo
    controlador.setModel(logica)

    #Para comenzar con la pantalla de inicio: True aparece la pantalla y False la destruye
    ventanaRegistro.setVisible(True)
