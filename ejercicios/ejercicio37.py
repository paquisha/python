#Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
#Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.
x1 = 1
suma1 = 0
x2 = 1
suma2 = 0
while x1 <= 15:
    num = int(input("ingrese numeros de lista 1:"))
    suma1 = suma1 + num
    x1 = x1 + 1

while x2 <= 15:
    num1 = int(input("ingrese numeros de lista 2:"))
    suma2 = suma2 + num1
    x2 = x2 + 1

if suma1 > suma2:
    print("lista 1 mayor")
else:
    if suma2 > suma1:
        print("lista 2 mayor")
    else:
        print("listas iguales")
