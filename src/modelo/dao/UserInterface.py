import mysql.connector

def obtener_ubicacion_basededatos(host, usuario, contraseña, base_de_datos):
    try:
        # Conectar a la base de datos MySQL
        conexion = mysql.connector.connect(
            host=host,
            user=usuario,
            password=contraseña,
            database=base_de_datos
        )

        # Obtener la ubicación de la base de datos
        cursor = conexion.cursor()
        cursor.execute("SELECT @@datadir;")
        ubicacion = cursor.fetchone()[0]
        
        print(f"La ubicación de la base de datos '{base_de_datos}' es: {ubicacion}")

    except mysql.connector.Error as error:
        print(f"Error al conectar con la base de datos: {error}")

    finally:
        if conexion:
            conexion.close()

# Configuración de la conexión a MySQL
host = 'localhost'
usuario = 'root'
contraseña = 'changeme'
base_de_datos = 'museo'

# Llamar a la función para obtener la ubicación de la base de datos
obtener_ubicacion_basededatos(host, usuario, contraseña, base_de_datos)
