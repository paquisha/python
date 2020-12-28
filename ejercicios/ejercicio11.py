#Realizar un programa que solicite la carga por teclado de dos números, si el primero es mayor al segundo 
# informar su suma y diferencia, en caso contrario informar el producto y la división del primero respecto al segundo.
num1 = int(input("ingrese numero uno: "))
num2 = int(input("ingrese numero dos: "))
if num1 > num2:
    suma = num1 + num2
    resta = num1 - num2
    print("la suma es: ")
    print(suma)
    print("la resta es: ")
    print(resta)
else:
    multiplicacion = num1 * num2
    division = num1 // 2
    print("la multiplicacion es: ")
    print(multiplicacion)
    print("la division es: ")
    print(division)