#Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la suma de los valores ingresados y su promedio.
x = 1
suma = 0 
while x <=10 :
    valor  = int(input("Ingrese un valor: "))
    suma = suma + valor
    x = x + 1
promedio = suma / 10
print("la suma de los 10 valores es")
print(suma)
print("el promedio es")
print(promedio)