"""
Calculadora:
- 2 campos para introducir los números
- 4 campos para elegir la operación
- nuestra el resultado por una alerta
"""

from tkinter import *
from tkinter import messagebox

class Calculadora():

    def __init__(self): 
        self.ventana = Tk()
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
        
        self.ventana.title("Ejercicio de calculadora")
        self.ventana.geometry("600x400")

        self.marco = Frame(self.ventana, width=250, height=250)
        self.marco.config(
            # bd=5,
            # relief=SOLID,
            pady=10,
            padx=10
        )
        self.marco.pack(side=TOP, anchor=CENTER)
        self.marco.pack_propagate(FALSE)

        Label(self.marco, text="Número 1: ").pack()
        Entry(self.marco, textvariable=self.numero1).pack()

        Label(self.marco, text="Número 2: ").pack()
        Entry(self.marco, textvariable=self.numero2).pack()

        Button(self.marco, text="sumar", command=self.sumar).pack(side=LEFT, fill=X, expand=YES)
        Button(self.marco, text="restar", command=self.restar).pack(side=LEFT, fill=X, expand=YES)
        Button(self.marco, text="multiplicar", command=self.multiplicar).pack(side=LEFT, fill=X, expand=YES)
        Button(self.marco, text="dividir", command=self.dividir).pack(side=LEFT, fill=X, expand=YES)

        self.ventana.mainloop()

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

calculadora = Calculadora()

