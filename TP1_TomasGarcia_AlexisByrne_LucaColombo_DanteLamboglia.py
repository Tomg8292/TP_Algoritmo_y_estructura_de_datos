"""
Integrantes:  Alexis Byrne, Tomás García, Dante Lamboglia y Luca Colombo
Declarativa de Variables utilizadas en el Programa Principal
opc: str
"""

import random
import os

cantjugadas_min_menor = 0
cantjugadas_num_secreto = 0
cantjugadas_par_impar = 0
cantvictorias_num_secreto = 0
cantvictorias_par_impar = 0
cantderrotas_num_secreto = 0
cantderrotas_par_impar = 0
nombreJugador = ""
MayorMenorRacha = 0

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
    print("   ▄▄▄▄███▄▄▄▄     ▄█  ███▄▄▄▄     ▄█       ▄█ ███    █▄     ▄████████   ▄██████▄   ▄██████▄     ▄████████ ")
    print(" ▄██▀▀▀███▀▀▀██▄ ███  ███▀▀▀██▄ ███      ███ ███    ███   ███    ███  ███    ███ ███    ███   ███    ███ ")
    print(" ███   ███   ███ ███▌ ███   ███ ███▌     ███ ███    ███   ███    █▀   ███    █▀  ███    ███   ███    █▀  ")
    print(" ███   ███   ███ ███▌ ███   ███ ███▌     ███ ███    ███  ▄███▄▄▄     ▄███        ███    ███   ███        ")
    print(" ███   ███   ███ ███▌ ███   ███ ███▌     ███ ███    ███ ▀▀███▀▀▀     ▀▀███ ████▄  ███    ███ ▀███████████ ")
    print(" ███   ███   ███ ███  ███   ███ ███      ███ ███    ███   ███    █▄   ███    ███ ███    ███          ███ ")
    print(" ███   ███   ███ ███  ███   ███ ███      ███ ███    ███   ███    ███  ███    ███ ███    ███    ▄█    ███ ")
    print("  ▀█   ███   █▀  █▀    ▀█   █▀  █▀   █▄ ▄███ ████████▀    ██████████  ████████▀   ▀██████▀   ▄████████▀  ")
    print("                                     ▀▀▀▀▀▀                                                            \n")
    
    print("........MENU PRINCIPAL........")
    print("A- Juego del menor-mayor")
    print("B- Adivinar el número secreto")
    print("C- Blackjack")
    print("D- Par o impar")
    print("E- Reporte")
    print("S- Salir del programa")

def cartel_construccion():
    """
    Variables locales: ninguna
    """
    print("\nJuego en construcción")
    input("Presione 'Enter' para retornar al menú principal...")
    limpiar_pantalla()

def mayor_menor():
    """
    Variables locales: mayomin: str, numero: int, numero_siguiente: int, racha: int
    """
    global MayorMenorRacha, cantjugadas_min_menor, nombreJugador
    racha = 0
    
    if nombreJugador == "":
        nombreJugador = input("Ingrese el nombre de usuario: ")
        
    numero = random.randint(1, 1000)
    cantjugadas_min_menor += 1
    
    while racha >= 0:
        print(f"\nNúmero actual: {numero}")
        mayomin = input("¿Cree que el siguiente número es 'Mayor' o 'Menor'? ").lower()
        
        while mayomin != "mayor" and mayomin != "menor":
            mayomin = input("Ingreso inválido. Escriba 'Mayor' o 'Menor': ").lower()
            
        numero_siguiente = random.randint(1, 1000)
        print(f"El siguiente número era: {numero_siguiente}")
        
        if mayomin == "mayor":
            if numero_siguiente > numero:
                print("=================================================")
                print(f"¡Ganaste esta ronda, {nombreJugador}!")
                print("=================================================")
                racha += 1
                numero = numero_siguiente
            else:
                print("=================================================")
                print(f"¡Perdiste, {nombreJugador}! Juego terminado.")
                print(f"Tu racha de victorias fue de {racha}!!")
                print("=================================================")
                if racha > MayorMenorRacha:
                    MayorMenorRacha = racha
                racha = -1
                
        elif mayomin == "menor":
            if numero_siguiente < numero:
                print("=================================================")
                print(f"¡Ganaste esta ronda, {nombreJugador}!")
                print("=================================================")
                racha += 1
                numero = numero_siguiente
            else:
                print("=================================================")
                print(f"¡Perdiste, {nombreJugador}! Juego terminado.")
                print(f"Tu racha de victorias fue de {racha}!!")
                print("=================================================")
                if racha > MayorMenorRacha:
                    MayorMenorRacha = racha
                racha = -1

    input("Presione ENTER para continuar...")

