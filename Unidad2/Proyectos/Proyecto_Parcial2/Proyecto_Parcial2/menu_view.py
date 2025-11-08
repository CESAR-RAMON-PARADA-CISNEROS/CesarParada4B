import tkinter as tk
from tkinter import messagebox
from user_view import UserApp
from products_view import productosApp

class MenuApp:
    def __init__(self, username):
        self.username = username
        self.root = tk.Tk()
        self.root.title("Menú principal")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.crear_elementos()
        self.root.mainloop()

    def crear_elementos(self):
        tk.Label(self.root, text=f"Bienvenido, {self.username}", font=("Arial", 14, "bold")).pack(pady=20)

        tk.Button(self.root, text="👤 Usuarios", width=20, command=self.abrir_usuarios).pack(pady=10)
        tk.Button(self.root, text="📦 Productos", width=20, command=self.abrir_productos).pack(pady=10)
        tk.Button(self.root, text="🚪 Cerrar sesión", width=20, bg="#dc3545", fg="white", command=self.cerrar_sesion).pack(pady=30)

    def abrir_usuarios(self):
        self.root.destroy()
        UserApp(self.username)

    def abrir_productos(self):
        self.root.destroy()
        productosApp(self.username)

    def cerrar_sesion(self):
        """Pide confirmación antes de cerrar sesión y regresa a la ventana de Login."""
        
        # IMPORTACIÓN LOCAL: Rompe la dependencia circular
        from login_view import LoginApp 
        
        confirmar = messagebox.askyesno(
            "Cerrar Sesión",
            "¿Está seguro de que desea cerrar la sesión actual?",
            parent=self.root 
        )

        if confirmar:
            self.root.destroy()
            new_root = tk.Tk()
            LoginApp(new_root)
            new_root.mainloop()
