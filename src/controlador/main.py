# En el cmd de Anaconda: pip install pyqt5
# Una vez isntalado en C:\Users\"user"\anaconda3\Library\bin executamos el designer.exe
# Para abrir un nuevo proyecto: Archivo -> Nuevo -> main Windows
# Arriba a la derecha borramos todo menos el central widget
# guardamos la ventana en la carpeta vista
import sys
ruta_modulo = r'ruta'
#sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src')

from PyQt5 import QtWidgets, uic

from vista.RegistroClientePVentana import *
from vista.ActualizarUsuarioVentana import *
from vista.EliminarUsuarioVentana import *

from controlador.coordinador import Coordinador
from modelo.logica import Logica


if __name__ == "__main__":
    #root = tk.Tk()
    app = QtWidgets.QApplication(sys.argv)
    ventanaRegistro = RegistroClientePVentana()
    # ventanaEliminarUsuario = EliminarUsuarioVentana()
    # ventanaActualizarUsuario = ActualizarUsuarioVentana()
    ##################################################################################################################
    #TODAVIA NO LE HE PUESTO QUE SE VEAN LAS VENTANAS DE ELIMINAR Y ACTUALIZAR, HAY QUE IRLAS CAMBIANDO PARA PROBARLAS
    ##################################################################################################################
    logica = Logica()
    controlador = Coordinador()

    # A cada ventana hay que asignarle un coordinador. Un mismo controlador puede controlar varias ventanas
    ventanaRegistro.setCoordinador(controlador)
    # ventanaEliminarUsuario.setCoordinador(controlador)
    # ventanaActualizarUsuario.setCoordinador(controlador)

    # Al coordinador hay que asignarle una ventana. Un coordinador puede tener referencias a varias ventanas
    controlador.setViewRegistro(ventanaRegistro)
    # controlador.setViewRegistro(ventanaEliminarUsuario)


    # Al coordinador también hay que asignarle la lógica del modelo
    controlador.setModel(logica)

    #Para comenzar con la pantalla de inicio: True aparece la pantalla y False la destruye
    ventanaRegistro.setVisible(True)
    # ventanaEliminarUsuario.setVisible(True)
    sys.exit(app.exec_())