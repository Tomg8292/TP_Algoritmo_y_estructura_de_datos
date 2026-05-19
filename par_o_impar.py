import random
aciertos = 0
nombre = input("ingrese el nombre de usuario: ")
while aciertos >= 0:
    numero2 = random.randint(1,6)
    numero1 = random.randint(1,6)
    numero = numero1 + numero2
    parOimpar= input("¿que numero salio? ").lower()
    if numero % 2 == 0:
        if parOimpar == "par":
            print("=================================================")
            print(f"Acertaste {nombre}!!")
            print("=================================================")
            aciertos +=1
        else:
            print("=================================================")
            print(f"Perdiste {nombre}!!")
            print("=================================================")
            aciertos = -1
    else:
        if parOimpar == "impar":
            print("=================================================")
            print(f"Acertaste {nombre}!!")
            print("=================================================")
            aciertos +=1
        else:
            print("=================================================")
            print(f"Perdiste {nombre}!!")
            print("=================================================")
            aciertos = -1    