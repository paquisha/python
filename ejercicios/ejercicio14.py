#calculadora de notas
nota1 = float(input("ingrese nota 1 :"))
nota2 = float(input("ingrese nota 2 :"))
nota3 = float(input("ingrese nota 3: "))
promedio = (nota1+nota2+nota3)/3
if promedio >= 7 :
    print("promocionado")
    print(promedio)
else:
    if promedio >= 4:
        print("supletorio")
        print(promedio)
    else:
        print("reprobado")
        print(promedio)
