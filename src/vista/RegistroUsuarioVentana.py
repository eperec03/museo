import sys
#sys.path.append(r'C:\Users\eripe\OneDrive\Documentos\ERI ULE\2º\SEGUNDO CUATRI\IS\PROYECTO\src\modelo')
sys.path.append(r'c:\Users\clara\Documents\2ºUNI\2CUATRI\IS\museoTrabajo\src\modelo')

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

        self.numTarj_label = tk.Label(self.root, text="Numero Tarjeta:")
        self.numTarj_label.pack()
        self.numTarj_entry = tk.Entry(self.root)
        self.numTarj_entry.pack()

        self.cvv_label = tk.Label(self.root, text="Cvv:")
        self.cvv_label.pack()
        self.cvv_entry = tk.Entry(self.root)
        self.cvv_entry.pack()

        self.cad_label = tk.Label(self.root, text="Fecha Caducidad:")
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
        self.dni_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.tfno_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.titular_entry.delete(0, tk.END)
        self.numTarj_entry.delete(0, tk.END)
        self.cvv_entry.delete(0, tk.END)
        self.cad_entry.delete(0, tk.END)
        self.contrasenna_entry.delete(0, tk.END)
        self.fecha_entry.delete(0, tk.END)

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
                DNI = self.dni_entry.get(),
                NombreCompleto = self.nombre_entry.get(),
                Telefono = self.tfno_entry.get(),
                Email = self.email_entry.get(),
                Titular = self.titular_entry.get(), 
                NumTarjeta = self.numTarj_entry.get(),
                Cvv = self.cvv_entry.get(), 
                Caducidad = self.cad_entry.get(), 
                Contraseña = self.contrasenna_entry.get(), 
                FechaRegistro = self.fecha_entry.get()
            )
            self.coordinador.registrarUsuario(persona)
            self.limpiar()
        except Exception as ex:
            messagebox.showwarning("Error", ex)