def numsecreto():
    """
    Variables locales: cont: int, gano: int, numero: int, num: int
    """
    global cantjugadas_num_secreto, cantvictorias_num_secreto, nombreJugador, cantderrotas_num_secreto
    cont = 0
    gano = 0

    if nombreJugador == "":
        nombreJugador = input("Ingrese el nombre de usuario: ")
        
    numero = random.randint(1, 100)
    cantjugadas_num_secreto += 1

    while cont < 6 and gano == 0:
        print("\nTe quedan ", 6 - cont, " intentos")
        num = input("Ingrese un número (1 al 100): ")
        
        # Validamos sin usar métodos de strings prohibidos, controlando los límites del rango
        while num < 1 or num > 100:
            num = input("Número fuera de rango. Reintente (1 al 100): ")
            
        if num == numero:
            print("=================================================")
            print("¡¡Descubriste el numero!!")
            cont += 1
            gano = 1
            cantvictorias_num_secreto += 1
            print("Descubriste el numero en ", cont, " intentos")
            print("=================================================")
        elif num > numero: 
            print("=================================================")
            print("El numero secreto es menor")
            cont += 1
        else:
            print("=================================================")
            print("El numero secreto es mayor")
            cont += 1

    if gano == 0:
        print("=================================================")
        print("PERDISTE")
        print("El numero secreto era el ", numero)
        print("=================================================")
        cantderrotas_num_secreto += 1

    input("Presione ENTER para continuar...")

def par_impar():
    """
    Variables locales: aciertos: int, numero: int, numero1: int, numero2: int, parOimpar: str
    """
    global cantjugadas_par_impar, cantvictorias_par_impar, nombreJugador, cantderrotas_par_impar
    aciertos = 0
    
    if nombreJugador == "":
        nombreJugador = input("Ingrese el nombre de usuario: ")
        
    cantjugadas_par_impar += 1
    
    while aciertos >= 0:
        numero2 = random.randint(1, 6)
        numero1 = random.randint(1, 6)
        numero = numero1 + numero2
        
        parOimpar = input("\n¿La suma de los dados es par o impar? ").lower()
        
        while parOimpar != "par" and parOimpar != "impar":
            parOimpar = input("Ingreso inválido, reintente (par/impar): ").lower()
            
        if numero % 2 == 0:
            if parOimpar == "par":
                print("=================================================")
                print(f"¡Acertaste {nombreJugador}! Salió {numero}.")
                print("=================================================")
                aciertos += 1
                cantvictorias_par_impar += 1
            else:
                print("=================================================")
                print(f"¡Perdiste {nombreJugador}! Salió {numero}.")
                print("=================================================")
                cantderrotas_par_impar += 1
                aciertos = -1
        else:
            if parOimpar == "impar":
                print("=================================================")
                print(f"¡Acertaste {nombreJugador}! Salió {numero}.")
                print("=================================================")
                aciertos += 1
                cantvictorias_par_impar += 1
            else:
                print("=================================================")
                print(f"¡Perdiste {nombreJugador}! Salió {numero}.")
                print("=================================================")
                cantderrotas_par_impar += 1
                aciertos = -1

    input("Presione ENTER para continuar...")

def reporte():
    """
    Variables locales: ninguna
    """
    print("=============================================")
    print("             REPORTE DE JUEGOS               ")
    print("=============================================")
    print(f"Jugador: {nombreJugador if nombreJugador != '' else 'Sin registrar'}")
    print(f"Mayor-Menor:    Partidas Jugadas: {cantjugadas_min_menor} | Mayor Racha: {MayorMenorRacha}")
    print(f"Número Secreto: Partidas Jugadas: {cantjugadas_num_secreto} | Ganadas: {cantvictorias_num_secreto} | Perdidas: {cantderrotas_num_secreto}")
    print(f"Par o Impar:    Partidas Jugadas: {cantjugadas_par_impar} | Ganadas: {cantvictorias_par_impar} | Perdidas: {cantderrotas_par_impar}")
    print("=============================================")

# ==========================================
# INICIO DEL PROGRAMA PRINCIPAL
# ==========================================

mostrar_advertencia()

opc = "" 

# Se inicia con la letra de control estructural solicitada (S)
while opc != "S": 
    MENU() 
    opc = input("\nIngrese su opcion: ").upper()

    # Validación de rango según plantilla exacta del FAQ de la cátedra
    while (opc < "A" or opc > "E" and opc != "S"): 
        opc = input("Ingreso Invalido - reintente: ").upper() 

    limpiar_pantalla() 

    match opc: 
        case "A": 
            mayor_menor() 
            limpiar_pantalla()
        case "B": 
            numsecreto() 
            limpiar_pantalla()
        case "C": 
            cartel_construccion() 
        case "D": 
            par_impar() 
            limpiar_pantalla()
        case "E": 
            reporte() 
            input("\nPresione 'Enter' para volver al menú...")
            limpiar_pantalla()
        case "S": 
            print("\nGracias por jugar, no apueste, juega por diversión")
            print("GRACIAS POR USAR NUESTRO SISTEMA!!!!")
            input("\nPresione 'Enter' para cerrar el programa...")