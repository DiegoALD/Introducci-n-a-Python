from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.geometry("300x300")

def sacarAlerta():
    MessageBox.showinfo("Alerta", "Alerta Nº 1")
    MessageBox.showerror("Alerta", "Alerta Nº 2")
    MessageBox.showwarning("Alerta", "Alerta Nº 3")
    MessageBox.askquestion("Alerta", "Alerta Nº 4")

    return True

Button(ventana, text="Mostrar alertas", command=sacarAlerta).pack()

ventana.mainloop()

