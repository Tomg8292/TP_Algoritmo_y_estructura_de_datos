cont = 0
max = 6
gano = 0
contjugadas = 0
contvictorias = 0
contderrotas = 0
import random

nombre = input("ingrese el nombre de usuario: ")
numero = random.randint(1,100)

while cont < 6 and gano == 0:
    
    #print(numero) #
    print("te quedan", 6 - cont, "intentos")
    num = int(input("ingrese un numero: "))
    if num == numero:
        print("=================================================")
        print("descubriste el numero!!")
        cont += 1
        gano = 1
        contvictorias +=1
        print("descubriste el numero en", cont, "intentos")
        print("=================================================")
        
    if num > numero: 
        print("=================================================")
        print("el numero secreto es menor")
        cont += 1
    
    if num < numero:
        print("=================================================")
        print("el numero secreto es mayor")
        cont += 1

    if cont >= 6:
        print("=================================================")
        print("PERDISTE")
        print("el numero secreto era el", numero)
        print("=================================================")
        gano = 3
        contderrotas +=1


    if gano == 1 or gano == 3:
        contjugadas +=1
        print("cantidad de partidas jugadas: ", contjugadas)
        print("cantidad de partidas ganadas: ", contvictorias)
        print("cantidad de partidas perdidas: ", contderrotas)
        retry = input("volver a jugar? ").lower()
        print("=================================================")

        if retry == "si" and (gano == 1 or gano == 3):
            numero = random.randint(1,100)
            cont = 0
            gano = 0