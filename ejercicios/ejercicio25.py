#Escribir un programa que pida ingresar la coordenada de un punto en el plano, es decir dos valores enteros x e y (distintos a cero).
#Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto. (1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)
x = int(input("ingrese el valor de x: "))
y = int(input("ingrese el valor de y: "))
if x > 0 and y > 0 :
    print("(",x,",",y,") pertenecen al primer cuadrante")
else:
    if x < 0 and y > 0 :
        print("(",x,",",y,") pertenecen al segundo cuadrante")
    else:
        if x < 0 and y < 0 :
           print("(",x,",",y,") pertenecen al tercer cuadrante")
        else:
            if x > 0 and y < 0 :
                print("(",x,",",y,") pertenecen al cuarto cuadrante")