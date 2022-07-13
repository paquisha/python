#menu

import string


menuPrincipal = int(input("Menu Principal \n 1- opcion uno  \n 2- opcion dos \n 3-opcion tres \n 4- opcion cuatro \n 0- salir"))

while menuPrincipal != 0:
    if menuPrincipal == 1:
        nombre = input('ingrese nombre:')
        print(nombre)
    elif menuPrincipal == 2:
        print('dos')
    elif menuPrincipal == 3:
        print('tres')
    elif menuPrincipal == 4:
        print('cuatro')
    else:
        print('pro favor ingrese opcion correcta')
    
    menuPrincipal = int(input("Menu Principal \n 1- opcion uno  \n 2- opcion dos \n 3-opcion tres \n 4- opcion cuatro \n 0- salir"))
    