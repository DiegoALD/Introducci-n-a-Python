from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("1300x600")

texto = Label(ventana, text="Hola a todos")
texto.config(font=("DIN", 20))
texto.pack(anchor=W)

imagen = Image.open("./11-tkinter/imagenes/lambo.jpg")
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack()

ventana.mainloop()
