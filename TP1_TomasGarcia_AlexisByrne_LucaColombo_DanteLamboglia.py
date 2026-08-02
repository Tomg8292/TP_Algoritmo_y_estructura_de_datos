"""
Integrantes: Alexis Byrne, Tomás García, Dante Lamboglia y Luca Colombo
================================================================================
DECLARACIÓN DE VARIABLES Y ESTRUCTURAS DE DATOS (PROGRAMA PRINCIPAL)
================================================================================
- opc: str                         -> Guarda la opción elegida en el Menú Principal
- opc_rep: str                     -> Guarda la opción elegida en el Submenú de Reportes
- jugadores: list de str          -> Lista con los nombres de hasta 10 jugadores

ESTADÍSTICAS Y CRÉDITO POR JUGADOR (Listas paralelas asociadas por índice):
- racha_menor_mayor: list de int    -> Racha máxima en Juego Menor-Mayor (inicia en 0)
- jugadas_num_secreto: list de int  -> Cantidad de partidas en Número Secreto (inicia en 0)
- ganadas_num_secreto: list de int  -> Cantidad de victorias en Número Secreto (inicia en 0)
- perdidas_num_secreto: list de int -> Cantidad de derrotas en Número Secreto (inicia en 0)
- ganadas_blackjack: list de int    -> Cantidad de partidas ganadas en Blackjack (inicia en 0)
- jugadas_par_impar: list de int    -> Cantidad de partidas en Par o Impar (inicia en 0)
- ganadas_par_impar: list de int    -> Cantidad de victorias en Par o Impar (inicia en 0)
- credito_par_impar: list de int    -> Crédito de cada jugador para Par o Impar (inicia en $1000)
================================================================================
"""

import random
import os

# ==========================================
# ESTRUCTURAS DE DATOS (MÁXIMO 10 JUGADORES)
# ==========================================
jugadores = []  # Lista con los nombres de los jugadores ingresados

# Listas paralelas de estadísticas
racha_menor_mayor = [0] * 10
jugadas_num_secreto = [0] * 10
ganadas_num_secreto = [0] * 10
perdidas_num_secreto = [0] * 10
ganadas_blackjack = [0] * 10
jugadas_par_impar = [0] * 10
ganadas_par_impar = [0] * 10
credito_par_impar = [1000] * 10  # Crédito inicial de $1000 por jugador


# ==========================================
# FUNCIONES AUXILIARES Y SISTEMA
# ==========================================
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


def obtener_o_registrar_jugador():
    """
    Variables locales: nombre: str, idx: int, i: int
    """
    nombre = input("Ingrese su nombre de jugador: ").strip()
    while nombre == "":
        nombre = input("El nombre no puede estar vacío. Reintente: ").strip()

    # Buscar si el jugador ya ingresó antes
    idx = -1
    for i in range(len(jugadores)):
        if jugadores[i].lower() == nombre.lower():
            idx = i

    # Registro de nuevo jugador si hay cupo
    if idx == -1:
        if len(jugadores) < 10:
            jugadores.append(nombre)
            idx = len(jugadores) - 1
            print(f"¡Bienvenido/a {nombre}! Te has registrado como el jugador #{len(jugadores)}.")
        else:
            print("¡ATENCIÓN! No hay cupos disponibles. Ya se alcanzó el límite de 10 jugadores.")
            return -1
    else:
        print(f"¡Hola de nuevo, {jugadores[idx]}!")

    return idx


