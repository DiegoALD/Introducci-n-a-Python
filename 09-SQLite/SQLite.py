# Importar el móculo SQLite3
import sqlite3

from Modulos_06.Paquete_1.clase_coche import *

# Crear una conexión
conexion = sqlite3.connect('ejemplo.db')

# Crear nuestro curso
cursor = conexion.cursor()

# Salvar los cambios
conexion.commit()

"""
# Create table, con concatenación de stream
cursor.execute("CREATE TABLE IF NOT EXISTS coches(" +
    "id INTEGER PRIMARY KEY AUTOINCREMENT," +
    "marca varchar(256)," +
    "color varchar(256)," +
    "velocidad int(256)," +
    "plazas int(256))")
"""

# Create table, con comillas triples
cursor.execute(
    """CREATE TABLE IF NOT EXISTS coches(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    marca varchar(256),
    color varchar(256),
    velocidad int(256),
    plazas int(256))"""
    )

conexion.commit()

'''
# Insertar una fila en la table
cursor.execute("""INSERT INTO coches VALUES(
    null,
    'Kia',
    'gris marengo',
    120,
    4
    )""")

conexion.commit()
'''

'''
# Extraer registro seleccionados
cursor.execute("SELECT * FROM coches")
coches = cursor.fetchall()
conexion.commit()

for coche in coches:
    print("---------------")
    print("Key: ", coche[0])
    print("Marca: ", coche[1])
    print("Color: ", coche[2])
    print("Velocidad: ", coche[3])
    print("Plazas: ", coche[4])
'''

# Borrar todos los registros
cursor.execute("DELETE FROM coches")
conexion.commit()

# coche = 

coches = [
    ("Mercedes", "negro", 200, 5),
    ("Seat", "blanco", 120, 4),
    ("Volvo", "verde", 150, 5)
]
cursor.executemany("INSERT INTO coches VALUES (null,?,?,?,?)", coches)
conexion.commit()

cursor.execute("UPDATE coches SET velocidad = 180 WHERE marca = 'Volvo'")
cursor.execute("UPDATE coches SET color = 'amarillo' WHERE marca = 'Seat'")
conexion.commit()

# Extraer registro seleccionados
cursor.execute("SELECT * FROM coches WHERE plazas > 3")
coches = cursor.fetchall()
conexion.commit()

for coche in coches:
    print("---------------")
    print("Key: ", coche[0])
    print("Marca: ", coche[1])
    print("Color: ", coche[2])
    print("Velocidad: ", coche[3])
    print("Plazas: ", coche[4])

    print("----------------------------------------------------------")
    print("\tKey \tMarca \t\tColor \tVelocidad \tPlazas")

for coche in coches:
     print(f"\t{coche[0]} \t{coche[1]} \t\t{coche[2]} \t{coche[3]} \t{coche[4]}")

# Cerrar la bbdd
conexion.close()