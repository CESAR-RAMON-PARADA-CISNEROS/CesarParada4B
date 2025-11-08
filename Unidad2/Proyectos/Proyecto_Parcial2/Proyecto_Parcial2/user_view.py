import tkinter as tk
from tkinter import messagebox, ttk
# ELIMINAMOS: from login_view import LoginApp  <-- Esto causaba el error
from user_controller import ver_usuarios, agregar_usuarios, actualizar_usuarios, eliminar_usuarios

class UserApp:
    def __init__(self, username):
        self.username = username 
        self.root = tk.Tk()
        self.root.title(f"Bienvenido {username}")
        self.root.geometry("800x450")
        self.root.resizable(True, True)

        self.crear_elementos()
        self.cargar_usuarios()
        self.root.mainloop()

    def crear_elementos(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Marco de Botones (Izquierda - Vertical)
        frame_botones_lateral = tk.Frame(main_frame, width=150)
        frame_botones_lateral.pack(side="left", fill="y", padx=(0, 15))
        frame_botones_lateral.pack_propagate(False)

        tk.Label(frame_botones_lateral, text=f"Hola, {self.username}", 
                 font=("Arial", 12, "bold"), anchor="w").pack(fill="x", pady=(0, 15))

        tk.Button(frame_botones_lateral, text="➕ Agregar usuario", 
                  command=self.agregar_usuario, width=15).pack(pady=5)

        tk.Button(frame_botones_lateral, text="🔄 Actualizar usuario", 
                  command=self.actualizar_usuario, width=15).pack(pady=5)

        tk.Button(frame_botones_lateral, text="❌ Eliminar usuario", 
                  command=self.eliminar_usuario, width=15).pack(pady=5)
        
        tk.Button(frame_botones_lateral, text="🔃 Recargar lista", 
                  command=self.cargar_usuarios, width=15).pack(pady=15)

        tk.Button(frame_botones_lateral, text="🚪 Regresar al menu", 
                  command=self.cerrar_sesion, width=15).pack(side="bottom", pady=(10, 0))


        # Marco de Contenido (Derecha - Tabla)
        frame_contenido = tk.Frame(main_frame)
        frame_contenido.pack(side="right", fill="both", expand=True)

        tk.Label(frame_contenido, text="Lista de Usuarios", 
                 font=("Arial", 14, "bold")).pack(pady=5)

        self.tree = ttk.Treeview(frame_contenido, columns=("ID", "Usuario"), 
                                 show="headings", height=10) 
        
        self.tree.column("ID", width=70, anchor=tk.CENTER)
        self.tree.column("Usuario", width=250, anchor=tk.W)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Usuario", text="Usuario")
        
        scrollbar = ttk.Scrollbar(frame_contenido, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=False)


    def cargar_usuarios(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
            
        usuarios = ver_usuarios()
        if usuarios:
            for u in usuarios:
                self.tree.insert("", tk.END, values=u)
        else:
            self.tree.insert("", tk.END, values=("--", "No hay usuarios registrados o error de conexión"))


    def agregar_usuario(self):
        from user_controller import agregar_usuarios
        
        def guardar():
            u = entry_user.get().strip()
            p = entry_pass.get().strip()
            
            if not u or not p:
                messagebox.showwarning("Campos vacíos", "Ingrese usuario y contraseña.", parent=ventana)
                return
                
            if agregar_usuarios(u, p): 
                messagebox.showinfo("Éxito", f"Usuario {u} creado correctamente.", parent=ventana)
                self.cargar_usuarios()
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No se pudo crear el usuario.", parent=ventana)
        
        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar Usuario")
        ventana.geometry("300x200")
        ventana.transient(self.root)
        ventana.grab_set()

        tk.Label(ventana, text="Usuario").pack(pady=5)
        entry_user = tk.Entry(ventana)
        entry_user.pack(pady=5)
        tk.Label(ventana, text="Contraseña").pack(pady=5)
        entry_pass = tk.Entry(ventana, show="*")
        entry_pass.pack(pady=5)
        tk.Button(ventana, text="Guardar", command=guardar).pack(pady=10)


    def actualizar_usuario(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un usuario de la lista para actualizar.")
            return

        item = self.tree.item(seleccion)
        id_usuario = item['values'][0]
        usuario_actual = item['values'][1]

        def guardar_cambios():
            nuevo_usuario = entry_user.get().strip()
            nueva_contrasena = entry_pass.get().strip()

            if not nuevo_usuario or not nueva_contrasena:
                messagebox.showwarning("Campos vacíos", "Ingrese el nuevo usuario y contraseña.", parent=ventana_act)
                return
            
            if actualizar_usuarios(id_usuario, nuevo_usuario, nueva_contrasena):
                messagebox.showinfo("Éxito", f"Usuario con ID {id_usuario} actualizado a '{nuevo_usuario}'.", parent=ventana_act)
                self.cargar_usuarios()
                ventana_act.destroy()
            else:
                messagebox.showerror("Error", "No se pudo actualizar el usuario.", parent=ventana_act)

        ventana_act = tk.Toplevel(self.root)
        ventana_act.title(f"Actualizar Usuario ID: {id_usuario}")
        ventana_act.geometry("300x250")
        ventana_act.transient(self.root)
        ventana_act.grab_set()

        tk.Label(ventana_act, text=f"Editando a: {usuario_actual}", font=("Arial", 12)).pack(pady=10)

        tk.Label(ventana_act, text="Nuevo Usuario").pack(pady=5)
        entry_user = tk.Entry(ventana_act)
        entry_user.insert(0, usuario_actual)
        entry_user.pack(pady=5)

        tk.Label(ventana_act, text="Nueva Contraseña").pack(pady=5)
        entry_pass = tk.Entry(ventana_act, show="*")
        entry_pass.pack(pady=5)
        
        tk.Button(ventana_act, text="Guardar Cambios", command=guardar_cambios).pack(pady=10)


    def eliminar_usuario(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un usuario de la lista para eliminar.")
            return

        item = self.tree.item(seleccion)
        id_usuario = item['values'][0]
        usuario_a_eliminar = item['values'][1]

        confirmar = messagebox.askyesno(
            "Confirmar Eliminación",
            f"¿Está seguro de que desea eliminar al usuario '{usuario_a_eliminar}' (ID: {id_usuario})?"
        )

        if confirmar:
            if eliminar_usuarios(id_usuario):
                messagebox.showinfo("Éxito", f"Usuario '{usuario_a_eliminar}' eliminado correctamente.")
                self.cargar_usuarios()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el usuario.")

    # SOLUCIÓN AL ERROR DE IMPORTACIÓN
    def cerrar_sesion(self):
        from menu_view import MenuApp 
        self.root.destroy()
        MenuApp(self.username)