def MENU():
    """
    Variables locales: ninguna
    """
    print("   ▄▄▄▄███▄▄▄▄     ▄█  ███▄▄▄▄     ▄█       ▄█ ███    █▄     ▄████████   ▄██████▄   ▄██████▄     ▄████████ ")
    print(" ▄██▀▀▀███▀▀▀██▄ ███  ███▀▀▀██▄ ███      ███ ███    ███   ███    ███  ███    ███ ███    ███   ███    ███ ")
    print(" ███   ███   ███ ███▌ ███   ███ ███▌     ███ ███    ███   ███    █▀   ███    █▀  ███    ███   ███    █▀  ")
    print(" ███   ███   ███ ███▌ ███   ███ ███▌     ███ ███    ███  ▄███▄▄▄     ▄███        ███    ███   ███        ")
    print(" ███   ███   ███ ███▌ ███   ███ ███▌     ███ ███    ███ ▀▀███▀▀▀     ▀▀███ ████▄ ███    ███ ▀███████████ ")
    print(" ███   ███   ███ ███  ███   ███ ███      ███ ███    ███   ███    █▄   ███    ███ ███    ███          ███ ")
    print(" ███   ███   ███ ███  ███   ███ ███      ███ ███    ███   ███    ███  ███    ███ ███    ███    ▄█    ███ ")
    print("  ▀█   ███   █▀  █▀    ▀█   █▀  █▀   █▄ ▄███ ████████▀    ██████████  ████████▀   ▀██████▀   ▄████████▀  ")
    print("                                     ▀▀▀▀▀▀                                                          \n")
    
    print("........MENU PRINCIPAL........")
    print("A- Juego del menor-mayor")
    print("B- Adivinar el número secreto")
    print("C- Blackjack")
    print("D- Par o impar")
    print("E- Reporte")
    print("F- Salir del programa")


# ==========================================
# JUEGO A: MENOR - MAYOR
# ==========================================
def jugar_menor_mayor():
    """
    Variables locales: idx_jugador: int, racha_actual: int, numero_actual: int,
                      numero_siguiente: int, eleccion: str, jugando: bool
    """
    idx_jugador = obtener_o_registrar_jugador()
    if idx_jugador == -1:
        input("Presione ENTER para continuar...")
        return

    print("\n--- JUEGO MENOR O MAYOR ---")
    racha_actual = 0
    numero_actual = random.randint(1, 1000)

    jugando = True
    while jugando:
        print(f"\nNúmero actual: {numero_actual}")
        eleccion = input("¿Crees que el siguiente número es 'Mayor' o 'Menor'?: ").strip().lower()

        while eleccion != "mayor" and eleccion != "menor":
            eleccion = input("Ingreso inválido. Escriba 'Mayor' o 'Menor': ").strip().lower()

        numero_siguiente = random.randint(1, 1000)
        print(f"El siguiente número fue: {numero_siguiente}")

        if numero_siguiente == numero_actual:
            print("¡Salió el mismo número! El juego continúa sin alterar la racha.")
        elif (eleccion == "mayor" and numero_siguiente > numero_actual) or \
             (eleccion == "menor" and numero_siguiente < numero_actual):
            print("=================================================")
            print(f"¡Acertaste, {jugadores[idx_jugador]}!")
            print("=================================================")
            racha_actual += 1
            numero_actual = numero_siguiente
        else:
            print("=================================================")
            print(f"¡Perdiste, {jugadores[idx_jugador]}! Juego terminado.")
            print(f"Tu racha de aciertos fue de: {racha_actual}")
            print("=================================================")
            jugando = False

    if racha_actual > racha_menor_mayor[idx_jugador]:
        racha_menor_mayor[idx_jugador] = racha_actual

    input("Presione ENTER para continuar...")


# ==========================================
# JUEGO B: NÚMERO SECRETO
# ==========================================
def jugar_numero_secreto():
    """
    Variables locales: idx_jugador: int, numero_secreto: int, intentos: int,
                      gano: bool, num: int, intentos_usados: int
    """
    idx_jugador = obtener_o_registrar_jugador()
    if idx_jugador == -1:
        input("Presione ENTER para continuar...")
        return

    print("\n--- ADIVINAR EL NÚMERO SECRETO ---")
    numero_secreto = random.randint(1, 100)
    intentos = 6
    gano = False

    jugadas_num_secreto[idx_jugador] += 1

    while intentos > 0 and not gano:
        print(f"\nTe quedan {intentos} intento(s).")
        num = int(input("Ingrese un número entre 1 y 100: "))

        while num < 1 or num > 100:
            num = int(input("Número fuera de rango (1-100). Reintente: "))

        if num == numero_secreto:
            gano = True
            intentos_usados = 7 - intentos
            print("=================================================")
            print(f"¡Felicidades {jugadores[idx_jugador]}! ¡Descubriste el número secreto!")
            print(f"Te llevó {intentos_usados} intento(s).")
            print("=================================================")
            ganadas_num_secreto[idx_jugador] += 1
        elif num > numero_secreto:
            print("El número secreto es MENOR.")
            intentos -= 1
        else:
            print("El número secreto es MAYOR.")
            intentos -= 1

    if not gano:
        print("=================================================")
        print(f"¡PERDISTE {jugadores[idx_jugador]}! Se agotaron tus intentos.")
        print(f"El número secreto era el: {numero_secreto}")
        print("=================================================")
        perdidas_num_secreto[idx_jugador] += 1

    input("Presione ENTER para continuar...")


