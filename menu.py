"""
Integrantes:  Alexis Byrne, Tomás García, Dante Lamboglia
Declarativa de Variables utilizadas en el Programa Principal
opc: int
"""

import random
import os

def limpiar_pantalla():
    """
    Variables locales: ninguna
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def mostrar_advertencia():
    """
    Variables locales: ninguna
    """
    print("=====================================================================")
    print("||                                                                 ||")
    print("||   ATENCION: LOS JUEGOS DE APUESTA ESTAN PROHIBIDOS PARA LOS     ||")
    print("||   MENORES Y ES PERJUDICIAL PARA LA SALUD.                       ||")
    print("||                                                                 ||")
    print("=====================================================================")
    
    input("\nPresione la tecla 'Enter' para continuar...")
    limpiar_pantalla()

def MENU():
    """
    Variables locales: ninguna
    """
    print("   ▄▄▄▄███▄▄▄▄    ▄█  ███▄▄▄▄    ▄█       ▄█ ███    █▄     ▄████████   ▄██████▄   ▄██████▄     ▄████████ ")
    print(" ▄██▀▀▀███▀▀▀██▄ ███  ███▀▀▀██▄ ███      ███ ███    ███   ███    ███  ███    ███ ███    ███   ███    ███ ")
    print(" ███   ███   ███ ███▌ ███   ███ ███▌     ███ ███    ███   ███    █▀   ███    █▀  ███    ███   ███    █▀  ")
    print(" ███   ███   ███ ███▌ ███   ███ ███▌     ███ ███    ███  ▄███▄▄▄     ▄███        ███    ███   ███        ")
    print(" ███   ███   ███ ███▌ ███   ███ ███▌     ███ ███    ███ ▀▀███▀▀▀    ▀▀███ ████▄  ███    ███ ▀███████████ ")
    print(" ███   ███   ███ ███  ███   ███ ███      ███ ███    ███   ███    █▄   ███    ███ ███    ███          ███ ")
    print(" ███   ███   ███ ███  ███   ███ ███      ███ ███    ███   ███    ███  ███    ███ ███    ███    ▄█    ███ ")
    print("  ▀█   ███   █▀  █▀    ▀█   █▀  █▀   █▄ ▄███ ████████▀    ██████████  ████████▀   ▀██████▀   ▄████████▀  ")
    print("                                     ▀▀▀▀▀▀                                                            \n")
    
    print("........MENU PRINCIPAL........")
    print("1- Juego del menor-mayor")
    print("2- Adivinar el número secreto")
    print("3- Blackjack")
    print("4- Par o impar")
    print("5- Reporte")
    print("6- Salir del programa")

def cartel_construccion():
    """
    Variables locales: ninguna
    """
    print("\nJuego en construcción")
    input("Presione 'Enter' para retornar al menú principal...")
    limpiar_pantalla()

def juego1():
    racha = 0
    nombre = input("Ingrese el nombre de usuario: ")

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

def juego2():
    cont = 0
    max = 6
    gano = 0
    contjugadas = 0
    contvictorias = 0
    contderrotas = 0

    nombre = input("Ingrese el nombre de usuario: ")
    numero = random.randint(1,100)

    while cont < 6 and gano == 0:
        
        #print(numero) #
        print("Te quedan ", 6 - cont, " intentos")
        num = int(input("Ingrese un numero: "))
        if num == numero:
            print("=================================================")
            print("Descubriste el numero!!")
            cont += 1
            gano = 1
            contvictorias +=1
            print("Descubriste el numero en ", cont, " intentos")
            print("=================================================")
            
        if num > numero: 
            print("=================================================")
            print("El numero secreto es menor")
            cont += 1
        
        if num < numero:
            print("=================================================")
            print("El numero secreto es mayor")
            cont += 1

        if cont >= 6:
            print("=================================================")
            print("PERDISTE")
            print("El numero secreto era el ", numero)
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
             

def juego4():
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

    input("Presione ENTER para continuar...")
      

def reporte():
    pass 

# ==========================================
# INICIO DEL PROGRAMA PRINCIPAL
# ==========================================

mostrar_advertencia()

opc = 0 

while opc != 6: 
    MENU() 
    opc = int(input("\nIngrese su opcion (1-6): "))

    while opc < 1 or opc > 6: 
        opc = int(input("Ingreso Invalido - reintente (1-6): ")) 

    limpiar_pantalla() 

    match opc: 
        case 1: 
            juego1() 
            limpiar_pantalla()
        case 2: 
            juego2() 
            limpiar_pantalla()
        case 3: 
            cartel_construccion() 
        case 4: 
            juego4() 
            limpiar_pantalla()
        case 5: 
            reporte() 
            input("\nPresione 'Enter' para volver al menú...")
            limpiar_pantalla()
        case 6: 
            print("\nGracias por jugar, no apueste, juega por diversión")
            input("Presione 'Enter' para cerrar...")