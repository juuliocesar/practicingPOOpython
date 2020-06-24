class Galleta():
    chocolate = False


Galleta.chocolate=True

galleta = Galleta()


if galleta.chocolate:
    print("La galleta tiene chocolate")
else:
    print("La galleta no tiene chocolate")


#Para consultar el valor por defecto

print("Valor por defecto:",Galleta.chocolate)


