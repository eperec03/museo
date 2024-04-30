import sys
sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')

import tkinter as tk
from vo.UserVO import UserVO
from tkinter import messagebox

class RegistroUsuarioVentana:
    def __init__(self, controlador = None):
        # Crea la ventana principal
        self.root = tk.Tk()
        # Almacena una referencia al controlador
        self.coordinador = controlador

        self.dni_label = tk.Label(self.root, text="DNI:")
        self.dni_label.pack()
        self.dni_entry = tk.Entry(self.root)
        self.dni_entry.pack()

        self.nombre_label = tk.Label(self.root, text="Nombre Completo:")
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(self.root)
        self.nombre_entry.pack()

        self.tfno_label = tk.Label(self.root, text="Teléfono:")
        self.tfno_label.pack()
        self.tfno_entry = tk.Entry(self.root)
        self.tfno_entry.pack()

        self.email_label = tk.Label(self.root, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()

        self.titular_label = tk.Label(self.root, text="Titular:")
        self.titular_label.pack()
        self.titular_entry = tk.Entry(self.root)
        self.titular_entry.pack()

        self.cvv_label = tk.Label(self.root, text="Cvv:")
        self.cvv_label.pack()
        self.cvv_entry = tk.Entry(self.root)
        self.cvv_entry.pack()

        self.cad_label = tk.Label(self.root, text="Cad:")
        self.cad_label.pack()
        self.cad_entry = tk.Entry(self.root)
        self.cad_entry.pack()

        self.contrasenna_label = tk.Label(self.root, text="Contraseña:")
        self.contrasenna_label.pack()
        self.contrasenna_entry = tk.Entry(self.root)
        self.contrasenna_entry.pack()

        self.fecha_label = tk.Label(self.root, text="Fecha:")
        self.fecha_label.pack()
        self.fecha_entry = tk.Entry(self.root)
        self.fecha_entry.pack()

        self.boton = tk.Button(self.root, text="Guardar", command=self.registrarPersona)
        self.boton.pack()

    def limpiar(self):
        self.id_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def setVisible(self, visible: bool) -> None:
        if visible:
            self.root.mainloop()
        else:
            self.root.destroy()

    def setCoordinador(self, coord) -> None:
        self.coordinador = coord

    #############################Listeners##############################

    def registrarPersona(self) -> None:
        try:
            persona = UserVO(
                idUser = self.id_entry.get(),
                nombre = self.nombre_entry.get(),
                email = self.email_entry.get()
            )
            self.coordinador.registrarUsuario(persona)
            self.limpiar()
        except Exception as ex:
            messagebox.showwarning("Error", ex)