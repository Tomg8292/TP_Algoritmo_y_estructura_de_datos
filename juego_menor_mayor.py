import random

racha=0
nombre = input("ingrese el nombre de usuario: ")

while racha >= 0:
    numero = random.randint(1,1000)
    print(numero)

    mayomin= input("Cree que el numero es mayor o menor? ").lower()
    numeroant= numero
    numero = random.randint(1,1000)
    if mayomin == "mayor":
        if numero > numeroant:
            print("=================================================")
            print(f"El numero es mayor {nombre}, ganaste!!")
            print("=================================================")
            racha +=1
        else:
            print("=================================================")
            print(f"El numero es menor {nombre}, perdiste!!")
            print(f"Tu racha de victorias fue de {racha}!!")
            print("=================================================")
            racha = -1
    elif mayomin == "menor":
        if numero < numeroant:
            print("=================================================")
            print(f"El numero es menor {nombre}, ganaste!!")
            print("=================================================")
            racha +=1
        else:
            print("=================================================")
            print(f"El numero es mayor {nombre}, perdiste!!")
            print(f"Tu racha de victorias fue de {racha}!!")
            print("=================================================")
            racha = -1
