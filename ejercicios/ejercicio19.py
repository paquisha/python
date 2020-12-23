#Confeccionar un programa que lea por teclado tres números enteros distintos y nos muestre el mayor.
num1 = int(input("ingrese numero uno: "))
num2 = int(input("ingrese numero dos: "))
num3 = int(input("ingrese numero tres: "))
if num1 > num2 and num1 > num3 :
    print(num1)
    print("es mayor")
else:
    if num2 > num3 :
        print(num2)
        print("es mayor")
    else:
        print(num3)
        print("es mayor")