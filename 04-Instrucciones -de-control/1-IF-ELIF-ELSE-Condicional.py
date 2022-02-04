# Estructura de control de flujo condicional (if)

"""
Condicional if

Si se cumple la condición se ejecuta bloque 1
Si no se cumple la condición se ejecuta bloque2

if condicion:
    bloque1
else:
    bloque2
"""

# ejemplo 1
"""
programador = input("Dime en que lenguajes programas ")

if programador == "Python":
    print("Asignar a este programador proyectos de Python")
else:
    print("No asignar proyectos de Python a este programador")
"""

# Ifs anidados

# Introducimos el número del día de la semana y nos dice el nombre
"""
numero_dia_de_la_semana = input("Dime el número del día de la semana ")

if int(numero_dia_de_la_semana) == 1:
    nombre_dia_de_la_semana = "lunes"
    print(f" El número {numero_dia_de_la_semana} es {nombre_dia_de_la_semana}")
else:
    if int(numero_dia_de_la_semana) == 2:
        nombre_dia_de_la_semana = "martes"
        print(f" El número {numero_dia_de_la_semana} es {nombre_dia_de_la_semana}")
    else:
        if int(numero_dia_de_la_semana) == 3:
            nombre_dia_de_la_semana = "miércoles"
            print(f" El número {numero_dia_de_la_semana} es {nombre_dia_de_la_semana}")
        else:    
            if int(numero_dia_de_la_semana) == 4:
                nombre_dia_de_la_semana = "jueves"
                print(f" El número {numero_dia_de_la_semana} es {nombre_dia_de_la_semana}")
            else: 
                if int(numero_dia_de_la_semana) == 5:
                    nombre_dia_de_la_semana = "viernes"
                    print(f" El número {numero_dia_de_la_semana} es {nombre_dia_de_la_semana}")
                else:
                    print(f" El número {numero_dia_de_la_semana} es FINDE :-)")
"""


# Ejemplo 2

numero_dia = input("Dime el número del día de la semana ")
if int(numero_dia) < 1 or int(numero_dia) > 7:
    print("No es un número válido")
else:
    if int(numero_dia) == 1:
        nombre_dia = "lunes"
        print(f"El número {numero_dia} es {nombre_dia}")
    elif int(numero_dia) == 2:
        nombre_dia = "martes"
        print(f"El número {numero_dia} es {nombre_dia}")
    elif int(numero_dia) == 3:
        nombre_dia = "miércoles"
        print(f"El número {numero_dia} es {nombre_dia}")
    elif int(numero_dia) == 4:
        nombre_dia = "jueves"
        print(f"El número {numero_dia} es {nombre_dia}")
    elif int(numero_dia) == 5:
        nombre_dia = "viernes"
        print(f"El número {numero_dia} es {nombre_dia}")
    else:
        nombre_dia = "finde"
        print("Fin de semana")