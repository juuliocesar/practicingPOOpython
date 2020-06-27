"""
la capacidad de una subclase de heredar de múltiples
superclases

Esto conlleva un problema, y es que si varias superclases
tienen los mismos atributos o métodos, la subclase sólo
podrá heredar de una de ellas.

En estos casos Python dará prioridad a las clases más a
la izquierda en el momento de la declaración de la subclase
"""


class A:
    def __init__(self):
        print("Soy de clase A")
    def a(self):
        print("Este método lo heredo de A")

class B:
    def __init__(self):
        print("Soy de clase B")
    def b(self):
        print("Este método lo heredo de B")

class C(A,B):
    def c(self):
        print("Este método es de C")


c = C()
c.a()
c.b()
c.c()

