"""
Crear un programa que tenga:
- (Hecho) Una ventana
- (Hecho) Tamaño fijo
- (Hecho) No redimensionable
- (Hecho) Un menu (Inicio, Añadir, Información, Salir)
- (Hecho) Opción de salir
- (Hecho) Diferentes pantallas
- (Hecho) Formulario de añadir productos
- (Hecho) Guardar datos temporalmente
- Mostrar datos listados en la pantalla inicio
"""

# Contectando con las librerías
from tkinter import *

# Crear ventana
ventana = Tk()
ventana.geometry("500x500")
ventana.resizable(0, 0)
ventana.title("Lista de productos")
# entana.iconbitmap("favicon.ico")

# Definición de la clase Lista_de_productos
class Lista_de_productos(object):
    def __init__(self):
        # Variables importantes
        self.name_data = StringVar()
        self.price_data = StringVar()
        self.products = [] # En esta variable lista guardamos los datos de los productos

                
        # Etiqueta de Inicio en la pantalla Inicio
        self.home_label = Label(ventana, text="Inicio")

        # Frame para manejar todos los widgets a la vez dentro del listado de pantalla de inicio
        self.products_box = Frame(ventana, width=250)

        # Etiqueta de Añadir en la pantalla Añadir
        self.add_label = Label(ventana, text="Añadir")

        # Etiqueta de Información en la pantalla Información
        self.info_label = Label(ventana, text="Información")

        # Etiqueta de Política de Productos en la pantalla información
        self.data_label = Label(ventana, text="Politica de calidad de nuestro productos")

        # Formulario de productos en la pantalla de Añadir
        self.add_frame = Frame(ventana) # Frame para manejar todos los widgets a la vez dentro del frame

        self.add_name_label = Label(self.add_frame, text="Nombre de producto")
        self.add_name_entry = Entry(self.add_frame, textvariable=self.name_data)

        self.add_price_label = Label(self.add_frame, text="Precio de producto")
        self.add_price_entry = Entry(self.add_frame, textvariable=self.price_data)

        self.add_description_label = Label(self.add_frame, text="Descripción de producto")
        self.add_description_entry = Text(self.add_frame)

        self.boton = Button(self.add_frame, text="Guardar", command= self.add_product)

        # Crear el menu superior 
        """
        opcion_menu = StringVar()
        opcion_menu.set("Inicio")

        selector = OptionMenu(ventana, opcion_menu, "Inicio", "Añadir", "Informacion", "Salir")
        selector.grid(row=0, column=0)
        """
        self.menu_superior = Menu(ventana)
        self.menu_superior.add_command(label="Inicio", command =self.home)
        self.menu_superior.add_command(label="Añadir", command=self.add)
        self.menu_superior.add_command(label="Información", command=self.info)
        self.menu_superior.add_command(label="Salir", command=ventana.quit)


    # Definir funciones
    def home(self):
        # Encabezado de la función
        self.home_label.config(
            padx=220,
            pady=15,
            fg="white",
            bg="black",
            font=("DIN", 25)
        )
        self.home_label.grid(row=0, column=0, columnspan=12, sticky=W)

        self.products_box.grid(row=1)

        # Listar productos en la pantalla de Inicio
        for product in self.products:
            if len(product) == 3:
                product.append("added")
                Label(self.products_box, text=product[0]).grid()
                Label(self.products_box, text=product[1]).grid()
                Label(self.products_box, text=product[2]).grid()
                Label(self.products_box, text="--------------").grid()



        # Ocultar widgets
        self.add_label.grid_remove()
        self.info_label.grid_remove()
        self.data_label.grid_remove()
        self.add_frame.grid_remove()

        

    def add(self):
        # Encabezado de la función
        self.add_label.config(
            padx=200,
            pady=15,
            fg="white",
            bg="black",
            font=("DIN", 25)
        )
        self.add_label.grid(row=0, column=0, columnspan=12, sticky=W)

        # Configuración de los widgets del formulario
        self.add_frame.grid(row=1)

        self.add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
        self.add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        self.add_name_entry.config(justify=CENTER)
        self.add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
        self.add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        self.add_price_entry.config(justify=CENTER)
        self.add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NE)
        self.add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        self.add_description_entry.config(
            width=30,
            height=5,
            font=("DIN", 15),
            padx=10,
            pady=10
        )
        self.boton.grid(row=4, column=1, sticky=W)
        self.boton.config(
            fg="white",
            bg="green",
            padx=10,
            pady=10
        )

        # Ocultar widgets
        self.home_label.grid_remove()
        self.info_label.grid_remove()
        self.data_label.grid_remove()
        self.products_box.grid_remove()


    def info(self):
        # Encabezado de la función
        self.info_label.config(
            padx=200,
            pady=15,
            fg="white",
            bg="black",
            font=("DIN", 25)
        )
        self.info_label.grid(row=0, column=0, columnspan=12, sticky=W)

        self.data_label.config(
            fg="darkblue",
            bg="lightblue",
            font=("arial", 10),
            pady=15,
            padx=15
        )
        self.data_label.grid(row=1, column=0, sticky=W)

        # Ocultar widgets
        self.home_label.grid_remove()
        self.add_label.grid_remove()
        self.add_frame.grid_remove()
        self.products_box.grid_remove()

    def add_product(self):
        # Añadir un producto a la lista products
        self.products.append([
            self.name_data.get(),
            self.price_data.get(),
            self.add_description_entry.get("1.0", "end-1c")
        ])
        # Inicializar añadir producto
        self.name_data.set("")
        self.price_data.set("")
        self.add_description_entry.delete("1.0", END )

        self.home()


lista_de_productos = Lista_de_productos()

ventana.config(menu=lista_de_productos.menu_superior)

ventana.mainloop()