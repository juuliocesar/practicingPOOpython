"""
La encapsulación consiste en denegar el acceso a los
atributos y métodos internos de la clase desde el exterior.
En Python no existe, pero se puede simular precediendo 
atributos y métodos con dos barras bajas __ como indicando
que son "especiales".
"""

class Ejemplo():
    __atributo_privado = "Soy un antributo inalcanzable desde afuera"

    def __metodo_privado(self):
        print("Soy un método priavdo")


    def atributo_publico(self):
        return self.__atributo_privado
    

e = Ejemplo()

print(e.atributo_publico())


