from logging import exception
import notas.acciones 
import usuarios.usuario 

class Acciones():

    def registro(self):
        print("Muy bien, vamos a registrarte")
        nombre = input("Introduce tu nombre: ")
        apellidos = input("Introduce tus apellidos: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = usuarios.usuario.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
            entrar = input("¿quieres entrar en la aplicación? si/no: ")
            if entrar == "si":
                self.login()
            else:
                print(f"Nos vemos pronto {usuario[0]} ")
        else:
            print("No te has registrado bien")

    def login(self):
        print("Identificate")

        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            usuario = usuarios.usuario.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado con fecha del {login[4]}")
                self.acciones_con_notas(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("Datos incorrectos, vuelvelo a intentar")

    def acciones_con_notas(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nota (crear)
        - Mostrar notas (mostrar)
        - Eliminar notas (eliminar)
        - Salir (salir)
        """)  

        accion = input("¿Qué quieres hacer? " )
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            self.acciones_con_notas(usuario)
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.acciones_con_notas(usuario)
        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.acciones_con_notas(usuario)
        elif accion == "salir":
            print(f"My bien {usuario[1]}, hasta pronto")
            exit()
