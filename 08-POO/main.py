# Importamos el módulo coche que contiene la clase Coche, sus propiedades y sus metodos
from clase_coche import *
from clase_humano import *

# Instanciamos, o sea, creamos y declaramos los objetos de la clase Coche
# coche1 = Coche("Volvo", "verde", 180, 5)  # Instacia (crear, declarar y dar valores a coche1)
coche2 = Coche("Seat", "azul", 150, 4)  # Instacia (crear, declarar y dar valores a coche2)
coche3 = Coche("Mercedes", "negro", 200, 7)  # Instacia (crear, declarar y dar valores a coche3)
coche4 = Coche("Fiat", "amarillo", 220, 3)  # Instacia (crear, declarar y dar valores a coche4)

"""
# Utilizamos los métodos getter y setter para ver valores y modificarlos
print("### Coche 1 ###")
print(coche1.getMarca())
print(coche1.getColor())
print(coche1.getVelocidad())
print(coche1.getPlazas())
print("### Coche 2 ###")
print(coche2.getMarca())
print(coche2.getColor())
print(coche2.getVelocidad())
print(coche2.getPlazas())
print("### Coche 3 ###")
print(coche3.getMarca())
print(coche3.getColor())
print(coche3.getVelocidad())
print(coche3.getPlazas())

print("### cambio coche 1 ###")
coche1.setMarca("Auid")
coche1.setColor("gris")
coche1.setVelocidad(250)
coche1.setPlazas(2)

print("### Nuevas expecificaciones de Coche 1 ###")
print(coche1.getColor())
print(coche1.getMarca())
print(coche1.getVelocidad())
print(coche1.getPlazas())

# Utilización de la función infoCoche
print("#### Info de Coche1 ####", coche1.infoCoche())
print("#### Info de Coche2 ####", coche2.infoCoche())
print("#### Info de Coche3 ####", coche3.infoCoche())
print("#### Info de Coche4 ####", coche4.infoCoche())

coche1.marca = "Renault"
print(coche1.marca)
"""
# print(coche1)
# print(coche1.__str__())

coche5 = Biplaza("Lamborguini", "rojo", 350, 2, False, False)
print(coche5.__str__())
coche5.acelerar()
coche5.acelerar()
coche5.acelerar()
coche5.abrir_el_techo(True)
print(coche5)
coche5.acelerarFuerte()
print(coche5)

"""
# Ejemplo de como variable pública y variable privada
print(coche2.variable_publica)
# print(coche2.__variable_privada)
print(coche2.getVariable_privada())
"""

