from usuarios import acciones

"""
	Proyecto Python MySQL
	- Abrir asistente
	- Login o registro
	- Si elegimos registro, creará un registro en la BBDD de MySQL
	- Si elegimos login, identifica el usuario y nos preguntará ¿qué queremos hacer?_
        - Crear una nota
        - Mostrar una nota o todas
        - Borrar una nota
"""

print("""
    Acciones disponibles:
    - registro
    - login
""")

hazEl = acciones.Acciones()
accion =input("¿Qué es lo que quieres hacer? ")

if accion == "registro":
    hazEl.registro()
elif accion == "login":
    hazEl.login()
else:
    print("Te has equivocado, vuelvelo a intentar")

