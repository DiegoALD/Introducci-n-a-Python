"""
Calculadora:
- 2 campos para introducir los números
- 4 campos para elegir la operación
- nuestra el resultado por una alerta
"""

from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title = ("Ejercicio de calculadora")
ventana.geometry("400x400")

def convFloat(numero):
    try:
        result = float(numero)
    except:
        messagebox.showerror("Datos", "Introduce bien los datos")
        result = 0
    return result

# 3ª fase, meter los command en los buttons y crear las funciones
def sumar():
# 4ª fase try/except (quitar de aquí y poner en convFloat)
#    try:
    resultado.set(convFloat(numero1.get()) + convFloat(numero2.get()))
    mostarResultado()
#    except:
#        messagebox.showerror("Introduce bien los datos")

def restar():
    resultado.set(convFloat(numero1.get()) - convFloat(numero2.get()))
    mostarResultado()

def multiplicar():
    resultado.set(convFloat(numero1.get()) * convFloat(numero2.get()))
    mostarResultado()

def dividir():
    resultado.set(convFloat(numero1.get()) / convFloat(numero2.get()))
    mostarResultado()

def mostarResultado():
    messagebox.showinfo("Resultado", f"el resultado es {resultado.get()}")
    numero1.set("")
    numero2.set("")

# 2ª fase en buttons (side=LEFT(ya esta), fill=X, expand=YES)
marco = Frame(ventana, width=250, height=250)
marco.config(
    bd=5,
    relief=SOLID,
    pady=10,
    padx=10
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(FALSE)


# 1ª fase poner ventana en los objetos, no marco
numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

Label(marco, text="Número 1: ").pack()
Entry(marco, textvariable=numero1).pack()

Label(marco, text="Número 2: ").pack()
Entry(marco, textvariable=numero2).pack()

Button(marco, text="sumar", command=sumar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="restar", command=restar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="multiplicar", command=multiplicar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="dividir", command=dividir).pack(side=LEFT, fill=X, expand=YES)

ventana.mainloop()