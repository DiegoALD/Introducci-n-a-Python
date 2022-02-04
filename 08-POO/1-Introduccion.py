# Programación Orientada a Objetos POO, Oriented Object Programing OOP

"""
Una vez que hemos aprendido la Programación Estructurada, vamos un paso más adelante 
utilizando la POO. La POO es un paredigma de programación en el cual los programas se 
basa en la representación de los objetos de de la vida cotidiana mediante clases.
Una clase es un molde que representa un determinado objeto.
La clase tiene:
    - Propiedades que representan las caracteristicas del objeto
    - Métodos que representan las acciones que puede realizar el objeto.
    - Ver ejemplos en los módulos clase_humano.py y clase_coche.py

class Clase()
    __init__(self, propiedades)  # constructor

    def metodos(self, parametros)


Caracteristicas que tiene la POO:

    - Abstración: con la POO podemos crear clases que describen 
    objetos con unas determinadas propiedades que hemos abstraido,
    no debenos conocer ni siquiera la clase, sólo que propiedades y
    métodos tiene. Ademas con relaciones entre clases padres e
    hijos podemos aumentar la abstracción que nos ofrete la POO
    - Herencia. 
        La herencia es la compartición entre clases de propiedades
        y metodos.
        Cuando declaras la clase hija pones () la clase padre

        class Hija(Padre):
            __init__(self, propiedades)
                super.__init__(self, propiedades)

                Si pones super() en lugar de Padre, hereda de la clase superior sin
                tener que nombrarla explicitamente, veremos un ejemplo.

                super().__init__()

    - Modularidad: 
    Las aplicaciones se dividen en módulos dedicados a realizar
    determinadas funciones por lo cual simplificamos mucho
    el desarrollo de las aplicaciones.
    - Ocultación:
        Uno de los paradigmas de la programación orientada a objetos es que cada clase debe tener acceso al 
        mínimo estricto de información necesaria para cumplir su función. Una gestión demasiado laxa del 
        acceso a la información puede provocar fallos, malentendidos en el código y dependencias innecesarias, 
        incluso perjudiciales para el proyecto. De ahí el interés de que las clases controlen la exposición 
        de sus miembros.

        Hay tres tipos de visibilidad, representadas por diferentes símbolos en UML:
        - Pública (símbolo +): el miembro es accesible para todas las demás clases del programa.
        - Protegida (símbolo #): el miembro es accesible solo para las clases derivadas de la clase en cuestión 
        (las clases derivadas se presentan en la sección Herencia). 
        - Privada (símbolo -): el miembro es accesible solo para la clase en cuestión.

        El interés de la visibilidad es controlar el acceso del resto del programa a los miembros de una clase. 
        Hay datos que deben ser accesibles en modo lectura, pero no en modo escritura, por ejemplo. En este 
        caso, es necesario no ofrecer una interfaz para modificar estos datos. O bien hay atributos que son 
        útiles solo para la clase que los define, para realizar cálculos complicados. La modificación de estos 
        atributos podría provocar un error de cálculo, de ahí el interés de enmascararlos. Y si no le interesan 
        a nadie...
        Con la estrate getters and setters, combinada con la 
        visibilidad de las variables, nos permite ocultar el 
        contenido de los objetos instanciados.
"""