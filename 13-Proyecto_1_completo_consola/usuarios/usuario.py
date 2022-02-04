import datetime
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

# No son necesarios getters ni setters

    def registrar(self):
        fecha = datetime.datetime.now()
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, self.password, fecha)

        cursor.execute(sql, usuario)
        database.commit()
    
        return [cursor.rowcount, self]  # Cuenta los registros cambiados

    def identificar(self):

        # Consulta para comprobar si existe el usuario
        sql = "SELECT * FROM usuarios WHERE (email = %s) AND (password = %s)"

        # Datos para la consulta
        usuario = (self.email, self.password)

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result