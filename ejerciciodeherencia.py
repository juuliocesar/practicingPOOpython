class Vehiculo():

    def __init__(self,color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):

        return f"color {self.color}, {self.ruedas} ruedas"

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):

        Vehiculo.__init__(self,color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + f", {self.velocidad} (km/h), {self.cilindrada} (cc)"

class Bicicleta(Vehiculo):

    def __init__(self,color,ruedas,tipo):
        Vehiculo.__init__(self,color,ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return Vehiculo.__str__(self) + f", {self.tipo} (urbana/deportiva)"

class Motocicleta(Bicicleta):

    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        Bicicleta.__init__(self,color,ruedas,tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Bicicleta.__str__(self) + f", {self.velocidad} velocidad, {self.cilindrada} cilindrada"        

class Camioneta(Coche):

    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga = carga
    
    def __str__(self):
        return Coche.__str__(self) + f", {self.carga}(Kg)"


mustang68 = Vehiculo("rojo/negro",4)
#print(mustang68)

neon = Coche("azul",4,90,1200)
#print(neon)

Diamondback = Bicicleta("negra",2,"urbana")
#print(Diamondback)

BMW1200 = Motocicleta("Negra",2,"deportiva",140,1200)
#print(BMW1200)

Suburban = Camioneta("negra",4,120,3446,752)
#print(Suburban)


vehiculos = [mustang68, neon, Diamondback, BMW1200, Suburban]

#Funcion que recibe la lista de vehiculos y los recorre
#mostrando el nombre de su clase y sus atributos.

def catalogar(lista=[]):
    for i in lista:
        print(type(i).__name__,": ", end=" ")
        print(i)
    
#catalogar(vehiculos)


def catalogar2(lista=[],ruedas=None):
    con = 0    
    if ruedas != None:
        for i in lista:
            if i.ruedas==ruedas:
                print(type(i).__name__,": ", end=" ")
                print(i)
                con+=1
        print(f"Se han encontrado {con} vehiculos con {ruedas} ruedas")      
    
    else:
        for i in lista:
            print(type(i).__name__,": ", end=" ")
            print(i)


catalogar2(vehiculos,2)








