#Se ingresan por teclado tres números, si al menos uno de los valores ingresados es menor a 10, imprimir en pantalla la leyenda "Alguno de los números es menor a diez".
num1 = int(input("ingrese numero uno: "))
num2 = int(input("ingrese numero dos: "))
num3 = int(input("ingrese numero tres: "))
if num1 < 10 and num2 < 10 and num3 < 10 :
    print("son menores a 10")
else:
    print("al menos uno es menor a 10")