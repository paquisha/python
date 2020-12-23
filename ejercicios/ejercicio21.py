#Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde a Navidad.
dia = int(input("ingrese el dia: "))
mes = int(input("ingrese el mes: "))
anio = int(input("ingrese el a;o: "))
if dia == 25 and mes == 12 :
    print(dia,"-",mes,"-",anio)
    print("es Navidad")
else:
    print(dia,"-",mes,"-",anio)
    print("NO es navidad")