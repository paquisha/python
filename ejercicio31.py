piezas = int(input("ingrese la cantidad de piezas: "))
cantidad = 0
x = 1 
while x <= piezas :
    largo = float(input("Ingrese la medida de la pieza: "))
    if largo >= 1.2 and largo <= 1.3 :
        cantidad = cantidad + 1
    x = x +1
print("la cantidad de piezas aptas son")
print(cantidad)