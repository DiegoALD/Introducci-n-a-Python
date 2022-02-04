# Presentación y Concatenación de streams en print

texto1 = "Madrid"
texto2 = "Valencia"
texto3 = "Bilbao"
numero1 = 10

print("Modo 1 de concatenación")
print(texto1 + "            " + texto2 + " " + texto3)
print()
print("Modo 2 de concatenación")
print(f"{texto1}          {texto2}  {texto3}  {numero1}")
print()
print("Modo 3 de concatenación")
print("formador: {}, {}, año: {}".format(texto1,texto3,numero1))
print()
print("Modo 4 de concatenación")
print(texto1,texto2,texto3,numero1)
print()