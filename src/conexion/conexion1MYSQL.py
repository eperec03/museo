# pip install mysql-connector-python

import mysql.connector


class ConexionMSQL:

    # Especifica los detalles de la conexión
    host = 'localhost'
    database = 'museo'
    user = 'root'
    password = 'changeme'

    "Abre una conexión a la base de datos."
    @staticmethod
    def getConnection():
        try:
            return mysql.connector.connect(
                host= ConexionMSQL.host,
                database= ConexionMSQL.database,
                user= ConexionMSQL.user,
                password= ConexionMSQL.password,
            )
        except mysql.connector.Error as e:
            print(e)

    "Cierra una conexión a la base de datos."
    @staticmethod
    def close(conn):
        try:
            conn.close()
        except mysql.connector.Error as e:
            print(e)
a=ConexionMSQL()
a.getConnection()
