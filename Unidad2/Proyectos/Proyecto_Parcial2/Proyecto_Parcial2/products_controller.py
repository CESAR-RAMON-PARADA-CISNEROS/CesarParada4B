from database import crear_conexion

# 🧾 MOSTRAR (READ)
def ver_productos():
    """Obtiene todos los productos registrados."""
    conexion = crear_conexion()
    if not conexion:
        return []

    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id_productos, nombre_producto, stock, provedor, precios, status, marca, descripcion
            FROM productos
        """)
        resultado = cursor.fetchall()
        conexion.close()
        return resultado
    except Exception as e:
        print(f"Error al obtener productos: {e}")
        return []


# ➕ AGREGAR (CREATE)
def agregar_producto(nombre_producto, stock, provedor, precios, status, marca, descripcion):
    """Inserta un nuevo producto en la tabla."""
    conexion = crear_conexion()
    if not conexion:
        return False

    try:
        cursor = conexion.cursor()
        consulta = """
            INSERT INTO productos (nombre_producto, stock, provedor, precios, status, marca, descripcion)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(consulta, (nombre_producto, stock, provedor, precios, status, marca, descripcion))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al agregar producto: {e}")
        conexion.rollback()
        return False


# ✏️ ACTUALIZAR (UPDATE)
def actualizar_producto(id_producto, nombre_producto, stock, provedor, precios, status, marca, descripcion):
    """Actualiza los datos de un producto por su ID."""
    conexion = crear_conexion()
    if not conexion:
        return False

    try:
        cursor = conexion.cursor()
        consulta = """
            UPDATE productos
            SET nombre_producto = %s,
                stock = %s,
                provedor = %s,
                precios = %s,
                status = %s,
                marca = %s,
                descripcion = %s
            WHERE id_productos = %s
        """
        cursor.execute(consulta, (nombre_producto, stock, provedor, precios, status, marca, descripcion, id_producto))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al actualizar producto: {e}")
        conexion.rollback()
        return False


# ❌ ELIMINAR (DELETE)
def eliminar_producto(id_producto):
    """Elimina un producto por su ID."""
    conexion = crear_conexion()
    if not conexion:
        return False

    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id_productos = %s", (id_producto,))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al eliminar producto: {e}")
        conexion.rollback()
        return False
