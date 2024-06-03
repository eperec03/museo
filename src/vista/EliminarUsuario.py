# import tkinter as tk
# from src.modelo.vo.UserVO import UserVO
# from tkinter import messagebox

# class EliminarUsuarioVentana:
#     def __init__(self, controlador = None):
#         # Crea la ventana principal
#         self.root = tk.Tk()
#         # Almacena una referencia al controlador
#         self.coordinador = controlador
#         self.dni_label = tk.Label(self.root, text="Id:")
#         self.dni_label.pack()
#         self.dni_entry = tk.Entry(self.root)
#         self.dni_entry.pack()


#         self.boton = tk.Button(self.root, text="Borrar", command=self.eliminarPersona)
#         self.boton.pack()


#     def limpiar(self):
#         self.id_entry.delete(0, tk.END)


#     def setVisible(self, visible: bool) -> None:
#         if visible:
#             self.root.mainloop()
#         else:
#             self.root.destroy()


#     def setCoordinador(self, coord) -> None:
#         self.coordinador = coord

# #############################Listeners##############################


#     # def registrarPersona(self) -> None:
#     #     try:
#     #         persona = UserVO(
#     #             idUser =  int(self.dni_entry.get()),
#     #         )
#     #         self.coordinador.eliminarUsuario(persona)
#     #         self.limpiar()
#     #     except Exception as ex:
#     #         messagebox.showwarning("Error", ex)
