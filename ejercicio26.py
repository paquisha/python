sueldo = int(input("ingrese el sueldo: "))
antiguedad = int(input("ingrese los años de servicio: "))
if sueldo < 500 and antiguedad > 10 :
    aumento = 20 * sueldo / 100
    total = sueldo + aumento
    print("tiene un aumento del 20% ", aumento)
    print("total: ", total)
else:
    if sueldo < 500 and antiguedad < 10 :
       aumento = 5 * sueldo / 100
       total = sueldo + aumento
       print("tiene un aumento del 5% ", aumento)
       print("total: ", total)
    else:
        if sueldo >= 500 :
            print("total a recibir es: ", sueldo)
