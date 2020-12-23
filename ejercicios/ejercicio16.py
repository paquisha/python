#Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo, negativo o nulo (es decir cero)
num = int(input("ingrese numero: "))
if num > 0 :
    print(num)
    print("es positivo")
else:
    if num < 0 :
        print(num)
        print("es negativo")
    else:
        print(num)
        print(" es cero")