# ==========================================
# JUEGO C: BLACKJACK (EL 21)
# ==========================================
def obtener_valor_carta(carta_num):
    """
    Variables locales: carta_num: int
    Calcula los puntos: 2-10 valen su número, J/Q/K (11,12,13) valen 10, As (1) vale 11 inicialmente.
    """
    if carta_num == 1:
        return 11
    elif carta_num >= 10:
        return 10
    else:
        return carta_num


def calcular_puntos(cartas_mano):
    """
    Variables locales: cartas_mano: list, puntos: int, ases: int, c: int, v: int
    Suma las cartas ajustando el valor del As (11 a 1) en caso de superar los 21 puntos.
    """
    puntos = 0
    ases = 0
    for c in cartas_mano:
        v = obtener_valor_carta(c)
        if c == 1:
            ases += 1
        puntos += v

    while puntos > 21 and ases > 0:
        puntos -= 10
        ases -= 1

    return puntos


def jugar_blackjack():
    """
    Variables locales: idx_jugador: int, quiere_jugar_otra: str, mazo: list,
                      cartas_jugador: list, cartas_banca: list, puntos_jugador: int,
                      puntos_banca: int, se_planto: bool, perdio_jugador: bool,
                      opcion: str, nueva_carta: int, nueva_carta_banca: int
    """
    idx_jugador = obtener_o_registrar_jugador()
    if idx_jugador == -1:
        input("Presione ENTER para continuar...")
        return

    quiere_jugar_otra = "S"

    while quiere_jugar_otra.upper() == "S":
        print("\n--- BLACKJACK (EL 21) ---")

        # Se arma un mazo único de 52 cartas sin repetición
        mazo = []
        for palo in range(4):
            for valor in range(1, 14):
                mazo.append(valor)

        random.shuffle(mazo)

        # Reparto de 2 cartas iniciales
        cartas_jugador = [mazo.pop(), mazo.pop()]
        cartas_banca = [mazo.pop(), mazo.pop()]

        puntos_jugador = calcular_puntos(cartas_jugador)
        print(f"\nTus cartas: {cartas_jugador} (Suma total: {puntos_jugador})")
        print(f"Carta visible de la Banca: {cartas_banca[0]}")

        se_planto = False
        perdio_jugador = False

        # --- TURNO JUGADOR ---
        while not se_planto and not perdio_jugador:
            if puntos_jugador == 21:
                print("¡Llegaste a 21!")
                se_planto = True
            else:
                opcion = input("¿Deseas 'Pedir' otra carta o 'Plantarte'?: ").strip().lower()
                while opcion != "pedir" and opcion != "plantarte":
                    opcion = input("Opción inválida. Ingrese 'Pedir' o 'Plantarte': ").strip().lower()

                if opcion == "pedir":
                    nueva_carta = mazo.pop()
                    cartas_jugador.append(nueva_carta)
                    puntos_jugador = calcular_puntos(cartas_jugador)
                    print(f"Obtuviste: {nueva_carta}. Tus cartas: {cartas_jugador} (Suma total: {puntos_jugador})")

                    if puntos_jugador > 21:
                        print("=================================================")
                        print("¡Te pasaste de 21! Perdiste automáticamente.")
                        print("=================================================")
                        perdio_jugador = True
                else:
                    se_planto = True

        # --- TURNO BANCA Y RESOLUCIÓN ---
        # Solo juega la banca si el jugador NO perdió automáticamente por pasarse de 21
        if not perdio_jugador:
            puntos_banca = calcular_puntos(cartas_banca)
            print(f"\nTurno de la Banca. Cartas de la Banca: {cartas_banca} (Suma: {puntos_banca})")
            
            # La Banca pide mientras tenga menos de 17 puntos
            while puntos_banca < 17:
                nueva_carta_banca = mazo.pop()
                cartas_banca.append(nueva_carta_banca)
                puntos_banca = calcular_puntos(cartas_banca)
                print(f"La banca pide carta... Cartas de la Banca: {cartas_banca} (Suma: {puntos_banca})")

            print("\n================ RESULTADO ================")
            print(f"Puntos de {jugadores[idx_jugador]}: {puntos_jugador}")
            print(f"Puntos de la Banca: {puntos_banca}")

            if puntos_banca > 21:
                print(f"¡La banca se pasó de 21! ¡Ganaste, {jugadores[idx_jugador]}!")
                ganadas_blackjack[idx_jugador] += 1
            elif puntos_jugador > puntos_banca:
                print(f"¡Ganaste, {jugadores[idx_jugador]}!")
                ganadas_blackjack[idx_jugador] += 1
            elif puntos_jugador < puntos_banca:
                print("Gana la Banca.")
            else:
                print("¡Es un Empate!")
            print("===========================================")

        quiere_jugar_otra = input("\n¿Deseas jugar otra partida de Blackjack? (S/N): ").strip()

    input("\nPresione ENTER para regresar al menú principal...")


