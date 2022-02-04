from usuarios import acciones

"""
	Proyecto Python MySQL
	- Abrir asistente
	- Login o registro
	- Si elegimos registro, creará un registro en la BBDD
	- Si elegimos login, identifica el usuario y nos preguntará_
        - Crear nota, buscar nota o borrarla
"""




print("""
    Acciones disponibles:
    -   registro
    -   login
""")
hazEl = acciones.Acciones()
accion = input("¿Qué quieres hacer? ")
if accion == "registro":
    hazEl.registro()
    
elif accion == "login":
    hazEl.login()
