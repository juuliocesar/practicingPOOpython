"""
El constructor es un método que se llama automáticamente al 
crear un objeto, se define con el nombre init.
"""

class Galleta():
    #Atributos
    chocolate = False 

    #Constructor
    def __init__(self):  
        print("Se ha ejecutado el método")
        
    def chocolatear(self):
        self.chocolate = True
    
galleta = Galleta() #Realizamos la instancia
#galleta.chocolatear()

print(galleta.chocolate)



