

class Humano(object):

    def __init__(self, fecha_de_nacimiento, edad, padres, genero, peso, estatura, color_de_pelo, ojos):
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.edad = edad
        self.padres = padres
        self.genero = genero
        self.peso = peso
        self.estatura = estatura
        self.color_de_pelo = color_de_pelo
        self.ojos = ojos
            
    def getFecha_de_nacimiento(self):
        return self.fecha_de_nacimiento

    def setFecha_de_nacimiento(self, fecha_de_nacimiento):
        self.fecha_de_nacimiento = fecha_de_nacimiento

    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad

    def getPadres(self):
        return self.padres

    def setPadres(self, padres):
        self.padres = padres

    def getGenero(self):
        return self.genero

    def setGenero(self, genero):
        self.genero = genero

    def getPeso(self):
        return self.peso

    def setPeso(self, peso):
        self.peso = peso

    def getEstatura(self):
        return self.estatura

    def setEstatura(self, Estatura):
        self.Estatura = Estatura

    def getColor_de_pelo(self):
        return self.color_de_pelo

    def setColor_de_pelo(self, color_de_pelo):
        self.color_de_pelo = color_de_pelo

    def getOjos(self):
        return self.ojos

    def setOjos(self, ojos):
        self.ojos = ojos
    
    def correr(self):
        return "Estoy corriendo"

    def caminar(self):
        return "Estoy caminando"

    def hablar(self):
        return "Estoy hablando"

    def infoHumano(self):  # Simplemente crea un str con todas las propiedades en diferentes líneas
        info_humano = str("\n" + 
        str(self.fecha_de_nacimiento) + "\n" +
        str(self.edad) + "\n" +
        self.padres + "\n" +
        self.genero + "\n" +
        str(self.peso) + "\n" +
        str(self.estatura) + "\n" +
        self.color_de_pelo + "\n" +
        self.ojos + "\n")
        return info_humano

marcos = Humano("24/3/93", 26, "Rosa, Leonardo", "M", 69, 1.74, "rubio", "verdes")
marcos.fecha_de_nacimiento
print(marcos.getOjos())
print(marcos.getFecha_de_nacimiento())
print(marcos.fecha_de_nacimiento)
marcos.ojos = "azules"
marcos.setOjos("azules")
print(marcos.getOjos())
elisa = Humano({"dia":24, "mes":3, "año": 92}, 27, "Antonia y Martín", "F", 67, 1.64, "negro", "café")
elisa.fecha_de_nacimiento
print(elisa.fecha_de_nacimiento)
print(marcos.infoHumano())
print(elisa.infoHumano())

