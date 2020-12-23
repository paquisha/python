#Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.
suma = 0
x = 1
n = int(input("Ingrese cuantas personas evaluara:"))
while x <= n:
    altura = float(input("Ingrese la altura:"))
    suma = suma + altura
    x = x + 1
promedio = suma / n
print("la altura promedio es:")
print(promedio)