# ==========================================
# JUEGO D: PAR O IMPAR
# ==========================================
def jugar_par_impar():
    """
    Variables locales: idx_jugador: int, credito: int, apuesta: int,
                      dado1: int, dado2: int, suma: int, eleccion: str, es_par: bool
    """
    idx_jugador = obtener_o_registrar_jugador()
    if idx_jugador == -1:
        input("Presione ENTER para continuar...")
        return

    print("\n--- PAR O IMPAR ---")
    credito = credito_par_impar[idx_jugador]

    if credito <= 0:
        print(f"Lo sentimos, {jugadores[idx_jugador]}, no te queda crédito ($0) para jugar.")
        input("Presione ENTER para continuar...")
        return

    print(f"Tu crédito disponible es: ${credito}")
    apuesta = int(input("Ingrese el monto a apostar: $"))

    while apuesta <= 0 or apuesta > credito:
        apuesta = int(input(f"Monto inválido. Debe ser entre $1 y ${credito}: $"))

    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma = dado1 + dado2

    eleccion = input("¿Crees que la suma de los dados es 'Par' o 'Impar'?: ").strip().lower()
    while eleccion != "par" and eleccion != "impar":
        eleccion = input("Opción inválida. Ingrese 'Par' o 'Impar': ").strip().lower()

    jugadas_par_impar[idx_jugador] += 1
    es_par = (suma % 2 == 0)

    print("=================================================")
    if (eleccion == "par" and es_par) or (eleccion == "impar" and not es_par):
        print(f"¡Ganaste, {jugadores[idx_jugador]}! Los dados sumaron {suma}.")
        credito += apuesta
        ganadas_par_impar[idx_jugador] += 1
    else:
        print(f"¡Perdiste, {jugadores[idx_jugador]}! Los dados sumaron {suma}.")
        credito -= apuesta

    credito_par_impar[idx_jugador] = credito
    print(f"Tu nuevo crédito actual es: ${credito}")
    print("=================================================")

    input("Presione ENTER para continuar...")


