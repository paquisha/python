num1 = int(input("ingrese numero uno: "))
num2 = int(input("ingrese numero dos: "))
num3 = int(input("ingrese numero tres: "))
if num1 == num2 and num1 == num3 :
    operacion = (num1 + num2) * num3
    print("el resultado es: ")
    print(operacion)
else:
    print("no son iguales")