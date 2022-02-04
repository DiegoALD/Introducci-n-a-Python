# texto = Label(ventana, text="Hola a todos")
# texto.pack()

# fg = color del texto
# bg = color del fondo
# lista de colores: https://www.tcl.tk/man/tcl8.5/TkCmd/colors.html
# color en RGB: https://guia-tkinter.readthedocs.io/es/develop/chapters/8-colors/8.1-Intro.html#nombres-de-colores
# padx = margen horizontal dentro del widget (pixeles)
# pady =
# font = tipo de fuente, tamaño
# weigh = anchura en caracteres
# high = en lineas de caracteres
# cursor = define la forma del cursor

from tkinter import *

ventana = Tk()
ventana.geometry("900x500")

texto = Label(ventana, text= "Primer texto")
texto.config(
    fg ="white",
    bg ="chocolate",
    padx=15,
    pady=15,
    font=("arial", 30),
    width=10,
    height=2,
    cursor="spider"
)
texto.pack(side=LEFT,anchor=W)


texto = Label(ventana, text= "Segundo texto")
texto.config(
    fg ="white",
    bg ="red",
    padx=15,
    pady=15,
    font=("arial", 30),
    width=10,
    height=2,
    cursor="spider"
)
texto.pack(side=TOP,anchor=N)


texto = Label(ventana, text= "Tercer texto")
texto.config(
    fg ="white",
    bg ="blue",
    padx=15,
    pady=15,
    font=("arial", 30),
    width=10,
    height=2,
    cursor="spider"
)
texto.pack(side=BOTTOM ,anchor=E)

ventana.mainloop()
