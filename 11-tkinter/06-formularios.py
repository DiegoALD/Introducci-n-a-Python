from tkinter import *

# Crear ventana
ventana = Tk()
ventana.geometry("500x500")
ventana.title("Python")
# ventana.iconbitmap("fav.ico")
ventana.resizable(1, 1)

"""
# Crear encabezado
encabezado = Label(ventana, text="Hola Mundo")
encabezado.config(
    bg="lightblue",
    fg="darkblue",
    font=("DIN", 20),
    padx=15,
    pady=15
)
encabezado.pack(side=TOP, anchor=NW, fill=X, expand=YES)

# Crear texto
campo_texto = Entry(ventana, text="Primer texto")
campo_texto.config(
    bg="lightgrey",
    fg="black"
)
campo_texto.pack(side=TOP, anchor=NW)
"""
"""
# Pack es más para manejar cajas, para formularios Grid

# Crear encabezado
encabezado = Label(ventana, text="Hola Mundo")
encabezado.config(
    bg="lightblue",
    fg="darkblue",
    font=("DIN", 20),
    padx=15,
    pady=15,
    width=30
)
encabezado.grid(row=0, column=0, columnspan=12, sticky=W)


# Crear texto
etiqueta = Label(ventana, text="Nombre:")
etiqueta.config(font=("DIN", 10))
etiqueta.grid(row=1, column=0, padx=10, pady=10, sticky=E)


campo_texto = Entry(ventana)
campo_texto.config(
    bg="lightgrey",
    fg="black",
    justify="center",
    state="normal"

)
campo_texto.grid(row=1, column=1, sticky=W, padx=10, pady=10)

etiqueta = Label(ventana, text="Apellidos:")
etiqueta.config(font=("DIN", 10))
etiqueta.grid(row=2, column=0, padx=10, pady=10, sticky=E)


campo_texto = Entry(ventana)
campo_texto.config(
    bg="lightgrey",
    fg="black",
    justify="center",
    state="normal"
)
campo_texto.grid(row=2, column=1, sticky=W, padx=10, pady=10)

# Campo de texto grande para un descripción
etiqueta = Label(ventana, text="Descripción:")
etiqueta.config(font=("DIN", 10))
etiqueta.grid(row=3, column=0, padx=10, pady=10, sticky=NE)

campo_texto = Text(ventana)
campo_texto.config(
    width=30,
    height=6,
    fg="black",
    bg="lightgrey",
    state=NORMAL # La otra opción es "disable"
)
campo_texto.grid(row=3, column=1, sticky=W, padx=10, pady=10)

# Creamos un botón
boton = Button(ventana, text="Enviar")
boton.config(
    bg="green",
    fg="white",
    padx=10,
    pady=10
)
boton.grid(row=4, column=1, sticky=E)
"""

# entero = IntVar()  # Declara variable de tipo entera
# flotante = DoubleVar()  # Declara variable de tipo flotante
# cadena = StringVar()  # Declara variable de tipo cadena
# booleano = BooleanVar()  # Declara variable de tipo booleana


"""
def getDato():
    resultado.set(dato.get())

dato = StringVar()
resultado = StringVar()

Label(ventana, text="Introduce dato: ").pack(anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=NW)

Label(ventana, text="Dato recogido: ").pack(anchor=NW)
Label(ventana, textvariable=resultado).pack(anchor=NW)

Button(ventana, text="Mostrar dato", command=getDato).pack(anchor=NW)
"""

def getDato():
    resultado.set(dato.get())

dato = IntVar()
resultado = IntVar()

Label(ventana, text="Introduce dato: ").pack(anchor=NW)
Entry(ventana, textvariable=str(dato)).pack(anchor=NW)

Label(ventana, text="Dato recogido: ").pack(anchor=NW)
Label(ventana, textvariable=str(resultado)).pack(anchor=NW)

Button(ventana, text="Mostrar dato", command=getDato).pack(anchor=NW)


ventana.mainloop()

print(str(resultado.get()))
