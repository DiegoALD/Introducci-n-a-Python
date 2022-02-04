# -*- coding: utf-8 -*-  

# Distintos tipos de variables en Python

"""
Las variables son contenerdores de datos:
* Python es debilmente tipado.
* Es obligatorio declarar una variable antes de utilizarla
"""

"""
PEP 8: variables
Utilizar nombres descriptivos y en minúsculas. Para nombres
compuestos, separar las palabras por guiones bajos. Antes y
después del signo =, debe haber uno (y solo un) espacio en
blanco
Correcto: mi_variable = 12
Incorrecto: MiVariable = 12 | mivariable = 12 | mi_variable=12 |
mi_variable = 12
"""

# Tipos de variables sencillas

from cgi import print_directory


cadena = "Antonio"  # Esta variable es un string str
entero = 22  # Esta variable es un entero int
flotante = 5.3  # Esta variable es un flotante float
booleano = True  # Esta variable es un booleano bool

# Tipos de datos complejos

# list es un conjunto de datos con indice (ordenado) y es mutable
lista = ["inicio", 12, "medio", 2, "fin"]
# tuple es un conjunto de datos con indice (ordenado) y es inmutable
tupla = (12, "segundo", 5, 7, "fin")
# range es un conjunto de números enteros
rango = range(-1, 100)
# set es un conjunto de datos no ordenado (sin indice)
conjunto = {"inicio", 2, "medio", 4, "fin"}
# dictionary es un conjunto Clave/Valor, es ordenado y es mutable
diccionario_flor = {
    "nombre": "Clavel",
    "color": "rojo",
    "origen": "España",
    "precio_docena": 20
}
# Listas de diccionarios,
diccionario_flores = [
    {
        "nombre": "Clavel",
        "color": "rojo",
        "origen": "España",
        "precio_docena": 20       
    },
    {
        "nombre": "Rosa",
        "color": "rosa",
        "origen": "Holanda",
        "precio_docena": 40       
    }    
]



   











