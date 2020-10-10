cantidadPreguntas = int(input("ingrese la cantidad total de preguntas: "))
correctas = int(input("ingrese la cantidad de preguntas correctas: "))
porcentaje = correctas * 100 / cantidadPreguntas
if porcentaje >= 90 :
    print("nivel maximo")
else:
    if porcentaje >= 75 and porcentaje < 90:
        print("nivel medio")
        print(porcentaje)
    else:
        if porcentaje >= 50 and porcentaje < 75:
            print("nivel regular")
            print(porcentaje)
        else:
            print("fuera de nivel")
            print(porcentaje)