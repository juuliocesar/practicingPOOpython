"""
Una clase heredada puede fácilmente extender algunas funcionalidades, 
simplemente añadiendo nuevos atributos y métodos, o sobreescribiendo los 
ya existentes.
"""


class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format( self.color, self.ruedas )

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "color {}, {} km/h, {} ruedas, {} cc".format( self.color, self.velocidad, self.ruedas, self.cilindrada )

coche = Coche("azul", 150, 4, 1200)
print(coche)


"""
El inconveniente más evidente de ir sobreescribiendo es que
tenemos que volver a escribir el código de la superclase y 
luego el específico de la subclase.
"""