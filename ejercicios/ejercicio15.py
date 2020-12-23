#Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos.
num1 = int(input("ingrese numero uno: "))
num2 = int(input("ingrese numero dos: "))
num3 = int(input("ingrese numero tres: "))
if num1 > num2 and num1 > num3 :
    print(num1)
    print("numero uno es mayor")
else:
    if num2 > num1 and num2 > num3:
        print(num2)
        print("numero dos es mayor")
    else:
        print(num3)
        print("numero tres es mayor");