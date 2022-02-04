# Bucle FOR

"""
for variable in elemento_iterable (lista, rango, etc):
    BLOQUE DE INSTRUCCIONES
else:
    BLOQUE DE INSTRUCCIONES1
"""

# Ejemplo 1: Escribir los 100 primero números naturales. range(1, 100)
"""
mi_tupla = ('rosa', 'verde', 'celeste', 'amarillo') 
for color in mi_tupla: 
    print(color)

mi_lista = ['Juan', 'Antonio', 'Pedro', 'Herminio'] 
for nombre in mi_lista: 
    print(nombre)
else:
    print("Hemos terminado con la lista de nombres")
"""
"""
contador = 0
resultado = 0

for contador in range(0, 100):
    print("voy por el " + str(contador))
    resultado += contador
else:
    print(f"El resutado es {resultado}")
"""
# Ejemplo 2:
"""
* El usuario nos de un número (tiene que se entre 1 y 100)
* Presentamos la tabla de multiplicar del 1 al 10 de ese número.
* Lo hacemos con for
"""
tabla = int(input("¿De qué número quieres la tabla?: "))
print(f"#### Tabla de multiplicar del número {tabla} ####")

for numero_en_tabla in range(1, 11):

    if (tabla < 1) or (tabla > 99):
        
        print("Número introducido no permitido")
        break
    
    print(f"{tabla} x {numero_en_tabla} = {tabla * numero_en_tabla}")
else:
    print("Tabla finalizada")
