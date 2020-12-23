#En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.
sueldo1 = 0
sueldo2 = 0
suma = 0
x = 1
n = int(input("Ingrese cantidad de empleados:"))
while x <= n:
    sueldo = float(input("ingrese sueldo:"))
    if sueldo > 300:
        sueldo1 = sueldo1 + 1
    else:
        sueldo2 = sueldo2 + 1
    suma = suma + sueldo
    x = x + 1
print("numero de empleados cobran mas de 300: ")
print(sueldo1)
print("numero de empleados cobran entre de 100 y 300: ")
print(sueldo2)
print("gasto de importe en sueldos:")
print(suma)
