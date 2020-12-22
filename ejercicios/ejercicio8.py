#Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas y el valor por hora.
horasTrabajadas = float(input("ingrese la cantidad de horas trabajadas: "))
valorHora = float(input("ingrese el costo de la hora: "))
sueldoTotal = horasTrabajadas * valorHora
print("el sueldo mensual es:")
print(sueldoTotal)