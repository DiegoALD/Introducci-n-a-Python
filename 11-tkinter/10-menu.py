# Configuración del widget Menu

from tkinter import *
from tkinter import ttk


ventana = Tk()
ventana.geometry("400x400")
ventana.title("Widgets complejos en Python")
# ventana.iconbitmap("fav.ico")

mi_menu = Menu(ventana) # instanciación del objeto mi_menu
ventana.config(menu=mi_menu) # configuración en el contenedor ventana

# menu vertical de Archivo
archivo = Menu(mi_menu, tearoff=0) # Con tearoff controla la primera linea del menú
archivo.add_command(label="Nuevo archivo")
archivo.add_command(label="Nueva ventana")
archivo.add_separator()
archivo.add_command(label="Abrir archivo")
archivo.add_command(label="Salir", command=ventana.quit)

editar = Menu(mi_menu, tearoff=1)
editar.add_command(label="Deshacer")
editar.add_command(label="Rehacer")
editar.add_separator()
editar.add_command(label="Cortar")
editar.add_command(label="copiar")
editar.add_command(label="Pegar")
editar.add_separator()

# menú horizontal (superior) con el vertical en archivo
mi_menu.add_cascade(label="Archivo", menu=archivo)
mi_menu.add_cascade(label="Editar", menu=editar)
mi_menu.add_command(label="Selección")
mi_menu.add_command(label="Salir", command=ventana.quit)

# Todos los add_command pueden llevar un evento con command.

ventana.mainloop()