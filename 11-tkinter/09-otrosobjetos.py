"""
Button
checkbutton
radiobutton
optionmenu
menu
"""

from tkinter import *
from tkinter import ttk


ventana = Tk()
ventana.geometry("400x400")
ventana.title("Widgets complejos en Python")
# ventana.iconbitmap("fav.ico")

encabezado = Label(ventana, text="Checkbox/Radiobutton/Menu")
encabezado.config(
    fg="darkblue",
    bg="lightblue",
    font=("DIN", 20),
    padx=10,
    pady=10
)
encabezado.grid(row=0, column=0, columnspan=6, sticky=W)

# Button
# En command= se pone una función Callback
# "Callback funtion" https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/que-es-un-callback/
# Como función Callback podemos utilizar Lambda. 
# Lambda es una función de una sóla línea. nos permita comprimir el código.
# Información sobre lambda https://www.w3schools.com/python/python_lambda.asp
"""
def funcion_callback_de_button():
    Label(ventana, text="He apretado mi botón").grid(row=1, column=1)
"""

boton = Button(ventana, text="Mi botón", command= lambda: Label(ventana, text="He apretado mi botón").grid(row=1, column=1))
boton.grid(row=1, column=0)

# Checkbutton

def mostrarLenguaje():
    texto = ""

    if lenguaje1.get():
        texto += "Python"
    
    if lenguaje2.get():
        if lenguaje1.get():
            texto += " C#"
        else:
            texto = "C#"

    mostrar.config(
        bg= "green",
        text= texto,
        padx=10
    )

lenguaje1 = IntVar()
lenguaje2 = IntVar()

etiqueta = Label(
    ventana,
    text="¿Qué lenguaje utilizas?: ",
    font=("DIN", 12)
).grid(row=3, column=0, sticky=W)

Checkbutton(
    ventana,
    text="Python",
    variable=lenguaje1,
    onvalue=1,
    offvalue=0,
    command=mostrarLenguaje
).grid(row=4, column=0, sticky=W)

Checkbutton(
    ventana,
    text="C#",
    variable=lenguaje2,
    onvalue=1,
    offvalue=0,
    command=mostrarLenguaje
).grid(row=5, column=0, sticky=W)

mostrar = Label(ventana)
mostrar.grid(row=6, column=0, sticky=W)


# Radiobutton
"""
def marcar():
    marcado.config(text=opcion.get())
"""

label_rb = Label(ventana, text="Estos son los Radiobutton")
label_rb.grid(row=8, column=0)
label_rb.config(
    fg="darkblue",
    bg="lightblue"
)

opcion = StringVar()
opcion.set(None)

Label(ventana, text="¿Cuál es tu género?: ").grid(row=9, column=0)

Radiobutton(
    ventana, 
    text="Masculino",
    value="Masculino",
    variable=opcion,
    command=lambda : marcado.config(text=opcion.get())
    ).grid(row=10, column=0, sticky=W)

Radiobutton(
    ventana,
    text="Femenino",
    value="Femenino",
    variable=opcion,
    command=lambda : marcado.config(text=opcion.get())
    ).grid(row=11, column=0, sticky=W)

marcado = Label(ventana)
marcado.grid(row=12, column=0, sticky=W)

# Option Menu

def seleccionar():
    seleccionado.config(text=opcion_menu.get())

opcion_menu = StringVar()
opcion_menu.set("Opción1")

Label(ventana, text="Selecciona una opción: ").grid(row=7, column=3)

selector = OptionMenu(ventana, opcion_menu, "Opción1", "Opción2", "Opción3", "Opción4", "Otra opcion")
selector.grid(row=8, column=3)

Button(ventana, text="ver OpMenu", command=seleccionar).grid(row=9, column=3)

seleccionado = Label(ventana)
seleccionado.grid(row=10, column=3)

ventana.mainloop()
