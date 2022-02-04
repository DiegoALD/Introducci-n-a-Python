"""
    - Hacer un programa que tenga una lista de 10 números enteros:
    - Recorres la lista y mostrarla.
    - Hacer una función que recorra listas de números y devuelva un string
    - Ordenarla y mostrarla
    - Mostrar su longitud
    - Buscar algún elemento (que el usuario pida por teclado)
"""

"""
lista=[0,6,7,8,9,1,2,3,4,5,]

def mostrarLista(lista):
    for x in lista:
        print(x)

def mostrarString(lista):
    for x in lista:
         print(str(x))
def ordenar(lista):
    lista.sort() 
    return print(lista)     
def longitud(lista):
    longitud=len(lista)
    return print("la lista contiene "+str(longitud)+" elementos"  )  
def buscar(lista):
    print("Introduce que elemento quieres ver si pertenece a la lista:")
    busca=input()
    if not busca in lista:
        return print("El elemento " + str(busca) + " existe") 
    else:
        return print("El elemento " + str(busca) + "no existe")
mostrarLista(lista)
print("ya" +'\n')
mostrarString(lista) 
print("ya" +'\n')
ordenar(lista)
print("ya" +'\n')
longitud(lista)
print("ya" +'\n')
buscar(lista)  
"""


def prueba(parametro):
    print("\n")
    print(type(parametro))
    print(parametro)

prueba({"nombre": "Mario", "edad": 35})
prueba([1, 2, 3 ,4])
prueba("Antonio")
prueba((1, 2, 3, 4))