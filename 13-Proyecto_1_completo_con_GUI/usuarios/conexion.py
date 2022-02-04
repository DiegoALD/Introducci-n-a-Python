import mysql.connector

"""
Si queremos cambiar algún parametro de la conexión como el nombre de la BBDD
o el usuario que accede o el host, sólo tenemos que tocar este módulo.
"""

# Conexión
def conectar():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="proyecto_1",
        port=3306  # El puerto está en phpMyAdmin
    )
    cursor = database.cursor(buffered=True)  # Permite hacer muchas consultas con el mismo cursor

    return [database, cursor]
