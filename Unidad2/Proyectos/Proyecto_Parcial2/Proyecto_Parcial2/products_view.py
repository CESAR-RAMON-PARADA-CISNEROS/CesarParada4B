import tkinter as tk
from tkinter import messagebox, ttk
from products_controller import (
    ver_productos,
    agregar_producto,
    actualizar_producto,
    eliminar_producto
)
# Nota: La importación de 'menu_view' se hace de forma local en 'cerrar_sesion' para evitar dependencias circulares.

class productosApp:
    def __init__(self, username):
        self.username = username
        self.root = tk.Tk()
        self.root.title(f"Gestión de productos - {username}")
        self.root.geometry("1000x550") # Aumentamos el tamaño para la tabla
        self.root.resizable(True, True)

        self.crear_elementos()
        self.cargar_productos() # <--- ¡Carga inicial de productos!
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

        tk.Button(frame_botones_lateral, text="➕ Agregar producto", 
                  command=self.agregar_producto, width=15).pack(pady=5)

        tk.Button(frame_botones_lateral, text="🔄 Actualizar producto", 
                  command=self.actualizar_producto, width=15).pack(pady=5)

        tk.Button(frame_botones_lateral, text="❌ Eliminar producto", 
                  command=self.eliminar_producto, width=15).pack(pady=5)
        
        tk.Button(frame_botones_lateral, text="🔃 Recargar lista", 
                  command=self.cargar_productos, width=15).pack(pady=15)

        tk.Button(frame_botones_lateral, text="🚪 Regresar al menu", 
                  command=self.cerrar_sesion, width=15).pack(side="bottom", pady=(10, 0))

        # Marco de Contenido (Derecha - Tabla)
        frame_contenido = tk.Frame(main_frame)
        frame_contenido.pack(side="right", fill="both", expand=True)

        tk.Label(frame_contenido, text="Lista de Productos", 
                 font=("Arial", 14, "bold")).pack(pady=5)

        # Configuración de la tabla Treeview
        columns = ("ID", "Nombre", "Stock", "Proveedor", "Precio", "Status", "Marca", "Descripcion")
        self.tree = ttk.Treeview(frame_contenido, columns=columns, show="headings", height=15) 
        
        self.tree.column("ID", width=50, anchor=tk.CENTER)
        self.tree.column("Nombre", width=120, anchor=tk.W)
        self.tree.column("Stock", width=70, anchor=tk.CENTER)
        self.tree.column("Proveedor", width=100, anchor=tk.W)
        self.tree.column("Precio", width=80, anchor=tk.CENTER)
        self.tree.column("Status", width=80, anchor=tk.CENTER)
        self.tree.column("Marca", width=80, anchor=tk.W)
        self.tree.column("Descripcion", width=200, anchor=tk.W)

        for col in columns:
            self.tree.heading(col, text=col)
        
        scrollbar_y = ttk.Scrollbar(frame_contenido, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar_x = ttk.Scrollbar(frame_contenido, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        
        scrollbar_x.pack(side="bottom", fill="x")
        scrollbar_y.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True)


    def cargar_productos(self):
        for row in self.tree.get_children():
                self.tree.delete(row)

        productos = ver_productos()

        if productos:
            for p in productos:
                self.tree.insert("", tk.END, values=p)
        else:
            self.tree.insert("", tk.END, values=("--", "Sin datos", "", "", "", "", "", ""))


    def agregar_producto(self):
        
        def guardar():
            # Obtener y validar los valores
            try:
                nombre_producto = entry_nombre.get().strip()
                stock = entry_stock.get().strip()
                provedor = entry_provedor.get().strip()
                precios = entry_precio.get().strip()
                status = entry_status.get().strip()
                marca = entry_marca.get().strip()
                descripcion = text_descripcion.get("1.0", tk.END).strip()

                if not all([nombre_producto, stock, provedor, precios, status, marca]):
                    messagebox.showwarning("Campos incompletos", "Complete todos los campos obligatorios.", parent=ventana)
                    return
                
                # Conversión a tipos de datos esperados por el controlador
                stock = int(stock)
                precios = float(precios)
                
            except ValueError:
                messagebox.showwarning("Error de datos", "Stock debe ser un número entero y Precio un número decimal.", parent=ventana)
                return

            if agregar_producto(nombre_producto, stock, provedor, precios, status, marca, descripcion): 
                messagebox.showinfo("Éxito", f"Producto '{nombre_producto}' agregado correctamente.", parent=ventana)
                self.cargar_productos()
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No se pudo agregar el producto.", parent=ventana)
        
        ventana = tk.Toplevel(self.root)
        ventana.title("➕ Agregar Producto")
        ventana.geometry("350x550")
        ventana.transient(self.root)
        ventana.grab_set()

        # Creación de campos
        tk.Label(ventana, text="Nombre del Producto").pack(pady=2)
        entry_nombre = tk.Entry(ventana, width=40)
        entry_nombre.pack(pady=2)

        tk.Label(ventana, text="Stock (entero)").pack(pady=2)
        entry_stock = tk.Entry(ventana, width=40)
        entry_stock.pack(pady=2)
        
        tk.Label(ventana, text="Proveedor").pack(pady=2)
        entry_provedor = tk.Entry(ventana, width=40)
        entry_provedor.pack(pady=2)

        tk.Label(ventana, text="Precio (decimal)").pack(pady=2)
        entry_precio = tk.Entry(ventana, width=40)
        entry_precio.pack(pady=2)

        tk.Label(ventana, text="Status").pack(pady=2)
        entry_status = tk.Entry(ventana, width=40)
        entry_status.pack(pady=2)

        tk.Label(ventana, text="Marca").pack(pady=2)
        entry_marca = tk.Entry(ventana, width=40)
        entry_marca.pack(pady=2)

        tk.Label(ventana, text="Descripción").pack(pady=2)
        text_descripcion = tk.Text(ventana, height=4, width=30)
        text_descripcion.pack(pady=2)

        tk.Button(ventana, text="Guardar Producto", command=guardar).pack(pady=10)


    def actualizar_producto(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un producto de la lista para actualizar.")
            return

        item = self.tree.item(seleccion)
        valores_actuales = item['values']
        id_producto = valores_actuales[0] # ID

        def guardar_cambios():
            try:
                nombre_producto = entry_nombre.get().strip()
                stock = entry_stock.get().strip()
                provedor = entry_provedor.get().strip()
                precios = entry_precio.get().strip()
                status = entry_status.get().strip()
                marca = entry_marca.get().strip()
                descripcion = text_descripcion.get("1.0", tk.END).strip()
                
                if not all([nombre_producto, stock, provedor, precios, status, marca]):
                    messagebox.showwarning("Campos incompletos", "Complete todos los campos obligatorios.", parent=ventana_act)
                    return

                # Conversión a tipos de datos
                stock = int(stock)
                precios = float(precios)
                
            except ValueError:
                messagebox.showwarning("Error de datos", "Stock debe ser un número entero y Precio un número decimal.", parent=ventana_act)
                return

            if actualizar_producto(id_producto, nombre_producto, stock, provedor, precios, status, marca, descripcion):
                messagebox.showinfo("Éxito", f"Producto ID {id_producto} actualizado.", parent=ventana_act)
                self.cargar_productos()
                ventana_act.destroy()
            else:
                messagebox.showerror("Error", "No se pudo actualizar el producto.", parent=ventana_act)

        ventana_act = tk.Toplevel(self.root)
        ventana_act.title(f"✏️ Actualizar Producto ID: {id_producto}")
        ventana_act.geometry("350x600")
        ventana_act.transient(self.root)
        ventana_act.grab_set()

        tk.Label(ventana_act, text=f"Editando: {valores_actuales[1]} (ID: {id_producto})", font=("Arial", 12, "bold")).pack(pady=10)

        # Campos y pre-llenado con valores actuales
        tk.Label(ventana_act, text="Nombre del Producto").pack(pady=2)
        entry_nombre = tk.Entry(ventana_act, width=40)
        entry_nombre.insert(0, valores_actuales[1])
        entry_nombre.pack(pady=2)

        tk.Label(ventana_act, text="Stock (entero)").pack(pady=2)
        entry_stock = tk.Entry(ventana_act, width=40)
        entry_stock.insert(0, valores_actuales[2])
        entry_stock.pack(pady=2)
        
        tk.Label(ventana_act, text="Proveedor").pack(pady=2)
        entry_provedor = tk.Entry(ventana_act, width=40)
        entry_provedor.insert(0, valores_actuales[3])
        entry_provedor.pack(pady=2)

        tk.Label(ventana_act, text="Precio (decimal)").pack(pady=2)
        entry_precio = tk.Entry(ventana_act, width=40)
        entry_precio.insert(0, valores_actuales[4])
        entry_precio.pack(pady=2)

        tk.Label(ventana_act, text="Status").pack(pady=2)
        entry_status = tk.Entry(ventana_act, width=40)
        entry_status.insert(0, valores_actuales[5])
        entry_status.pack(pady=2)

        tk.Label(ventana_act, text="Marca").pack(pady=2)
        entry_marca = tk.Entry(ventana_act, width=40)
        entry_marca.insert(0, valores_actuales[6])
        entry_marca.pack(pady=2)

        tk.Label(ventana_act, text="Descripción").pack(pady=2)
        text_descripcion = tk.Text(ventana_act, height=4, width=30)
        text_descripcion.insert("1.0", valores_actuales[7])
        text_descripcion.pack(pady=2)
        
        tk.Button(ventana_act, text="Guardar Cambios", command=guardar_cambios).pack(pady=10)


    def eliminar_producto(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un producto de la lista para eliminar.")
            return

        item = self.tree.item(seleccion)
        id_producto = item['values'][0]
        nombre_a_eliminar = item['values'][1]

        confirmar = messagebox.askyesno(
            "Confirmar Eliminación",
            f"¿Está seguro de que desea eliminar el producto '{nombre_a_eliminar}' (ID: {id_producto})?"
        )

        if confirmar:
            if eliminar_producto(id_producto):
                messagebox.showinfo("Éxito", f"Producto '{nombre_a_eliminar}' eliminado correctamente.")
                self.cargar_productos()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el producto.")

    def cerrar_sesion(self):
        # Importación local para evitar dependencias circulares con menu_view
        from menu_view import MenuApp 
        self.root.destroy()
        MenuApp(self.username)