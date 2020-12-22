#Podemos observar lo siguiente: Siempre se hace la carga del sueldo, pero si el sueldo que ingresamos supera 3000 dolares se mostrará por pantalla el mensaje "Esta persona debe abonar impuestos", en caso que la persona cobre 3000 o menos no aparece nada por pantalla.
sueldo = int(input("ingrese el sueldo del operario: "))
if sueldo >= 3000 :
    print("debe pagar impuestos")