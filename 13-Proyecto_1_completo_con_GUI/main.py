from usuarios import acciones
from tkinter import *

"""
	Proyecto Python MySQL
	- Abrir asistente
	- Login o registro
	- Si elegimos registro, creará un registro en la BBDD
	- Si elegimos login, identifica el usuario y nos preguntará_
        - Crear nota, buscar nota o borrarla
"""

ventana = Tk()
ventana.minsize(600, 400)
ventana.title("APP de gestión de notas")
ventana.iconbitmap("./11-tkinter/imagenes/eoi.ico")

fra_reg_o_log = Frame(ventana)

Label(fra_reg_o_log, text="¿Qué quieres hacer?: ").grid(row=0, column=0, sticky=W)

# Radiobutton
def marcar_registro():

    marca.set(opcion.get())
    label_log.grid_remove()
    label_reg = Label(fra_reg_o_log, text=marca.get())
    label_reg.grid(row=3, column=0, sticky=W)
    Button(fra_reg_o_log, fg="white", bg="grey",text= "Continuar", command=hazEl.registro).grid(row=3, column=1)
    
def marcar_login():
    marca.set(opcion.get())
    label_reg.grid_remove()
    label_log = Label(fra_reg_o_log, text=marca.get())
    label_log.grid(row=3, column=0, sticky=W)
    Button(fra_reg_o_log, fg="white", bg="blue",text= "Continuar", command=hazEl.login).grid(row=3, column=1)
    
opcion = StringVar()
marca = StringVar()
opcion.set(None)

fra_reg_o_log.config(
    bg="pink",
    bd=5,
    relief=SOLID,
    padx=10,
    pady=10
)
fra_reg_o_log.grid(row=0)

Radiobutton(
    fra_reg_o_log, 
    text="Registro",
    value="registro",
    variable=opcion,
    command=marcar_registro
    ).grid(row=1, column=0, sticky=W)

Radiobutton(
    fra_reg_o_log,
    text="Login",
    value="login",
    variable=opcion,
    command=marcar_login
    ).grid(row=2, column=0, sticky=W)

Label(fra_reg_o_log, text=marca.get()).grid(row=3, column=0, sticky=W)
label_reg = Label(fra_reg_o_log, text=marca.get())
label_log = Label(fra_reg_o_log, text=marca.get())

hazEl = acciones.Acciones(ventana, fra_reg_o_log)

ventana.mainloop()