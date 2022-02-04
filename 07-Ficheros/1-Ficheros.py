import os

direc =os.getcwd()
print(direc)
archivo = open("remeras.txt", "w+") 
contenido = archivo.read() 
nombre = archivo.name 
print(nombre)
modo = archivo.mode
print(modo)
encoding = archivo.encoding
print(encoding)
archivo.write("Hola, soy Mario")

archivo.close() 
if archivo.closed: 
    print("El archivo se ha cerrado correctamente") 
else: 
    print("El archivo permanece abierto")