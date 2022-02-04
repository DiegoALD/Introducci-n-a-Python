# Importar el módulo de tkinter
from tkinter import *
from tkinter.font import families
from typing import Sized

"""
Tkinder es un módulo que nos permite crear interfaces
gráficos para nuestras aplicaciones.
El módulo ya viene de forma estándard en Python.
"""
"""
# Módulo para crear interfaces gráficas de usuario
from tkinter import * 

# Crear la ventana raíz
ventana = Tk()

# Icono de una ventana, tiene que ser de tipo .ico
ventana.iconbitmap("./11-tkinder/imagenes/descargar.ico")

# Poner titulo
ventana.title("Programa de desarrolladores Madrid")

# Incrementar el tamaño
ventana.geometry("750x450")(pixeles)

# Bloqueo del tamaño de la ventana horizontalmente y verticalmente
# (0,0)(1,1)(0,1)(1,0)
ventana.resizable(1,1)

# Arrancar y mostrar la ventana hasta qeu se cierre
ventana.mainloop()
"""
"""
# Instanciar la ventana
ventana = Tk()
ventana.geometry("500x500")
ventana.title("Programa Python")
ventana.iconbitmap("./11-tkinter/imagenes/bicicleta.ico")
ventana.resizable(1,1)

texto = Label(ventana, text="Hola desde esta ventana")
texto.pack()
# Lanzamos la ventana
ventana.mainloop()
"""

class Programa():
    def __init__(self, title, icon, size, resizable):
        # self.title = "EOI Programa Python"
        # self.ico = "./11-tkinter/imagenes/EOI.ico"
        # self.size = "500x500"
        # self.resizable = True
        self.title = title
        self.icon = icon
        self.size = size
        self.resizable = resizable



    def cargar (self):

        # Crear ventana
        ventana = Tk()

        self.ventana = ventana

        # Añadimos las caracteristicas
        ventana.iconbitmap(self.icon)
        ventana.title(self.title)
        ventana.geometry(self.size)
        if self.resizable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)

    # Añadimos un texto
    def addText(self, textoAnadir):
        texto = Label(self.ventana, text=textoAnadir)
        texto.pack()

    def mostrar(self):
        # Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()

programa = Programa("Programa de Python", "", "500x500", True)
programa.cargar()
programa.addText("Primer texto")
programa.addText("Segundo texto")
programa.addText("Tercer texto")
programa.mostrar()