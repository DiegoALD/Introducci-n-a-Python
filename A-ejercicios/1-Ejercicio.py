"""
Ejercicio 1.
    - Crear variables "pais" y "continente"
    - Mostrar su valor por pantalla.
    - Poner un comentario diciendo el tipo de dato que son las variable.
"""
"""
Ejercicio 2.
    - Escribir un script que nos muestre por pantalla los números pares entre el 1 y el 100. Utilizar for.

"""

"""
muestrame = ""
for contador in range(1, 101):
    if contador % 2 == 0:
        muestrame = muestrame + "\n" + str(contador)
else:
    print(muestrame)
"""



"""
Ejercicio 3.
    - Escribir un script que muestro los cuadrados de los primeros 60 números naturales.
    - Lo hacemos con un while
"""


"""
contador = 0
while contador <= 60:
    print(f"El cuadrado de {contador} es {contador**2}")
    contador += 1
else:
    print("Fin de la tabla")
"""


"""
Ejercicio 4. 
    - Pedir la usuario que nos de dos núemros.
    - Realizar con esos números las 4 operaciones fundamentales de la calculadora (+, -, *, /)
    - Presentar el resultado.
"""


"""
numero1 = int(input("Introduce el número 1 "))
numero2 = int(input("Introduce el número 2 "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"La suma de {numero1} + {numero2} es {suma}")
print(f"La resta de {numero1} - {numero2} es {resta}")
print(f"La multiplicación de {numero1} x {numero2} es {multiplicacion}")
print(f"La división de {numero1} / {numero2} es {division}")
"""


"""
Ejercicio 5.
    - Mostrar todas las tablas de multiplicar entre el 1 y el 10.
    - Utilizar for's anidados.
    - Separamos cada tabla con una línea en blanco.

"""

"""
for contador_tablas in range(1, 11):
    print(f"\nTabla del {contador_tablas} \n")
    for contador_tabla in range(1, 11):
        print(f"{contador_tablas} x {contador_tabla} = {contador_tablas * contador_tabla}")
"""


"""
Ejercicio 6.
    - El usuario de la aplicación nos da 2 números entre el 1 y el 100.
    - Devolvemos todos los números pares entre los 2 números que nos ha dado el usuario.
"""


"""
muestra = ""
numero1 = int(input("Introduce el número 1 "))
numero2 = int(input("Introduce el número 2 "))
if int(numero1) < 1 or int(numero1) > 100:
    print("No es un número válido")
else:
    if numero1 < numero2:
        for contador in range(numero1+1,numero2):
            if contador == numero1+1:
                if contador%2 != 0: muestra = str(numero1)
            else:
                if contador%2 != 0: muestra = muestra + ", " + str(contador)
    else:
        for contador in range(numero2+1,numero1):
            if contador == numero2+1:
                if contador%2 != 0: muestra = str(contador)
            else:
                if contador%2 != 0: muestra = muestra + ", " + str(contador)
    print(muestra)
"""





"""
Ejercicio 7.
    - Tenemos una clase de 10 alumnos.
    - Nos dan la nota de cada alumno por teclado e introducir las notas en una lista.
    - Obtener el número de aprobados y de suspensos.
"""

# Funcion mete_las_notas()

"""
Esta funcion mete las 10 notas en una lista de enteros, inicializamos la lista con [].
Return con la lista de las notas.


def mete_las_notas():
    notas_de_alumnos_local = []
    for i in range(1, 11):
        nota_de_alumno_local = int(input(f"Escribe la nota del alumno {i}: "))
        while (nota_de_alumno_local < 0) or (nota_de_alumno_local > 10):
            print("Has escrito una nota incorrecta, pro favor, vuelvela a meter")
            nota_de_alumno_local = int(input(f"mete la nota del alumno {i}: "))
        notas_de_alumnos_local.append(nota_de_alumno_local)
    return(notas_de_alumnos_local)

# Funcion notas()


A este funcion le pasamos la lista de enteros con las notas.
Con el for recorremos la lista e incrementamos las variables con aprobados y suspensos.
Return una tupla con los aprobados y los suspensos

def notas(notas_de_alumnos_local):
    Aprobados_local = 0
    Suspensos_local = 0
    for a in notas_de_alumnos_local:
        if (a >= 5) and (a <= 10):
            Aprobados_local += 1
        else:
            Suspensos_local += 1
    return(Aprobados_local, Suspensos_local)       

Aprobados = 0
Suspensos = 0
notas_aprobados_suspensos = []

notas_de_alumnos = mete_las_notas()
notas_aprobados_suspensos =  notas(notas_de_alumnos)
print(f"Número de aprobados: {notas_aprobados_suspensos[0]}")
print(f"Número de suspendidos: {notas_aprobados_suspensos[1]}")
"""


