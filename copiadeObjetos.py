"""
De la misma forma que las colecciones, los objetos se pasan a 
las funciones por referencia. Si modificamos sus valores 
dentro, éstos se verán reflejados fuera.

Esto también afecta a la hora de hacer copias, creándose en su
lugar un acceso al objeto en lugar de uno nuevo con sus valores

"""
"""
Para realizar una copia a partir de sus valores podemos
utilizar la función copy del módulo con el mismo nombre
"""

from copy import copy

class Test:
    pass

test1 = Test()
test2 = copy(test1)

test1.algo = "Prueba"

print(test2 == test1)  # ¿Son el mismo objeto?

try:
    print(test2.algo)
except Exception as e:
    print(e)

