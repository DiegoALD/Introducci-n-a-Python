import mysql.connector

# Conexión
database = mysql.connector.connect(
   host = "localhost",
   user = "root",
   passwd = "",
   database = "proyecto_prueba", # Hasta que no se cree la bd no se puede conectar,
   port = 3306
)

# ¿La conexión ha sido correcta?
# print(database)

# Cursor
cursor = database.cursor(buffered=True)

# Crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS proyecto_prueba")

cursor.execute("SHOW DATABASES")

print("############## Show DDBB ##########")

for bd in cursor:
   print(bd)


# Crear tablas

cursor.execute("""
      CREATE TABLE IF NOT EXISTS coches(
      id int(10) auto_increment not null,
      marca varchar(30) not null,
      color varchar(30) not null,
      velocidad int(20) not null,
      plazas int(20) not null,
      CONSTRAINT pk_coches PRIMARY KEY(id)
      )ENGINE=InnoDb;
   """)

cursor.execute("SHOW TABLES")

print("############## Show Table ##########")

for table in cursor:
   print(table)

# cursor.execute("INSERT INTO coches VALUES(null, 'Opel', 'Astra', 160, 4)")

coches = [
   ("Mercedes", "negro", 200, 5),
   ("Seat", "blanco", 120, 4),
   ("Volvo", "verde", 150, 5),
   ("Renault", "azul", 140, 4)
]

cursor.executemany("INSERT INTO coches VALUES(null, %s, %s, %s, %s)", coches)
database.commit()


cursor.execute("SELECT * FROM coches")
#cursor.execute("SELECT * FROM coches WHERE velocidad <= 200 AND marca = 'Seat' ")
result = cursor.fetchall()

print("############## Mis coches ##########")
for coche in result:
   print(f"\t{coche[1]}\t{coche[3]}\t{coche[4]}")


# Borrar registros
cursor.execute("DELETE FROM coches WHERE marca = 'Renault' ")
database.commit()

print(cursor.rowcount, "borrados !!")

# Actualizar
cursor.execute("UPDATE coches SET color = 'rojo' WHERE marca = 'Seat' ") 
database.commit()

print(cursor.rowcount, "actualizados !!")
