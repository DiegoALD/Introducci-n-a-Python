"""
Calculadora:
- 2 campos para introducir los números
- 4 campos para elegir la operación
- nuestra el resultado por una alerta
"""

from tkinter import *
from tkinter import messagebox

ventana = Tk()

class Calculadora:

    def __init__(self):  
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
       
    def convFloat(self, numero):
        try:
            self.result = float(numero)
        except:
            self.result = 0
            messagebox.showerror("Datos", "Introduce bien los datos")
        return self.result

    def sumar(self):

        self.resultado.set(self.convFloat(self.numero1.get()) + self.convFloat(self.numero2.get()))
        self.mostarResultado()

    def restar(self):
        self.resultado.set(self.convFloat(self.numero1.get()) - self.convFloat(self.numero2.get()))
        self.mostarResultado()

    def multiplicar(self):
        self.resultado.set(self.convFloat(self.numero1.get()) * self.convFloat(self.numero2.get()))
        self.mostarResultado()


    def dividir(self):
        self.resultado.set(self.convFloat(self.numero1.get()) / self.convFloat(self.numero2.get()))
        self.mostarResultado()


    def mostarResultado(self):
        messagebox.showinfo("Resultado", f"el resultado es {self.resultado.get()}")
        self.numero1.set("")
        self.numero2.set("")

ventana.title = ("Ejercicio de calculadora")
ventana.geometry("400x400")

calculadora = Calculadora()

marco = Frame(ventana, width=250, height=250)
marco.config(
    pady=10,
    padx=10
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(FALSE)

Label(marco, text="Número 1: ").pack()
Entry(marco, textvariable=calculadora.numero1).pack()

Label(marco, text="Número 2: ").pack()
Entry(marco, textvariable=calculadora.numero2).pack()

Button(marco, text="sumar", command=calculadora.sumar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="restar", command=calculadora.restar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="multiplicar", command=calculadora.multiplicar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="dividir", command=calculadora.dividir).pack(side=LEFT, fill=X, expand=YES)

ventana.mainloop()