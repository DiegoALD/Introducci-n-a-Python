"""
Variable global, se declarada en la parte principal del programa y se puede utilizar
en cualuqier parte.
Variable local, se declara en la función y sólo se puede utilizar en la función. El valor se saca
con un return.
"""

def ejemplo():
    global frase  # Ahora el cambio de valor de frase es a nivel global
    frase = "Valor dentro de la funcion"
    print("Estamos dentro de la funcion")
    print(frase)

frase = "Valor global"
print("Fuera de la funcion primera vez")
print(frase)

ejemplo()

print("Fuera de la funcion segunda vez")
print(frase)