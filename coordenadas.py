import math

class Punto():

    equis2v = 0
    ye2v = 0

    equis2d = 0
    ye2d = 0
  
  
    def __init__(self,equis=None,ye=None):
        if equis == None and ye==None:
            self.equis = 0
            self.ye = 0
        else:
            self.equis = equis
            self.ye = ye


    def __str__(self):
        return f"Punto ({self.equis},{self.ye})"

    def cuadrante(self):
        
        if self.equis == 0 and self.ye!=0:
            print("El Punto se encuentra en el eje de las Ys")
        
        elif self.equis != 0 and self.ye == 0:
            print("El Punto se encuentra en el eje de las Xs")

        elif self.equis > 0 and self.ye > 0:
            print("El Punto se encuentra en el primer cuadrante")

        elif self.equis < 0 and self.ye > 0:
            print("El Punto se encuentra en el segundo cuadrante")

        elif self.equis < 0 and self.ye < 0:
            print("El Punto se encuentra en el tercer cuadrante")

        elif self.equis > 0 and self.ye < 0:
            print("El Punto se encuentra en el cuarto cuadrante")

        else:
            print("El Punto esta en el origen")

    def vector(self,equis2v=None,ye2v=None):
            
        self.equis2v=equis2v
        self.ye2v=ye2v

        print(f"El vector es ({self.equis2v-self.equis},{self.ye2v-self.ye})")

    def distancia(self,equis2d=None,ye2d=None):
        
        self.equis2d=equis2d
        self.ye2d=ye2d
        a = math.sqrt(pow((self.equis2d-self.equis),2) + pow((self.ye2d-self.ye),2)) #Variable Local
        print(f"La distancia entre los dos puntos es {round(a,2)}")



puntoA = Punto(2,3)
print(puntoA)
puntoA.cuadrante()


puntoB = Punto(5,5)
print(puntoB)

puntoC = Punto(-3,-1)
print(puntoC)
puntoC.cuadrante()

puntoD = Punto(0,0)
print(puntoD)
puntoD.cuadrante()

puntoA.vector(5,5)
puntoB.vector(2,3)

puntoA.distancia(5,5)
puntoB.distancia(2,3)

puntoA.distancia(0,0)
puntoB.distancia(0,0)
puntoC.distancia(0,0)

