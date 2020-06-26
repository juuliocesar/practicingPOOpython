"""
Herencia: Es la capacidad de una clase de heredar los atributos
y métodos de otra clase, además de agregar los suyos propios
o modificar los heredados.
"""

class Producto:
    def __init__(self,referencia,nombre,pvp,descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion

    def __str__(self):
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t {self.pvp}\n" \
               f"DESCRIPCIÓN\t {self.descripcion}\n"


class Adorno(Producto):
    pass


class Alimento(Producto):
    productor = ""
    distribuidor = ""

    def __str__(self):
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t {self.pvp}\n" \
               f"DESCRIPCIÓN\t {self.descripcion}\n" \
               f"PRODUCTOR\t\t {self.productor}\n" \
               f"DISTRIBUIDOR\t\t {self.distribuidor}\n"


class Libro(Producto):
    isbn = ""
    autor = ""

    def __str__(self):
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t {self.pvp}\n" \
               f"DESCRIPCIÓN\t {self.descripcion}\n" \
               f"ISBN\t\t {self.isbn}\n" \
               f"AUTOR\t\t {self.autor}\n"


adorno = Adorno(2034, "Vaso adornado", 15, "Vaso de porcelana")
print(adorno)

alimento = Alimento(2035, "Botella de Aceite de Oliva", 5, "250 ML")
alimento.productor = "La Aceitera"
alimento.distribuidor = "Distribuciones SA"
print(alimento)

libro = Libro(2036, "Cocina Mediterránea",9, "Recetas sanas y buenas")
libro.isbn = "0-123456-78-9"
libro.autor = "Doña Juana"
print(libro)

#Podemos manejar objetos de distintas clases masivamente de una
#forma muy simple


productos = [adorno, alimento]
productos.append(libro)

print(productos)

for i in productos:
    print(i, "\n")

#También podemos acceder a los atributos, siempre que sean
#compartidos entre todos los objetos:

for producto in productos:
    print(producto.referencia, producto.nombre)

#Si un objeto no tiene el atributo al que queremos acceder nos 
#dará error


#La función isinstance() para determinar si una instancia/objeto
# es de una determinado clase
#El objeto libro pertenece a la clase Producto
print(isinstance(libro,Producto)) 


"""
for producto in productos:
    if( isinstance(producto, Adorno) ):
        print(producto.referencia, producto.nombre)
    elif( isinstance(producto, Alimento) ):
        print(producto.referencia, producto.nombre, producto.productor)
    elif( isinstance(producto, Libro) ):
        print(producto.referencia, producto.nombre, p.isbn)  
"""

print(alimento.pvp)

def rebajar_producto(producto, rebaja):
        producto.pvp = producto.pvp - (producto.pvp/100 * rebaja)

rebajar_producto(alimento,10)
print(alimento)
#cuando modificamos un atributo de un objeto dentro de una 
#función éste cambia en la instancia.

print(alimento.pvp)

