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
# ventana.iconbitmap("favicon.ico")

# Definición de la clase Lista_de_productos
class Lista_de_productos(object):
    def __init__(self):
        # Variables importantes
        self.name_data = StringVar()
        self.price_data = StringVar()
        self.products = [] # En esta variable lista guardamos los datos de los productos


    # Definir funciones
    def home(self):
        # Encabezado de la función
        home_label.config(
            padx=220,
            pady=15,
            fg="white",
            bg="black",
            font=("DIN", 25)
        )
        home_label.grid(row=0, column=0, columnspan=12, sticky=W)

        products_box.grid(row=1)

        # Listar productos en la pantalla de Inicio
        for product in self.products:
            if len(product) == 3:
                product.append("added")
                Label(products_box, text=product[0]).grid()
                Label(products_box, text=product[1]).grid()
                Label(products_box, text=product[2]).grid()
                Label(products_box, text="--------------").grid()



        # Ocultar widgets
        add_label.grid_remove()
        info_label.grid_remove()
        data_label.grid_remove()
        add_frame.grid_remove()

        

    def add(self):
        # Encabezado de la función
        add_label.config(
            padx=200,
            pady=15,
            fg="white",
            bg="black",
            font=("DIN", 25)
        )
        add_label.grid(row=0, column=0, columnspan=12, sticky=W)

        # Configuración de los widgets del formulario
        add_frame.grid(row=1)

        add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
        add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        add_name_entry.config(justify=CENTER)
        add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
        add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        add_price_entry.config(justify=CENTER)
        add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NE)
        add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        add_description_entry.config(
            width=30,
            height=5,
            font=("DIN", 15),
            padx=10,
            pady=10
        )
        boton.grid(row=4, column=1, sticky=W)
        boton.config(
            fg="white",
            bg="green",
            padx=10,
            pady=10
        )

        # Ocultar widgets
        home_label.grid_remove()
        info_label.grid_remove()
        data_label.grid_remove()
        products_box.grid_remove()


    def info(self):
        # Encabezado de la función
        info_label.config(
            padx=200,
            pady=15,
            fg="white",
            bg="black",
            font=("DIN", 25)
        )
        info_label.grid(row=0, column=0, columnspan=12, sticky=W)

        data_label.config(
            fg="darkblue",
            bg="lightblue",
            font=("arial", 10),
            pady=15,
            padx=15
        )
        data_label.grid(row=1, column=0, sticky=W)

        # Ocultar widgets
        home_label.grid_remove()
        add_label.grid_remove()
        add_frame.grid_remove()
        products_box.grid_remove()

    def add_product(self):
        # Añadir un producto a la lista products
        self.products.append([
            self.name_data.get(),
            self.price_data.get(),
            add_description_entry.get("1.0", "end-1c")
        ])
        # Inicializar añadir producto
        self.name_data.set("")
        self.price_data.set("")
        add_description_entry.delete("1.0", END )

        self.home()


lista_de_productos = Lista_de_productos()

# Etiqueta de Inicio en la pantalla Inicio
home_label = Label(ventana, text="Inicio")

# Frame para manejar todos los widgets a la vez dentro del listado de pantalla de inicio
products_box = Frame(ventana, width=250)

# Etiqueta de Añadir en la pantalla Añadir
add_label = Label(ventana, text="Añadir")

# Etiqueta de Información en la pantalla Información
info_label = Label(ventana, text="Información")

# Etiqueta de Política de Productos en la pantalla información
data_label = Label(ventana, text="Politica de calidad de nuestro productos")

# Formulario de productos en la pantalla de Añadir
add_frame = Frame(ventana) # Frame para manejar todos los widgets a la vez dentro del frame

add_name_label = Label(add_frame, text="Nombre de producto")
add_name_entry = Entry(add_frame, textvariable=lista_de_productos.name_data)

add_price_label = Label(add_frame, text="Precio de producto")
add_price_entry = Entry(add_frame, textvariable=lista_de_productos.price_data)

add_description_label = Label(add_frame, text="Descripción de producto")
add_description_entry = Text(add_frame)

boton = Button(add_frame, text="Guardar", command= lista_de_productos.add_product)

# Crear el menu superior 
"""
opcion_menu = StringVar()
opcion_menu.set("Inicio")

selector = OptionMenu(ventana, opcion_menu, "Inicio", "Añadir", "Informacion", "Salir")
selector.grid(row=0, column=0)
"""
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command = lista_de_productos.home)
menu_superior.add_command(label="Añadir", command=lista_de_productos.add)
menu_superior.add_command(label="Información", command=lista_de_productos.info)
menu_superior.add_command(label="Salir", command=ventana.quit)

ventana.config(menu=menu_superior)

ventana.mainloop()