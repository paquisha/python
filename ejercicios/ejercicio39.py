#Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base y la altura de un triángulo. 
# El programa deberá informar:
#a) De cada triángulo la medida de su base, su altura y su superficie.
#b) La cantidad de triángulos cuya superficie es mayor a 12.

numero = int(input("cuantos triangulos revisara:"))
cantidad = 0
for f in range(numero):
    base = int(input("Ingrese valor de la base: "))
    altura = int(input("Ingrese el valor de la altura: "))
    superficie = base * altura / 2
    print(superficie)
    if superficie >= 12:
        cantidad = cantidad + 1
print("la cantidad de triangulos con superficie mayor a 12 es: ")
print(superficie)
