#Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares.
#Emplear el operador “%” en la condición de la estructura condicional (este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):
x = 1
acumuladorPar = 0
acumuladorImpar = 0
n = int(input("ingrese cantida a evaluar:"))
while x <= n:
    num = int(input("ingrese numeros:"))
    if num%2==0:
        acumuladorPar = acumuladorPar + 1
    else:
        acumuladorImpar = acumuladorImpar + 1
    x = x + 1
print("valores pares:")
print(acumuladorPar)
print("valor de impares")
print(acumuladorImpar)
