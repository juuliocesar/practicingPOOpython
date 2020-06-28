class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format( self.color, self.ruedas )


class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self,color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

class Camioneta(Coche):

    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color,ruedas, velocidad,cilindrada)
        self.carga = carga
    
    def __str__(self):
        return super().__str__() + f",{self.carga} kg de carga"

class Bicicleta(Vehiculo):

    def __init__(self,color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return super().__str__() + f",{self.tipo}"


class Motocicleta(Bicicleta):

    def __init__(self):
        super().__init__(color,ruedas, velocidad, cilindrada, carga,tipo)




        






