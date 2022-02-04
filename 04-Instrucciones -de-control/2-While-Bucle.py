# Bucle While

"""
Estructura de control que itera o repite la ejecución de una
serie de instrucciones tantas veces como sea necesario,
hasta que no se cumpla la condición. Admite else cuando no se cumpla la condición

while condicion:
    bloque de instrucciones
    actualizacion del contador
else:
    bloque de instrucciones
"""

# Ejemplo 1: Escribir los 100 primero números naturales

# Hecho ya

# Ejemplo 2:
"""
* El usuario nos de un número.
* Presentamos la tabla de multiplicar del 1 al 10 de ese número.
* Lo hacemos con while
"""

print("*** Ejemplo de tabla de multiplicar con While ***")
numero_usuario = input("¿Qué tabla quieres? ")

contador = 1
while contador <= 10:
    print(f"{numero_usuario} x {contador} = {int(numero_usuario)*contador}")
    contador += 1
else:
    print("Tabla terminada")

