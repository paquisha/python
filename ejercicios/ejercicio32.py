#Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.
contador = 0
acumulador = 0
x = 1
while x <= 10:
    notas = int(input("Ingrese nota: "))
    if notas >= 7:
        acumulador = acumulador + 1
    else:
        contador = contador + 1
    x = x + 1
print("la cantidad de estudiantes con notas mayores a 7 es: ")
print(acumulador)
print("la cantidad de estudiantes con notas menores a 7 es: ")
print(contador)