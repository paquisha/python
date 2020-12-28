#Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente 
# información: cantidad total de preguntas que se le realizaron y la cantidad de preguntas que contestó correctamente. 
# Se pide confeccionar un programa que ingrese los dos datos por teclado e informe el nivel del mismo según el porcentaje 
# de respuestas correctas que ha obtenido, y sabiendo que:
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