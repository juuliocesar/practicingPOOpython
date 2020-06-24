"""
String
El método str es el que devuelve la representación de un objeto
en forma de cadena. Un momento en que se llama automáticamente
es cuando imprimimos una variable por pantalla.
"""


class Galleta:

    def __init__(self, sabor, color):
        self.sabor = sabor
        self.color = color

    def __str__(self):
       return f"Soy una galleta {self.color} y {self.sabor}."

galleta = Galleta("dulce", "blanca")

print(galleta)

