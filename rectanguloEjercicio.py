class Rectangulo():

    def __init__(self,inicial1=None,inicial2=None,final1=None,final2=None):

        if inicial1==None and inicial2==None and final1==None and final2==None:
            self.inicial1  = 0
            self.inicial2  = 0
            self.final1  = 0
            self.final2  = 0
        else:
            self.inicial1  = inicial1
            self.inicial2  = inicial2
            self.final1  = final1
            self.final2  = final2

        print(f"Se crearon los puntos {self.inicial1,self.inicial2} y {self.final1,self.final2}")

    def __str__(self):
        return f"Se crearon los puntos {self.inicial1,self.inicial2} y {self.final1,self.final2}"
    

    def base(self):
        #print(f"La base del rectangulo es: {self.final1-self.inicial1}")
        return abs(self.final1-self.inicial1)
    def altura(self):
        #print(f"La altura es: {self.final2-self.inicial2}")
        return abs(self.final2-self.inicial2)
    def area(self):
        print(f"El área del rectangulo es: {self.base()*self.altura()}")

puntosR1 = Rectangulo(2,3,5,5)
print(puntosR1.base())
print(puntosR1.altura())
puntosR1.area()













