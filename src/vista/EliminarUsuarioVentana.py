import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src\modelo')

import tkinter as tk
from vo.UserVO import UserVO
from tkinter import messagebox

class EliminarUsuarioVentana:
    def __init__(self, controlador = None):
        # Crea la ventana principal
        self.root = tk.Tk()
        # Almacena una referencia al controlador
        self.coordinador = controlador

        self.dni_label = tk.Label(self.root, text="DNI:")
        self.dni_label.pack()
        self.dni_entry = tk.Entry(self.root)
        self.dni_entry.pack()

        self.boton = tk.Button(self.root, text="Guardar", command=self.eliminarPersona)
        self.boton.pack()

    def limpiar(self):
        self.dni_entry.delete(0, tk.END)

    def setVisible(self, visible: bool) -> None:
        if visible:
            self.root.mainloop()
        else:
            self.root.destroy()

    def setCoordinador(self, coord) -> None:
        self.coordinador = coord

    #############################Listeners##############################

    def eliminarPersona(self) -> None:
        try:
            persona = UserVO(
                DNI = self.dni_entry.get(),
                NombreCompleto=None, Telefono=None, Email=None,
                Titular=None, NumTarjeta=None, Cvv=None, Caducidad=None, Contraseña=None, FechaRegistro=None)
            self.coordinador.eliminarUsuario(persona)

            self.limpiar()
        except Exception as ex:
            messagebox.showwarning("Error", ex)