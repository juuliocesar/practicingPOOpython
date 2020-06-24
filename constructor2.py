class Galleta():
    chocolate = False

    def __init__(self,sabor,color):
        self.sabor = sabor
        self.color = color
        print(f"Se creo una galleta de sabor {sabor} y color {color}")


galleta1 = Galleta("chocholate","café")
galleta2 = Galleta("vainilla","blanca")



