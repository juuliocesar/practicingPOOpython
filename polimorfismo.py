from herencia import *

"""
El polimorfismo es una propiedad de la herencia por la que
objetos de distintas subclases pueden responder a una misma
acción.
"""

def rebajar_producto(producto, rebaja):
        producto.pvp = producto.pvp - (producto.pvp/100 * rebaja)

