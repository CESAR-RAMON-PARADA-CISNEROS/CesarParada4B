import mysql.connector
from mysql.connector import Error
def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user='root',
            password = '',
            database = 'poo_proyecto_parcial2'

        )

        if conexion.is_connected():
            print("Conexion exitosa en la base de datos")
            return conexion
        
    except Error as e:
        print("Error al conectar a Mysql: {e}")
        return None