#De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar un programa que lea los datos de entrada e informe:
#a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
#b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %.
#c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios.
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