"""
Ejercicio 8.
Vamos a definir un pequeño registro de usuarios:
    - Pedimos al usuario que introduzca un correo electronico,
    tenemos que comprobar que realmente es un correo electronico.
    - Pedimos al usuario que introduzca una clave que cumpla:
        - Tiene una longitud entre 6 y 12 caradcteres.
        - Contiene:
            - Al menos una mayuscula.
            - Al menos un número.
            - Al menos un caracter especial que sea + ó - ó * ó /.
        - El primer caracter es alfabético.
Si las 2 entradas son correctas, le decimos al usuario que se ha 
registrado correctamente.

Documentación1: https://www.w3schools.com/python/python_strings.asp
Documentación2: Capitulo 6 de curso de Python para principiantes.

Utilizaremos el resultado de este ejercicio para aplicarlo en programas más grandes.
"""

"""
# Declaro variables globales

mail = "null"
resultado = "False"

# Defino la función password que pide una contraseña al usuario y devuelve si es válida o no
# Permite salir mediante la palabra "exit"
# La función recorre un diccionario con clave cada condición y valor inicial False. Compara con los requisitos
# a cumplir y si cumple alguno sustituye el False por un True. Sólo devuelve un True si se cumplen todas las 
# condiciones. Puede devolver False, True o Exit, por ello el return se le define como string.
def password (comprobaciones):
    clave = str(input('''\nIntroduzca una clave que cumpla:\n
        - Tiene una longitud entre 6 y 12 caradcteres.\n
        - Contiene:\n
            - Al menos una mayuscula.\n
            - Al menos un número.\n
            - Al menos un caracter especial que sea + ó - ó * ó /.\n
        - El primer caracter es alfabético.\n
        O ESCRIBA exit PARA SALIR:  ))

    if clave != "exit":
        comprobaciones["long"] = len(clave) >= 6 and len(clave) <= 12
        comprobaciones["primer"] = str(clave[0].isalpha())
        for n in clave:
            if comprobaciones["cap"] == "False": comprobaciones["cap"] = str(n.isupper())
            if comprobaciones["num"] == "False": comprobaciones["num"] = str(n.isdigit())
            if n ==  "+" or n == "-" or n == "*" or n == "/": comprobaciones["especial"] = "True"
        
        for valores in comprobaciones:
            if comprobaciones[valores] == "False": 
                analisis = "False"
                break
        else: analisis = "True"
    else: analisis = "fin"
    
    return str(analisis)


# Mi programa funciona mientras no se le introduzca "exit"

mail = str(input("\nIntroduzca un correo electrónico: "))
while mail != "exit":
    # Si el mail es válido:
    if  ("@" in mail) and (".com" in mail):
        print ("\nEl correo introducido es válido")

        # Mientras la función password no valide la contraseña (resultado False)
        while resultado == "False":
            # Defino un diccionario con cada una de las condiciones y su estado
            valido = {"long":"False", "cap": "False", "num":"False", "especial":"False", "primer":"False"}
            # La función password me devuelve si la contraseña es o no correcta o si el usuario quiere salir
            resultado = password(valido)
            
            if resultado == "True": 
                print("\n¡Registrado con éxito!")
                mail = "exit"
            elif resultado == "fin": 
                mail = "exit"
                break
            else: print("\nERROR. Contraseña no cumple con los requisitos")

    #Si no tiene las condiciones de mail válido:   
    else: 
        mail = str(input("\nERROR. Introduzca un correo electrónico válido o escriba exit para salir: "))
print("\n\n======== FIN DE PROGRAMA ==========\n")


# EJERCICIO 8 REGISTROS DE USUARIO
"""


"""
print("Bienvenido al registro de usuario:")

print("Introduzca un correo valido:")
email=str(input())
def validarCorreo(email):
    valido= False
    if "@" in email and ".com" in email:
	    valido=True
    else:
        valido= False
        return valido   
while validarCorreo(email)==False:
    print("Introduzca un correo valido el anterior era erroneo:")
    email=str(input())


def validarPass(passw):
    especial=['$', '@', '#', '%','+' ,'ó' ,'-' ,'ó', '*', 'ó' ,'/']
    valido = False
    if len(passw) < 6 or len(passw) > 12:
        print("Asegurate de que la contraseña sea entre 6 y 12 caracteres")
        valido=False
    elif not passw[0].isalpha():
        print("Asegurate de que el primer caracter de la contraseña es una letra")    
        valido=False
    elif  not any(char.isdigit() for char in passw):
        print("Asegurate de que  la contraseña tenga un numero como se pide")
        valido=False
    elif not  any(char.isupper() for char in passw):
        print("Asegurate de que la contraseña tenga mayusculas,una al menos como se indica")
        valido=False
    elif not any(char in especial for char in passw): 
        print('Asegurate de poner un caracter especial en la contraseña $@#') 
        valido = False
    else:
        print("contraseña y usuarios correctos")
        valido=True
    return valido


print("Introduzca una contaseña valida que empiece por una letra, con almenos una mayuscula, un numero y caracter especial:")
passw=input()

while validarPass(passw)==False:
    print("introduzca una contraseña valida como se le pide:")
    passw=str(input())
print("Se registro correctamente")
"""
