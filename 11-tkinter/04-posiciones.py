from tkinter import *

ventana = Tk()

texto = Label(ventana, text="Hola a todos")
texto.config(
    padx=10,
    pady=10,
    fg="darkblue",
    bg="lightblue",
    font=("DIN", 20)
    )
texto.pack(side=TOP, fill=X, expand=YES)

texto = Label(ventana, text="Horizonte")
texto.config(
    padx=50,
    pady=50,
    fg="red",
    bg="yellow",
    font=("arial", 30)
    )
texto.pack(side=TOP, fill=X, expand=YES)

texto = Label(ventana, text="Primero")
texto.config(
    padx=30,
    pady=30,
    fg="black",
    bg="pink",
    font=("DIN", 30)
    )
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text="Segundo")
texto.config(
    padx=30,
    pady=30,
    fg="black",
    bg="blue",
    font=("DIN", 30)
    )
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text="Tercero")
texto.config(
    padx=30,
    pady=30,
    fg="black",
    bg="orange",
    font=("DIN", 30)
    )
texto.pack(side=LEFT, fill=X, expand=YES)

ventana.mainloop()