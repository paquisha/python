num = int(input("ingrese numero: "))
if num > 0: 
    if num < 10 :
        print(num)
        print("tiene una cifras")
    else:
        if num < 100 :
            print(num)
            print("tiene dos cifras")
        else:
            print(num)
            print("tiene tres cifras")
else:
    print("solo numero positivos: ")
    
