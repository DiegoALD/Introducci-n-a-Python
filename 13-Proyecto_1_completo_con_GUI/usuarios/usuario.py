import datetime
import usuarios.conexion as conexion
from tkinter import *

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self, nombre, apellidos, email, password, fra_reg):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
        self.fra_reg = fra_reg

# No son necesarios getters ni setters

    def registrar(self):
        fecha = datetime.datetime.now()
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, self.password, fecha)
        try:

            cursor.execute(sql, usuario)
            database.commit()

        except Exception as e:
            Label(self.fra_reg, text=str(type(e))).grid(row=9, column=0)
            Label(self.fra_reg, text=str(type(e).__name__)).grid(row=10, column=0)
            Label(self.fra_reg, text=f"Ya existe el correo {usuario[2]}, vuelvelo a intentar").grid(row=11, column=0)
  
        return [cursor.rowcount, self]  # Cuenta los registros cambiados

    def identificar(self):

        # Consulta para comprobar si existe el usuario
        sql = "SELECT * FROM usuarios WHERE (email = %s) AND (password = %s)"

        # Datos para la consulta
        usuario = (self.email, self.password)

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result