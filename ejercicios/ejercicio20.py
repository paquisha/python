dia = int(input("ingrese el dia: "))
mes = int(input("ingrese el mes: "))
anio = int(input("ingrese el a;o: "))
if mes == 1 or mes == 2 or mes == 3 :
    print("corresponde al primer trimestre del año", anio)
else:
    print("no corresponde al primer trimestre del año ", anio)