# ==========================================
# OPCIÓN E: REPORTE DE JUEGOS
# ==========================================
def reporte():
    """
    Variables locales: opc_rep: str, nombres: list, vics: list, creds: list,
                      total_v: int, n: int, i: int, j: int, nom_b: str, idx: int
    """
    opc_rep = ""
    while opc_rep != "e":
        limpiar_pantalla()
        print("........SUBMENÚ DE REPORTES........")
        print("a. Lista de jugadores ordenados por victorias (excepto Menor/Mayor)")
        print("b. Juegos e historial de un jugador puntual")
        print("c. Listado Par-Impar ordenado por crédito (Menor a Mayor)")
        print("d. Racha de un jugador en Menor/Mayor")
        print("e. Volver al menú principal")

        opc_rep = input("\nElija una opción (a-e): ").strip().lower()

        if opc_rep == "a":
            print("\n--- JUGADORES ORDENADOS POR VICTORIAS TOTALES ---")
            if len(jugadores) == 0:
                print("Aún no hay jugadores registrados.")
            else:
                nombres = list(jugadores)
                vics = []
                for i in range(len(jugadores)):
                    total_v = ganadas_num_secreto[i] + ganadas_blackjack[i] + ganadas_par_impar[i]
                    vics.append(total_v)

                # Ordenamiento Burbuja de mayor a menor
                n = len(nombres)
                for i in range(n - 1):
                    for j in range(n - 1 - i):
                        if vics[j] < vics[j + 1]:
                            vics[j], vics[j + 1] = vics[j + 1], vics[j]
                            nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]

                for i in range(len(nombres)):
                    print(f"{i+1}. {nombres[i]} - Total Victorias: {vics[i]}")
            input("\nPresione Enter para continuar...")

        elif opc_rep == "b":
            nom_b = input("\nIngrese el nombre del jugador a buscar: ").strip()
            idx = -1
            for i in range(len(jugadores)):
                if jugadores[i].lower() == nom_b.lower():
                    idx = i

            if idx == -1:
                print("El jugador ingresado no existe.")
            else:
                print(f"\n--- INFORMACIÓN DE {jugadores[idx]} ---")
                print(f"• Menor/Mayor: Racha máxima: {racha_menor_mayor[idx]}")
                print(f"• Número Secreto: Jugadas: {jugadas_num_secreto[idx]} | Ganadas: {ganadas_num_secreto[idx]} | Perdidas: {perdidas_num_secreto[idx]}")
                print(f"• Blackjack: Partidas ganadas: {ganadas_blackjack[idx]}")
                print(f"• Par o Impar: Jugadas: {jugadas_par_impar[idx]} | Aciertos: {ganadas_par_impar[idx]} | Crédito: ${credito_par_impar[idx]}")
            input("\nPresione Enter para continuar...")

        elif opc_rep == "c":
            print("\n--- JUGADORES PAR-IMPAR ORDENADOS POR CRÉDITO (MENOR A MAYOR) ---")
            if len(jugadores) == 0:
                print("Aún no hay jugadores registrados.")
            else:
                nombres = list(jugadores)
                creds = list(credito_par_impar[:len(jugadores)])

                # Ordenamiento Burbuja de menor a mayor
                n = len(nombres)
                for i in range(n - 1):
                    for j in range(n - 1 - i):
                        if creds[j] > creds[j + 1]:
                            creds[j], creds[j + 1] = creds[j + 1], creds[j]
                            nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]

                for i in range(len(nombres)):
                    print(f"{i+1}. {nombres[i]} - Crédito: ${creds[i]}")
            input("\nPresione Enter para continuar...")

        elif opc_rep == "d":
            nom_b = input("\nIngrese el nombre del jugador a buscar: ").strip()
            idx = -1
            for i in range(len(jugadores)):
                if jugadores[i].lower() == nom_b.lower():
                    idx = i

            if idx == -1:
                print("El jugador ingresado no existe.")
            else:
                print(f"\nLa mayor racha de {jugadores[idx]} en el juego Menor/Mayor es: {racha_menor_mayor[idx]}")
            input("\nPresione Enter para continuar...")


# ==========================================
# INICIO DEL PROGRAMA PRINCIPAL
# ==========================================
mostrar_advertencia()

opc = ""
while opc != "F":
    MENU()
    opc = str(input("Ingrese su opcion: ")).strip().upper()

    while (opc < "A" or opc > "F"):
        opc = str(input("Ingreso Inválido - reintente: ")).strip().upper()

    limpiar_pantalla()

    match opc:
        case "A":
            jugar_menor_mayor()
            limpiar_pantalla()
        case "B":
            jugar_numero_secreto()
            limpiar_pantalla()
        case "C":
            jugar_blackjack()
            limpiar_pantalla()
        case "D":
            jugar_par_impar()
            limpiar_pantalla()
        case "E":
            reporte()
            limpiar_pantalla()
        case "F":
            print("\nGracias por jugar, no apueste, juega por diversión")
            print('\n\n GRACIAS POR USAR NUESTRO SISTEMA!!!!')
            input("\nPresione 'Enter' para cerrar el programa...")