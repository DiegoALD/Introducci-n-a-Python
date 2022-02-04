from tkinter import *

ventana = Tk()
ventana.geometry("500x500")
ventana.title("Fundamentos de Tkinter")
# ventana.iconbitmap("fav.ico")

marco_padre1 = Frame(ventana, width=500, height=200)
"""marco_padre1.config(
    bg="lightblue",
    bd="10",
    relief="solid" # se puede poner el str o una cte. en mayúsculas
)"""
marco_padre1.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)


marco = Frame(marco_padre1, width=200, height=200)
marco.config(
    bg="blue",
    bd="10",
    relief="solid" # se puede poner el str o una cte. en mayúsculas
)
marco.pack(side=LEFT, anchor=SW)

marco = Frame(marco_padre1, width=200, height=200)
marco.config(
    bg="green",
    bd="10",
    relief="solid" # se puede poner el str o una cte. en mayúsculas
)
marco.pack(side=RIGHT, anchor=SE)

marco_padre2 = Frame(ventana, width=500, height=200)
"""marco_padre2.config(
    bg="lightblue",
    bd="10",
    relief="solid" # se puede poner el str o una cte. en mayúsculas
)"""
marco_padre2.pack(side=TOP, anchor=N, fill=X, expand=YES)


marco = Frame(marco_padre2, width=200, height=200)
marco.config(
    bg="RED",
    bd="10",
    relief="solid" # se puede poner el str o una cte. en mayúsculas
)
marco.pack(side=LEFT, anchor=NW)

marco = Frame(marco_padre2, width=200, height=200)
marco.config(
    bg="yellow",
    bd="10",
    relief="solid" # se puede poner el str o una cte. en mayúsculas
)
marco.pack(side=RIGHT, anchor=NE)

ventana.mainloop()