import os

descuentoGuayaquil = 30
contadorPrendaUno = 0
contadorPrendaDos = 0
contadorPrendaTres = 0
prendaUno = 10
prendaDos = 20
prendaTres = 30

nombre = input("Ingrese nombre: ")
edad = input("Ingrese edad: ")
talla = input("Ingrese talla: ")
residencia = input("Ingrese lugar de residencia: ")
email = input("Ingrese correo electronico: ")

print("""
=========================
1 - prendaUno = $10
2 - prendaDos = $20
3 - prendaTres = $30
=========================
""")
opcion = input("Escoja numero de prenda: ")
cantidad = float(input("Ingrese cantidad: "))

if opcion == "1":
    if residencia.lower() == "guayaquil":
        descuento = prendaUno * (descuentoGuayaquil/100)
        total = prendaUno - descuento
    else:
        total = prendaUno * cantidad
    contadorPrendaUno = contadorPrendaUno + 1
elif opcion == "2":
    if residencia.lower() == "guayaquil":
        descuento = prendaDos * (descuentoGuayaquil/100)
        total = prendaDos - descuento
    else:
        total = prendaDos * cantidad
    contadorPrendaDos = contadorPrendaDos + 1
elif opcion == "3":
    if residencia.lower() == "guayaquil":
        descuento = prendaTres * (descuentoGuayaquil/100)
        total = prendaTres - descuento
    else:
        total = prendaTres * cantidad
    contadorPrendaDos = contadorPrendaDos + 1
else:
    print("opcion invalida")
