# Definiendo una clase

class Coche(object):
    # Atributos o propiedades
    # Cuando utilizamos constructor ya no tenemos que instanciar los atributos
    """
    marca = "Volvo"
    color = "verde"
    velocidad = 180
    plazas = 5
    """
 

    # Métodos o funciones
    # Constructor, es la función que estancia las variables de esta clase
    def __init__(self, marca, color, velocidad, plazas):
        self.marca = marca
        self.color = color
        self.velocidad = velocidad
        self.plazas = plazas

    def getMarca(self):  # Devuelve la propiedad marca del objeto asociado.
        return self.marca

    def setMarca(self, marca):  # Cambia la propiedad marca y pone la del parametro.
        self.marca = marca

    def getColor(self):  # Devuelve la propiedad color del objeto asociado.
        return self.color

    def setColor(self, color):  # Cambia la propiedad color y pone la del parametro.
        self.color = color

    def getVelocidad(self):  # Devuelve la propiedad velocidad del objeto asociado.
        return self.velocidad

    def setVelocidad(self, velocidad):  # Cambia la propiedad velocidad y pone la del parametro.
        self.velocidad = velocidad

    def getPlazas(self):  # Devuelve la propiedad plazas del objeto asociado.
        return self.plazas

    def setPlazas(self, plazas):  # Cambia la propiedad plazas y pone la del parametro.
        self.plazas = plazas

    def infoCoche(self):  # Simplemente crea un str con todas las propiedades en diferentes líneas
        info_coche = str("\n" + self.marca + "\n" +
        self.color + "\n" +
        str(self.velocidad) + "\n" +
        str(self.plazas))
        return info_coche

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def __str__(self):
        cadena = str("\n" + self.marca + "\n" +
        self.color + "\n" +
        str(self.velocidad) + "\n" +
        str(self.plazas))
        return cadena

class Biplaza(Coche):
    """
    techo_descapotable
    puertas_gaviota
    """
    def __init__(self, marca, color, velocidad, plazas, techo_descapotable, puertas_gaviota):
        Coche.__init__(self, marca, color, velocidad, plazas)
        self.techo_descapotable = techo_descapotable
        self.puertas_gaviota = puertas_gaviota

    def __str__(self):
        cadena = str("\n" + self.marca + "\n" +
        self.color + "\n" +
        str(self.velocidad) + "\n" +
        str(self.plazas) + "\n" +
        str(self.techo_descapotable) + "\n" +
        str(self.puertas_gaviota))
        return cadena

    def abrir_el_techo(self, abrir_techo):
        self.techo_descapotable = abrir_techo

    def cerrar_el_techo(self, cerrar_techo):
        self.techo_descapotable = cerrar_techo

    def frenarFuerte(self):
        super().frenar()
        super().frenar()
        super().frenar()

    def acelerarFuerte(self):
        super().acelerar()
        super().acelerar()
        super().acelerar()