from logging import exception
import notas.acciones
import usuarios.usuario
from tkinter import *
from tkinter import ttk
# from main import *

class Acciones(object):
    def __init__(self, ventana, fra_reg_o_log):
        self.ventana = ventana
        self.fra_reg_o_log = fra_reg_o_log
        self.fra_reg = Frame(self.ventana)
        self.fra_log = Frame(self.ventana)
        self.fra_notas = Frame(self.ventana)

    def registro(self):

        def guardar_registro():

            nombre_guardado.set(nombre.get())
            apellidos_guardado.set(apellidos.get())
            email_guardado.set(email.get())
            password_guardado.set(password.get())

            usuario = usuarios.usuario.Usuario(nombre_guardado.get(), apellidos_guardado.get(), email_guardado.get(), password_guardado.get(), self.fra_reg)
            registro = usuario.registrar()

            if registro[0] >= 1:
                
                Label(self.fra_reg, text=f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}").grid(row=8, column=0, sticky=E)
                
                Label(self.fra_reg, text="¿quieres entrar en la aplicación?").grid(row=10, column=0)
        
                opcion = StringVar()
                opcion.set(None)
        
                Radiobutton(
                    self.fra_reg, 
                    text="Sí",
                    value="Sí",
                    variable=opcion,
                    command= lambda : self.login()
                    ).grid(row=11, column=0, sticky=W)

                Radiobutton(
                    self.fra_reg,
                    text="No",
                    value="No",
                    variable=opcion,
                    command= lambda : self.ventana.quit()
                    ).grid(row=12, column=0, sticky=W)

            else:
                # self.fra_reg.grid_remove()
                Label(self.fra_reg, text="No te has registrado bien, vuelve a intentarlo más tarde").grid(row=13, column=0, sticky=E)
            
            return

        self.fra_reg.config(
            bg="lightblue",
            bd=5,
            relief=SOLID,
            padx=10,
            pady=10
        )
        self.fra_reg_o_log.grid_remove()
        self.fra_reg.grid(row=1)


        nombre = StringVar()
        apellidos = StringVar()
        email = StringVar()
        password = StringVar()
        nombre_guardado = StringVar()
        apellidos_guardado = StringVar()
        email_guardado = StringVar()
        password_guardado = StringVar()

        Label(self.fra_reg, text="Vamos a registrarte: ").grid(row=0, column=0, sticky=W)
        Label(self.fra_reg, text="Nombre: ").grid(row=1, column=0, sticky=E)
        Entry(self.fra_reg, textvariable=nombre).grid(row=1, column=1, sticky=W)
        Label(self.fra_reg, text="Apellidos: ").grid(row=2, column=0, sticky=E)
        Entry(self.fra_reg, textvariable=apellidos).grid(row=2, column=1, sticky=W)
        Label(self.fra_reg, text="Email: ").grid(row=3, column=0, sticky=E)
        Entry(self.fra_reg, textvariable=email).grid(row=3, column=1, sticky=W)
        Label(self.fra_reg, text="Contraseña: ").grid(row=4, column=0, sticky=E)
        Entry(self.fra_reg, textvariable=password).grid(row=4, column=1, sticky=W)

        Button(self.fra_reg, text="Guardar", command=guardar_registro).grid(row=5, column=0)   

        return




    def login(self):
        
        def guardar_login(): # Función que implementa el evento del botón para guardar datos del login
            email_guardado_login.set(email_login.get())
            password_guardado_login.set(password_login.get())

            try:
                usuario = usuarios.usuario.Usuario('', '', email_guardado_login.get(), password_guardado_login.get(), self.fra_log)
                login = usuario.identificar()

                if email_guardado_login.get() == login[3]:
                    self.fra_log.grid_remove()
                    self.fra_log.grid(row=0)
                    Label(self.fra_log, text=f"Bienvenido {login[1]}, te has registrado con fecha del {login[5]}").grid(row=0, column=0)
                    # Button(self.fra_log, text="Continuar", fg="white", gb="green", pady=10, padx=10, command=lambda: ).grid(row=7, column=0)
                    self.acciones_con_notas(login)
            except Exception as e:
                self.fra_log.grid_remove()
                self.fra_log.grid(row=0)
                # Label(self.marco2, text=str(type(e))).grid(row=1, column=0)
                # Label(self.marco2, text=str(type(e).__name__)).grid(row=2, column=0)
                Label(self.fra_log, text="Datos incorrectos, vuelvelo a intentar").grid(row=5, column=0)

            return

        self.fra_reg_o_log.grid_remove()
        self.fra_reg.grid_remove()
    
        self.fra_log.config(
            bg="lightgreen",
            bd=5,
            relief=SOLID,
            padx=10,
            pady=10,
            width=100,
            height=200        
        )
        self.fra_log.grid(row=0)

     
        email_login = StringVar()
        password_login = StringVar()
        email_guardado_login = StringVar()
        password_guardado_login = StringVar()

    

        Label(self.fra_log, text="Vamos a identificarte: ").grid(row=0, column=0)
        Label(self.fra_log, text="Email: ").grid(row=1, column=0)
        Entry(self.fra_log, textvariable=email_login).grid(row=1, column=1)
        Label(self.fra_log, text="Contraseña: ").grid(row=2, column=0)
        Entry(self.fra_log, textvariable=password_login).grid(row=2, column=1)

        Button(self.fra_log, text="Guardar", command=guardar_login).grid(row=3, column=0)  

        return

    def acciones_con_notas(self, usuario):

        def lanzar_crear():
            self.fra_notas.grid_remove()
            self.fra_notas = Frame(self.ventana)
            self.fra_notas.grid(row=0)
            hazEl.crear(usuario, self.fra_notas)
            self.acciones_con_notas(usuario)
            return

        def lanzar_mostrar():
            self.fra_notas.grid_remove()
            self.fra_notas = Frame(self.ventana)
            self.fra_notas.grid(row=0)
            hazEl.mostrar(usuario, self.fra_notas)
            self.acciones_con_notas(usuario)
            return

        def lanzar_borrar():
            self.fra_notas.grid_remove()
            self.fra_notas = Frame(self.ventana)
            self.fra_notas.grid(row=0)
            hazEl.borrar(usuario, self.fra_notas)
            self.acciones_con_notas(usuario)
            return

        self.fra_log.grid_remove()
        self.fra_notas.config(
            bg="yellow",
            bd=5,
            relief=SOLID,
            padx=10,
            pady=10,
            width=50,
            height=50
        )
        self.fra_notas.grid(row=0)
        Label(self.fra_notas, text=(f"Muy bien '{usuario[1]}', vamos a gestionar notas")).grid(row=0, column=0)
    
        hazEl = notas.acciones.Acciones()

        mi_menu = Menu(self.ventana, tearoff=0)
        self.ventana.config(menu=mi_menu)
        mi_menu.add_command(label="Crear una nota", command=lanzar_crear)
        mi_menu.add_command(label="Mostrar Notas", command=lanzar_mostrar)
        mi_menu.add_separator()
        mi_menu.add_command(label="Eliminar Notas", command=lanzar_borrar)
        mi_menu.add_command(label="Salir", command=self.ventana.quit)
        # Label(self.fra_notas, text="Vamos con las notas").grid(row=0, column=0)
        return



