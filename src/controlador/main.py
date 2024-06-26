# En el cmd de Anaconda: pip install pyqt5
# Una vez isntalado en C:\Users\"user"\anaconda3\Library\bin executamos el designer.exe
# Para abrir un nuevo proyecto: Archivo -> Nuevo -> main Windows
# Arriba a la derecha borramos todo menos el central widget
# guardamos la ventana en la carpeta vista
import sys
ruta_modulo = r'ruta'
sys.path.append(r'C:\Users\eripe\Downloads\EntregaFinal\museo\src')
# sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src')
# sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museo\src')

from PyQt5 import QtWidgets, uic

from vista.InicioVentana import *

from controlador.coordinador import Coordinador
from modelo.logica import Logica


if __name__ == "__main__":
    #root = tk.Tk()
    app = QtWidgets.QApplication(sys.argv)
    # ventanaRegistro = RegistroClientePVentana()
    # ventanaRegistroEntrada = RegistroEntradaVentana()
    logica = Logica()
    controlador = Coordinador()
    controlador.setModel(logica)
    ventanaInicio = InicioVentana(controlador=controlador)
    ventanaInicio.setCoordinador(controlador)
    # ventanaEliminarUsuario = EliminarUsuarioVentana()
    # ventanaActualizarUsuario = ActualizarUsuarioVentana()
    ##################################################################################################################
    #TODAVIA NO LE HE PUESTO QUE SE VEAN LAS VENTANAS DE ELIMINAR Y ACTUALIZAR, HAY QUE IRLAS CAMBIANDO PARA PROBARLAS
    ##################################################################################################################

    # A cada ventana hay que asignarle un coordinador. Un mismo controlador puede controlar varias ventanas
    # ventanaRegistro.setCoordinador(controlador)
    # ventanaRegistroEntrada.setCoordinador(controlador)

    # ventanaEliminarUsuario.setCoordinador(controlador)
    # ventanaActualizarUsuario.setCoordinador(controlador)

    # Al coordinador hay que asignarle una ventana. Un coordinador puede tener referencias a varias ventanas
    # controlador.setViewRegistro(ventanaRegistro)
    # controlador.setViewRegistro(ventanaRegistroEntrada)
    controlador.setViewInicio(ventanaInicio)

    # controlador.setViewRegistro(ventanaEliminarUsuario)


    # Al coordinador también hay que asignarle la lógica del modelo

    #Para comenzar con la pantalla de inicio: True aparece la pantalla y False la destruye
    # ventanaRegistro.setVisible(True)
    # ventanaRegistroEntrada.setVisible(True)
    # ventanaEliminarUsuario.setVisible(True)
    # ventanaInicio.setVisible(True)
    sys.exit(app.exec_())