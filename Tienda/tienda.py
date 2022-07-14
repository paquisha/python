import sys
nombres = []
edades = []
tallas = []
residencias = []
emails = []
precios = []
descuentos = []
cantidades_vendidas = []
descuentoGuayaquil = 30
prendaUno = 10
prendaDos = 20
prendaTres = 30
contadorPrendaUno = 0
contadorPrendaDos = 0
contadorPrendaTres = 0
contadorPersonasGuayaquil= 0
contadorPersonas = 0
restoPais = 3

while True:
    print("""
=========================
    sistema ventas
=========================
""")
    eleccion = input("""
1 - Ingrese datos
2 - Estadisticas
3 - Mostrar información
4 - Salir
Seleccione: """)
    if eleccion == "1":
        nombre = input("Ingrese nombre: ")
        edad = input("Ingrese edad: ")
        talla = input("Ingrese talla: ")
        residencia = input("Ingrese lugar de residencia: ")
        email = input("Ingrese correo electronico: ")
        nombres.append(nombre)
        edades.append(edad)
        tallas.append(talla)
        residencias.append(residencia)
        emails.append(email)
        print("""
        =========================
        1 - prendaUno = $10
        2 - prendaDos = $20
        3 - prendaTres = $30
        =========================
        """)
        opcion = input("Escoja numero de prenda: ")
        cantidad = float(input("Ingrese cantidad: "))

        cantidad_vendida = 0.0

        if opcion == "1":
            if residencia.lower() == "guayaquil":
                descuento = prendaUno * (descuentoGuayaquil/100)
                total = prendaUno - descuento
                print("valor total: ")
                print(total)
                contadorPersonasGuayaquil = contadorPersonasGuayaquil + 1
            else:
                total = prendaUno * cantidad
                print("valor total: ")
                print(total)
                contadorPersonas = contadorPersonas + 1
            contadorPrendaUno = contadorPrendaUno + 1
        elif opcion == "2":
            if residencia.lower() == "guayaquil":
                descuento = prendaDos * (descuentoGuayaquil/100)
                total = prendaDos - descuento
                print("valor total: ")
                print(total)
                contadorPersonasGuayaquil = contadorPersonasGuayaquil + 1
            else:
                total = prendaDos * cantidad
                print("valor total: ")
                print(total)
                contadorPersonas = contadorPersonas + 1
            contadorPrendaDos = contadorPrendaDos + 1
        elif opcion == "3":
            if residencia.lower() == "guayaquil":
                descuento = prendaTres * (descuentoGuayaquil/100)
                total = prendaTres - descuento
                print("valor total: ")
                print(total)
                contadorPersonasGuayaquil = contadorPersonasGuayaquil + 1
            else:
                total = prendaTres * cantidad
                print("valor total: ")
                print(total)
                contadorPersonas = contadorPersonas + 1
            contadorPrendaDos = contadorPrendaTres + 1
        else:
            print("opcion invalida")
        precios.append(total)
        cantidades_vendidas.append(cantidad_vendida)
    elif eleccion == "2":
        print("estadisticas")
        print(f"cantidad de personas que obtuvieron descuento {contadorPersonasGuayaquil}\n")
        print(f"cantidad de personas que viven en guayaquil {contadorPersonasGuayaquil}\n")
        print(f"cantidad de personas que no residen en guayaquil {contadorPersonas}\n")
        print(f"talla mas vendida {contadorPersonas}\n")
        if contadorPrendaUno > contadorPrendaDos and contadorPrendaUno > contadorPrendaTres:
            print(f"prenda mas vendida, se vendio: {contadorPrendaUno} unidades\n")
            print(f"talla mas vendida uno {contadorPrendaUno}\n")
        elif contadorPrendaDos > contadorPrendaTres:
            print(f"prenda mas vendida, se vendio: {contadorPrendaDos} unidades\n")
            print(f"talla mas vendida dos {contadorPrendaDos}\n")
        else:
            print(f"prenda mas vendida, se vendio: {contadorPrendaTres} unidades\n")
            print(f"talla mas vendida tres {contadorPrendaTres}\n")
    elif eleccion == "3":
        if len(nombres) <= 0:
            print("No hay artículos")
            continue
        print("+--------------------+---------+---------+--------------------+--------------------+----------+----------+----------+-----------+")
        print("|NOMBRE              |EDAD     |TALLA    |RESIDENCIA          |EMAIL               |CANT.     |PRECIO    |V.RECAUDADO|V.AGREGADO|")
        print("+--------------------+---------+---------+--------------------+--------------------+----------+----------+-----------+----------+")
        indice = 0
        total = 0
        while indice < len(nombres):
            nombre = nombres[indice]
            edad = edades[indice]
            talla = tallas[indice]
            residencia = residencias[indice]
            email = emails[indice]
            precio = precios[indice]
            cantidad_vendida = cantidades_vendidas[indice]
            importe = precio * cantidad_vendida
            print("|{:<20}|{:>9}|{:>9}|{:<20}|{:<20}|{:>10.2f}|{:>10.2f}|{:>10.2f}|".format(
                nombre, edad, talla, residencia, email, cantidad_vendida, precio, importe))
            print("+--------------------+----------+----------+--------------------+--------------------+----------+----------+----------+----------+")
            total += importe
            indice += 1
    elif eleccion == "4":
        if input("Seguro (s/n): ") == "s":
            sys.exit()
