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