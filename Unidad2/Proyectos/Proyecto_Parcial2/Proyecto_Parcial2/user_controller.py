from database import crear_conexion

# Muestra el id y el username de todos los usuarios
def ver_usuarios():
    """Retorna una lista de todos los usuarios (ID y Username)."""
    conexion = crear_conexion()
    if not conexion:
        return []
    
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre FROM usuarios") 
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

# CREAR (INSERT)
def agregar_usuarios(username, password):
    """Inserta un nuevo usuario en la base de datos."""
    conexion = crear_conexion()
    
    if not conexion:
        return False
    
    try:
        cursor = conexion.cursor()
        consulta = "INSERT INTO usuarios (nombre, password) VALUES (%s, %s)"
        # CORRECCIÓN: Usar cursor.execute() con la tupla de parámetros
        cursor.execute(consulta, (username, password))
        
        conexion.commit()
        conexion.close()
        return True
    
    except Exception as e:
        if conexion:
            conexion.rollback()
        print(f"Error al crear un usuario. Tipo de error {e}")
        return False
    
# ACTUALIZAR (UPDATE)
def actualizar_usuarios(id_usuario, new_usuario, new_password):
    """Actualiza el username y password de un usuario por su ID."""
    conexion = crear_conexion()
    if not conexion:
        return False
        
    try:
        cursor = conexion.cursor()
        consulta = "UPDATE usuarios SET nombre = %s, password = %s WHERE id = %s"
        # CORRECCIÓN: Orden y formato de la tupla: (new_usuario, new_password, id_usuario)
        cursor.execute(consulta, (new_usuario, new_password, id_usuario)) 
        
        conexion.commit() # CORRECCIÓN: Agregar paréntesis
        conexion.close()
        return True # Retorna True si fue exitoso
        
    except Exception as e:
        if conexion:
            conexion.rollback()
        print(f"Error al actualizar usuario, Tipo de error: {e}")
        return False

# ELIMINAR (DELETE)
def eliminar_usuarios(id_usuario):
    """Elimina un usuario por su ID."""
    conexion = crear_conexion()
    if not conexion:
        return False
        
    try:
        cursor = conexion.cursor()
        # CORRECCIÓN: Pasar el id como una tupla de un solo elemento (id_usuario,)
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (id_usuario,))
        
        conexion.commit()
        conexion.close()
        return True
        
    except Exception as e:
        if conexion:
            conexion.rollback()
        print(f"Error al eliminar usuario, Tipo de error: {e}") 
        return False