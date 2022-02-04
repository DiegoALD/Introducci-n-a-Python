def dar_bienvenida(nombre):
    print(f"Bienvenido {nombre}")

def calculadora():

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

    