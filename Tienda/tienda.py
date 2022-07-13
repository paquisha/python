import sys
nombres = []
edades = []
tallas = []
residencias = []
emails = []
precios = []
cantidades_vendidas = []

while True:
    print("""
=========================
    sistema ventas
=========================
""")
    eleccion = input("""
1 - Ingrese datos
2 - Hacer una venta
3 - Mostrar información
4 - Borrar un artículo
5 - Salir
Seleccione: """)
    if eleccion == "1":
        nombre = input("Ingrese nombre: ")
        edad = input("Ingrese edad: ")
        talla = input("Ingrese tallas: ")
        residencia = input("Ingrese lugar de residencia: ")
        email = input("Ingrese email: ")
        precio = float(input("Precio del producto: "))
        cantidad_vendida = 0.0
        nombres.append(nombre)
        edades.append(edad)
        tallas.append(talla)
        residencias.append(residencia)
        emails.append(email)
        precios.append(precio)
        cantidades_vendidas.append(cantidad_vendida)
    elif eleccion == "2":
        nombre_articulo = input("Nombre del artículo que se vende: ")
        if nombre_articulo in nombres:
            cantidad = float(input("Cantidad vendida: "))
            indice = nombres.index(nombre_articulo)
            precio = precios[indice]
            cantidades_vendidas[indice] += cantidad
            print(
                f"Se vende(n) {cantidad} {nombre_articulo}. Total: {cantidad * precio}")
        else:
            print("El artículo no existe")
    elif eleccion == "3":
        if len(nombres) <= 0:
            print("No hay artículos")
            continue
        # Los nombres de artículos
        articulo_mas_vendido = nombres[0]
        articulo_menos_vendido = nombres[0]
        articulo_con_mas_ingresos = nombres[0]
        articulo_con_menos_ingresos = nombres[0]
        # Pero también necesitamos el conteo. Simplemente los inicializamos en un elemento del arreglo
        mas_vendido = cantidades_vendidas[0]
        menos_vendido = cantidades_vendidas[0]
        con_mas_ingresos = cantidades_vendidas[0] * precios[0]
        con_menos_ingresos = cantidades_vendidas[0] * precios[0]
        print("+--------------------+---------+---------+--------------------+--------------------+----------+----------+----------+")
        print("|NOMBRE              |EDAD     |TALLA    |RESIDENCIA          |EMAIL               |CANT.     |PRECIO    |IMPORTE   |")
        print("+--------------------+---------+---------+--------------------+--------------------+----------+----------+----------+")
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
            print("|{:<20}|{:>10}|{:>10}{:<20}|{:<20}|{:>10.2f}|{:>10.2f}|{:>10.2f}|".format(
                nombre, edad, talla, residencia, email, cantidad_vendida, precio, importe))
            print("+--------------------+----------+----------+----------+")
            if cantidad_vendida > mas_vendido:
                mas_vendido = cantidad_vendida
                articulo_mas_vendido = nombre
            if cantidad_vendida < menos_vendido:
                menos_vendido = cantidad_vendida
                articulo_menos_vendido = nombre
            if importe > con_mas_ingresos:
                con_mas_ingresos = importe
                articulo_con_mas_ingresos = nombre
            if importe < con_menos_ingresos:
                con_menos_ingresos = importe
                articulo_con_menos_ingresos = nombre
            total += importe
            indice += 1

        print(
            "|--------------------|----------|----------|--------------------|--------------------|----------|----------|----------|TOTAL:    |{:>10.2f}|".format(total))
        print("+--------------------+----------+----------+--------------------+--------------------+----------+----------+----------+")
        print(
            f"Artículo más vendido: {articulo_mas_vendido}, con {mas_vendido} unidades")
        print(
            f"Artículo menos vendido: {articulo_menos_vendido}, con {menos_vendido} unidades")
        print(
            f"Artículo con más ingresos: {articulo_con_mas_ingresos}, con {con_mas_ingresos} euros")
        print(
            f"Artículo con menos ingresos: {articulo_con_menos_ingresos}, con {con_menos_ingresos} euros")
    elif eleccion == "4":
        nombre_articulo = input("Nombre del artículo que se elimina: ")
        if nombre_articulo in nombres:
            indice = nombres.index(nombre_articulo)
            del nombres[indice]
            del precios[indice]
            del cantidades_vendidas[indice]
            print(f"Se elimina {nombre_articulo}")
        else:
            print("El artículo no existe")


    elif eleccion == "5":
        if input("Seguro (s/n): ") == "s":
            sys.exit()

    
