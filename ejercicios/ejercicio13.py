#Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar un mensaje indicando si el número tiene uno o dos dígitos.(Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)
num = int(input("ingrese numero: "))
if num >= 10 :
    print("tiene mas de dos digitos: ")
    print(num)
else:
    print("solo tiene un digito:")
    print(num)