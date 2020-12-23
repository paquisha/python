#Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras y muestre un mensaje indicando si tiene 1, 2, o 3 cifras. Mostrar un mensaje de error si el número de cifras es mayor.
num = int(input("ingrese numero: "))
if num > 0: 
    if num < 10 :
        print(num)
        print("tiene una cifras")
    else:
        if num < 100 :
            print(num)
            print("tiene dos cifras")
        else:
            print(num)
            print("tiene tres cifras")
else:
    print("solo numero positivos: ")
    
