import notas.nota as modelo
from tkinter import *

class Acciones:

    def crear(self, usuario, fra_notas):

        def lanzar_guardar():
            titulo_recogido.set(titulo.get())
            contenido_recogido.set(contenido.get())
            # Chequeamos si hay titulo (no está vacio)
            if len(titulo_recogido.get()) == 0:
                Label(fra_notas, text="Introduce un titulo").grid()
                return

            nota = modelo.Nota(usuario[0], titulo_recogido.get(), contenido_recogido.get())
            global guardar
            guardar = nota.guardar()
            if guardar[0] >= 1:
                Label(fra_notas, text=f"Muy bien {usuario[1]}, la nota {guardar[1].titulo} está guardada").grid(row=4, column=0)
            else:
                Label(fra_notas, text=f"Lo siento {usuario[1]}, no se ha guardado la nota").grid(row=4, column=0)

            return

        titulo = StringVar()
        contenido = StringVar()
        titulo.set("")
        contenido.set("")
        titulo_recogido = StringVar()
        contenido_recogido = StringVar()
    
        # Label(fra_notas, text=f"Muy bien {usuario[1]}, vamos a crear una nota").grid(row=0, column=0)
        Label(fra_notas, text=f"{usuario[1]} introduce el titulo de la nota").grid(row=1, column=0, sticky=E)
        Entry(fra_notas, textvariable=titulo).grid(row=1, column=1, sticky=W)
        Label(fra_notas, text=f"{usuario[1]} introduce el contenido de la nota").grid(row=2, column=0, sticky=E)
        Entry(fra_notas, textvariable=contenido).grid(row=2, column=1, sticky=W)
        titulo_recogido.set(titulo.get())
        contenido_recogido.set(contenido.get())

        boton = Button(            
            fra_notas, 
            text="Guardar", 
            command=lanzar_guardar, 
            bg="green",
            fg="white",
            padx=10,
            pady=10).grid(row=3, column=0)

        return

    def mostrar(self, usuario, fra_notas):
        Label(fra_notas, text=f"{usuario[1]}, aqui tienes tus notas").grid()

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            Label(fra_notas, text="**********************").grid()
            Label(fra_notas, text=nota[2]).grid()
            Label(fra_notas, text=nota[3]).grid()
            Label(fra_notas, text="**********************").grid()
        return

    def borrar(self, usuario, fra_notas):

        def lanzar_eliminar():

            titulo_recogido.set(titulo.get())
            nota.titulo = titulo_recogido.get()
            nota.eliminar()
            if nota.eliminado >= 1:
                Label(fra_notas, text= f"Se ha eliminado la nota {nota.titulo}").grid(row=3, column=0)
            else:
                Label(fra_notas, text= "No se ha borrado la nota").grid(row=3, column=0)

            return 

        titulo = StringVar()
        titulo.set("")
        titulo_recogido = StringVar()
        Label(fra_notas, text= f"Muy bien {usuario[1]} vamos a borar notas ").grid(row=0, column=0)
        Label(fra_notas, text= "Introduce el titulo de la nota a borrar ").grid(row=1, column=0, sticky=W)
        Entry(fra_notas, textvariable=titulo).grid(row=1, column=1, sticky=E)
        nota = modelo.Nota(usuario[0], titulo.get())
        
        boton = Button(
            fra_notas, 
            text= "Eliminar", 
            command=lanzar_eliminar, 
            fg="white", 
            bg="green").grid(row=2, column=0)

        return