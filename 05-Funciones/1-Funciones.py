# Definición de Funciones en Pyton

"""
    - Una función es un conjunto de instrucciones agrupadas bajo un nombre.

def nombre_de_la_funcion(parametros):
    Bloque de instrucciones
    return valor_retornado
"""



"""
def mi_funcion(nombre):
    print(f"Hola Mundo de parte de {nombre}")


nombre = ["Mario", "Antonio", "José", "Andrea"]

for registro in nombre:
    mi_funcion(registro)
"""

# Recomendaciones sobre funciones

# 1-las funciones se declaran al princio.
# 2-Los datos a la funcion se le pasan como parametros
# 3-Resultados a traves de return.

# Definicion de la funcion
"""
def mis_datos(nombre_local, apellido_local, DNI_local=None):
    if DNI_local == None:
        print(f" Mi nombre es {nombre_local} {apellido_local}")
    else:
        print(f" Mi nombre es {nombre_local} {apellido_local}, mi DNI= {DNI_local}")
        
"""

# Ahora con parametros normales
"""
nombre = "Mario"
apellido = "Lopez"
"""
# Invocamos la función con un parametro por omisión
"""
mis_datos("Mario", "Lopez")
mis_datos("Luisa", "Sánchez", "456372Q")
"""

# Llamada a la función con Keywords y con un parametro por omision
"""
mis_datos(apellido_local="Lopez", nombre_local="Mario")
mis_datos(apellido_local="Sanchez", DNI_local="456372Q", nombre_local="Luisa")
"""

# Ejercio de calculadora con parametro por omision y retorno del valor calculado

"""
Premisas:
    - La funcion es una calculadora con las 4 operaciones:
     
        Parametros:
        - Basicas + y - (Parametro por omision = False)
        - Complejas * y / (Parametro por omision = True)
        - Los otros 2 parametros son los numeros con los que hacemos los calculos
    - El usuario dice los 2 numeros y el tipo de operación.
    - Retornamos con return los valores de la operación (basica o compleja)
"""
# Ejemplo 6: 

def calculadora(numero1,numero2,basica=False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2
    cadena =""
    if basica == False:
        cadena += "Suma " + str(suma)
        cadena += "\n"
        cadena += "Resta " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multi " + str(multi)
        cadena += "\n"
        cadena += "División " + str(division)
        cadena += "\n"

    return cadena

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
tipo_de_operacion = input("introduce si la operación es basica (+ ó -) o compleja (* ó /): ")

if tipo_de_operacion == "basica":
    print(calculadora(num1, num2))
elif tipo_de_operacion == "compleja":
    print(calculadora(num1, num2, True))
else: print("No ha introducido 'basica' o 'compleja'")

