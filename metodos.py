#Son las funciones de las clases

class Galleta():
    chocolate = False

    def chocolatear(self):
        self.chocolate = True
        

galleta = Galleta() #Instancia
galleta.chocolatear() #Llamamos al método
print(galleta.chocolate)

"""
Sea como sea con este ejemplo podemos entender que por defecto
el valor de un atributo se busca en la clase, pero para
modificarlo en la instancia es necesario hacer referencia al 
objeto.
"""

