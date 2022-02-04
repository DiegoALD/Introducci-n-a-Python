from clase_vehiculo import *

"""
taxi_1100 = Taxi("4875DER", "Skoda", 100, 1100)
taxi_2330 = Taxi("5232BSA", "Toyota", 150, 2330)
print(taxi_1100.__str__())
print(taxi_2330.__str__())
taxi_1100.tuneoElMotor(2)
taxi_2330.tuneoElMotor(4)
print(taxi_1100.__str__())
print(taxi_2330.__str__())
"""

"""
autobus_27 = Autobus("8123ACR", "Pagaso", 1100, 60)
autobus_32 = Autobus("3956ESA", "Ivecco", 1500, 70)
print(autobus_27.__str__())
print(autobus_32.__str__())
autobus_27.tuneoElMotor(2, autobus_27)
autobus_32.tuneoElMotor(4, autobus_32)
print(autobus_27.__str__())
print(autobus_32.__str__())
"""

# Variable públicas y privas (__)
vehiculo_Antonio = Vehiculo("9877DSA", "Mercedes", 220)
print(vehiculo_Antonio.__str__())
print(vehiculo_Antonio.variable_publica)
# print(vehiculo_Antonio.__variable_privada) No funciona por ser una variable privada
print(vehiculo_Antonio.getVariablePrivada())
