#Se ingresan por teclado tres números, si todos los valores ingresados son menores a 10, imprimir en pantalla la leyenda "Todos los números son menores a diez".
num1 = int(input("ingrese numero uno: "))
num2 = int(input("ingrese numero dos: "))
num3 = int(input("ingrese numero tres: "))
if num1 < 10 and num2 < 10 and num3 < 10 :
    print("son menores a 10")
else:
    print("no son menores a 10")