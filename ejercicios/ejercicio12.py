#Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado".
nota1 = float(input("ingrese nota 1: "))
nota2 = float(input("ingrese nota 2:"))
nota3 = float(input("ingrese nota 3:"))
promedio = (nota1 + nota2 + nota3)/3
if promedio >= 7:
    print("aprobado: ")
    print(promedio)
else:
    print("reprobado: ")
    print(promedio)