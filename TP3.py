"""
Integrantes: Alexis Byrne, Tomás García, Dante Lamboglia y Luca Colombo
Comisión 103
Algoritmos y Estructuras de Datos - UTN FRRO
Trabajo Práctico Nro. 3 - 2026
Suite de Juegos "Azar y Lógica"

================================================================================
DECLARACIÓN DE VARIABLES Y ESTRUCTURAS DE DATOS (PROGRAMA PRINCIPAL)
================================================================================
- CARPETA_DATOS: str                  -> Ruta del directorio de archivos ('c:\\tp3\\')
- ArcFisiCat: str                     -> Ruta física del archivo Categorias.dat
- ArcFisiOpc: str                     -> Ruta física del archivo Opciones.dat
- ArcFisiJug: str                     -> Ruta física del archivo Jugadores.dat
- ArcLogCat: file                     -> Variable lógica para Categorias.dat
- ArcLogOpc: file                     -> Variable lógica para Opciones.dat
- ArcLogJug: file                     -> Variable lógica para Jugadores.dat
- CLAVE_ADMIN: str                    -> Contraseña fija para módulo de administración
- opc_menu: str                       -> Opción seleccionada en el Menú Principal
- jugador_actual: Jugador             -> Registro del jugador en la partida actual
- pos_jugador_actual: int             -> Posición en bytes del jugador en Jugadores.dat
================================================================================
"""

import pickle
import os
import os.path
import io
import random
import getpass


# ==============================================================================
# DEFINICIÓN DE REGISTROS (CLASES) SEGÚN TEORÍA DE LA CÁTEDRA
# ==============================================================================
class Categoria:
    def __init__(self):
        self.nro_categoria = 0          # int
        self.nombre_categoria = " "     # str (30 caracteres)
        self.pregunta = " "             # str (200 caracteres)
        self.estado = " "               # str (A/I)


class Opcion:
    def __init__(self):
        self.nro_categoria = 0          # int
        self.nro_opcion = 0             # int
        self.objeto = " "               # str (100 caracteres)
        self.valor = 0                  # int


class Jugador:
    def __init__(self):
        self.nombre = " "               # str (30 caracteres)
        self.creditos = 0.00            # float
        self.juegos = [[0] * 4 for i in range(2)]  # matriz de 2 x 4 de enteros


# ==============================================================================
# CONSTANTES Y VARIABLES GLOBALES DEL PROGRAMA
# ==============================================================================
CLAVE_ADMIN = "admin123"

CARPETA_DATOS = "c:\\tp3\\"
if not os.path.exists(CARPETA_DATOS):
    try:
        os.makedirs(CARPETA_DATOS)
    except Exception:
        CARPETA_DATOS = ""

ArcFisiCat = CARPETA_DATOS + "Categorias.dat"
ArcFisiOpc = CARPETA_DATOS + "Opciones.dat"
ArcFisiJug = CARPETA_DATOS + "Jugadores.dat"

ArcLogCat = None
ArcLogOpc = None
ArcLogJug = None

jugador_actual = None
pos_jugador_actual = -1


# ==============================================================================
# PROCEDIMIENTOS DE GESTIÓN Y FORMATEO DE REGISTROS
# ==============================================================================
def formatear_categoria(reg):
    """
    Formatea las cadenas del registro Categoria a longitud fija según teoría (slide 41).
    """
    reg.nombre_categoria = str(reg.nombre_categoria)[:30].ljust(30, " ")
    reg.pregunta = str(reg.pregunta)[:200].ljust(200, " ")
    reg.estado = str(reg.estado)[:1].ljust(1, " ")


def formatear_opcion(reg):
    """
    Formatea las cadenas del registro Opcion a longitud fija según teoría (slide 41).
    """
    reg.objeto = str(reg.objeto)[:100].ljust(100, " ")


def formatear_jugador(reg):
    """
    Formatea las cadenas del registro Jugador a longitud fija según teoría (slide 41).
    """
    reg.nombre = str(reg.nombre)[:30].ljust(30, " ")


# ==============================================================================
# APERTURA, CIERRE E INICIALIZACIÓN DE ARCHIVOS
# ==============================================================================
def abrir_archivos():
    """
    Abre o crea los archivos de acceso directo según teoría (slide 32).
    """
    global ArcLogCat, ArcLogOpc, ArcLogJug

    if not os.path.exists(ArcFisiCat):
        ArcLogCat = open(ArcFisiCat, "w+b")
    else:
        ArcLogCat = open(ArcFisiCat, "r+b")

    if not os.path.exists(ArcFisiOpc):
        ArcLogOpc = open(ArcFisiOpc, "w+b")
    else:
        ArcLogOpc = open(ArcFisiOpc, "r+b")

    if not os.path.exists(ArcFisiJug):
        ArcLogJug = open(ArcFisiJug, "w+b")
    else:
        ArcLogJug = open(ArcFisiJug, "r+b")


def cerrar_archivos():
    """
    Cierra los archivos lógicos al salir del programa (slide 32).
    """
    global ArcLogCat, ArcLogOpc, ArcLogJug
    if ArcLogCat is not None:
        ArcLogCat.close()
    if ArcLogOpc is not None:
        ArcLogOpc.close()
    if ArcLogJug is not None:
        ArcLogJug.close()


def inicializar_datos_si_vacio():
    """
    Carga al menos 3 categorías y 10 opciones por categoría si los archivos
    físicos se encuentran vacíos, garantizando el cumplimiento de la consigna.
    """
    global ArcLogCat, ArcLogOpc

    tam_cat = os.path.getsize(ArcFisiCat)
    if tam_cat == 0:
        # Categoría 1
        c1 = Categoria()
        c1.nro_categoria = 1
        c1.nombre_categoria = "Edad de Famosos"
        c1.pregunta = "¿Quién es mayor en edad (nació antes)?"
        c1.estado = "A"
        formatear_categoria(c1)
        ArcLogCat.seek(0, 2)
        pickle.dump(c1, ArcLogCat)

        # Categoría 2
        c2 = Categoria()
        c2.nro_categoria = 2
        c2.nombre_categoria = "Población de Países"
        c2.pregunta = "¿Qué país tiene más habitantes (millones)?"
        c2.estado = "A"
        formatear_categoria(c2)
        ArcLogCat.seek(0, 2)
        pickle.dump(c2, ArcLogCat)

        # Categoría 3
        c3 = Categoria()
        c3.nro_categoria = 3
        c3.nombre_categoria = "Duración de Películas"
        c3.pregunta = "¿Qué película dura más tiempo (minutos)?"
        c3.estado = "A"
        formatear_categoria(c3)
        ArcLogCat.seek(0, 2)
        pickle.dump(c3, ArcLogCat)

        ArcLogCat.flush()

    tam_opc = os.path.getsize(ArcFisiOpc)
    if tam_opc == 0:
        # 10 opciones de Categoría 1
        objs_cat1 = ["Lionel Messi", "Cristiano Ronaldo", "Tom Cruise", "Mirtha Legrand", "Guillermo Francella",
                     "Ricardo Darín", "Brad Pitt", "Keanu Reeves", "Shakira", "Mick Jagger"]
        vals_cat1 = [37, 39, 62, 97, 69, 67, 60, 60, 47, 81]
        for i in range(10):
            op = Opcion()
            op.nro_categoria = 1
            op.nro_opcion = i + 1
            op.objeto = objs_cat1[i]
            op.valor = vals_cat1[i]
            formatear_opcion(op)
            ArcLogOpc.seek(0, 2)
            pickle.dump(op, ArcLogOpc)

        # 10 opciones de Categoría 2
        objs_cat2 = ["Argentina", "Brasil", "Uruguay", "España", "México",
                     "Estados Unidos", "Japón", "Italia", "Alemania", "Chile"]
        vals_cat2 = [46, 215, 3, 48, 128, 335, 124, 59, 84, 19]
        for i in range(10):
            op = Opcion()
            op.nro_categoria = 2
            op.nro_opcion = i + 1
            op.objeto = objs_cat2[i]
            op.valor = vals_cat2[i]
            formatear_opcion(op)
            ArcLogOpc.seek(0, 2)
            pickle.dump(op, ArcLogOpc)

        # 10 opciones de Categoría 3
        objs_cat3 = ["Titanic", "El Padrino", "Avengers: Endgame", "Oppenheimer", "El Retorno del Rey",
                     "Jurassic Park", "Avatar", "Interestelar", "Toy Story", "Gladiador"]
        vals_cat3 = [195, 175, 181, 180, 201, 127, 162, 169, 81, 155]
        for i in range(10):
            op = Opcion()
            op.nro_categoria = 3
            op.nro_opcion = i + 1
            op.objeto = objs_cat3[i]
            op.valor = vals_cat3[i]
            formatear_opcion(op)
            ArcLogOpc.seek(0, 2)
            pickle.dump(op, ArcLogOpc)

        ArcLogOpc.flush()


# ==============================================================================
# PROCEDIMIENTOS Y FUNCIONES AUXILIARES DE SISTEMA
# ==============================================================================
def limpiar_pantalla():
    """
    Limpia la consola según el sistema operativo.
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def mostrar_advertencia():
    """
    Muestra el cartel reglamentario de advertencia sobre apuestas.
    """
    print("================================================================================")
    print("||                                                                            ||")
    print("||     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #        ||")
    print("||     #                                                             #        ||")
    print("||     #                         ATENCION                            #        ||")
    print("||     #                                                             #        ||")
    print("||     #    LOS JUEGOS DE APUESTAS ESTAN PROHIBIDOS PARA MENORES     #        ||")
    print("||     #                                                             #        ||")
    print("||     #    EL JUEGO COMPULSIVO ES PERJUDICIAL PARA LA SALUD         #        ||")
    print("||     #                                                             #        ||")
    print("||     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #        ||")
    print("||                                                                            ||")
    print("================================================================================")
    input("\nPresione la tecla 'Enter' para continuar...")
    limpiar_pantalla()


def MENU():
    """
    Muestra el menú principal iterativo.
    """
    print("================================================================================")
    print("                     SUITE DE JUEGOS 'AZAR Y LÓGICA'                            ")
    print("================================================================================")
    print("  a. Juego del menor-mayor")
    print("  b. Adivinar el número secreto")
    print("  c. Blackjack")
    print("  d. Par o impar")
    print("  e. Reporte")
    print("  f. Administración de Juegos")
    print("  g. Salir del programa")
    print("================================================================================")


# ==============================================================================
# GESTIÓN DE JUGADORES EN ARCHIVO DIRECTO (JUGADORES.DAT)
# ==============================================================================
def buscar_jugador(nombre):
    """
    Búsqueda secuencial sobre el archivo Jugadores.dat según teoría (slide 35).
    Retorna la posición en bytes (pos) o -1 si no existe.
    """
    pos = -1
    tam = os.path.getsize(ArcFisiJug)
    if tam > 0:
        ArcLogJug.seek(0, 0)
        encontrado = False
        while ArcLogJug.tell() < tam and not encontrado:
            pos_actual = ArcLogJug.tell()
            reg = pickle.load(ArcLogJug)
            if reg.nombre.strip().upper() == nombre.strip().upper():
                pos = pos_actual
                encontrado = True
    return pos


def identificar_jugador():
    """
    Procedimiento que solicita el nombre del jugador, lo busca en Jugadores.dat,
    y si no existe lo da de alta con $10.000 de crédito.
    Asigna las variables globales jugador_actual y pos_jugador_actual.
    """
    global jugador_actual, pos_jugador_actual

    nombre = input("\nIngrese su nombre de jugador: ").strip()
    while nombre == "":
        nombre = input("El nombre no puede estar vacío. Ingrese su nombre: ").strip()

    pos = buscar_jugador(nombre)
    if pos == -1:
        jugador_actual = Jugador()
        jugador_actual.nombre = nombre
        jugador_actual.creditos = 10000.00
        # matriz de juegos inicia en 0 por constructor
        formatear_jugador(jugador_actual)

        ArcLogJug.seek(0, 2)
        pos_jugador_actual = ArcLogJug.tell()
        pickle.dump(jugador_actual, ArcLogJug)
        ArcLogJug.flush()
        print("\n¡Bienvenido/a " + nombre + "! Registro creado con crédito inicial de $10.000,00.")
    else:
        pos_jugador_actual = pos
        ArcLogJug.seek(pos, 0)
        jugador_actual = pickle.load(ArcLogJug)
        print("\n¡Hola de nuevo, " + jugador_actual.nombre.strip() + "!")
        print("Crédito acumulado disponible: $" + str(round(jugador_actual.creditos, 2)))


def guardar_jugador_actual():
    """
    Procedimiento que actualiza el registro del jugador actual en Jugadores.dat
    según la técnica de modificación en archivo directo (slide 37).
    """
    global jugador_actual, pos_jugador_actual
    formatear_jugador(jugador_actual)
    ArcLogJug.seek(pos_jugador_actual, 0)
    pickle.dump(jugador_actual, ArcLogJug)
    ArcLogJug.flush()


def pedir_apuesta(credito_disponible):
    """
    Función que solicita y valida una apuesta numérica no mayor al crédito disponible.
    Devuelve un entero con el monto apostado.
    """
    entrada_valida = False
    monto = 0
    while not entrada_valida:
        cad = input("Ingrese el monto de créditos a apostar: $").strip()
        if cad.isdigit():
            monto = int(cad)
            if monto > 0 and monto <= credito_disponible:
                entrada_valida = True
            else:
                print("Monto inválido. Debe apostar entre $1 y $" + str(int(credito_disponible)) + ".")
        else:
            print("Entrada inválida. Ingrese solo números enteros positivos.")
    return monto


# ==============================================================================
# JUEGO A: MENOR - MAYOR
# ==============================================================================
def contar_categorias_activas():
    """
    Función que cuenta cuántas categorías activas ('A') existen en Categorias.dat.
    """
    cant = 0
    tam = os.path.getsize(ArcFisiCat)
    if tam > 0:
        ArcLogCat.seek(0, 0)
        while ArcLogCat.tell() < tam:
            reg = pickle.load(ArcLogCat)
            if reg.estado.strip() == "A":
                cant = cant + 1
    return cant


def contar_opciones_categoria(nro_cat):
    """
    Función que cuenta las opciones registradas para una categoría específica.
    """
    cant = 0
    tam = os.path.getsize(ArcFisiOpc)
    if tam > 0:
        ArcLogOpc.seek(0, 0)
        while ArcLogOpc.tell() < tam:
            reg = pickle.load(ArcLogOpc)
            if reg.nro_categoria == nro_cat:
                cant = cant + 1
    return cant


def jugar_menor_mayor():
    """
    Procedimiento del Juego Menor-Mayor.
    Cumple con el sistema de 6 rondas, categorías y opciones de archivos físicos,
    apuestas y actualización en Jugadores.dat.
    """
    global jugador_actual

    limpiar_pantalla()
    print("================================================================================")
    print("                       JUEGO DEL MENOR - MAYOR                                  ")
    print("================================================================================")

    identificar_jugador()

    if jugador_actual.creditos <= 0:
        print("\nAtención: No posees crédito ($0) para apostar en este juego.")
        input("Presione Enter para regresar al menú...")
    else:
        apuesta = pedir_apuesta(jugador_actual.creditos)

        cant_activas = contar_categorias_activas()
        if cant_activas == 0:
            print("\nNo hay categorías activas registradas en el sistema.")
            input("Presione Enter para regresar al menú...")
        else:
            print("\n--- CATEGORÍAS DISPONIBLES ---")
            tam_cat = os.path.getsize(ArcFisiCat)
            ArcLogCat.seek(0, 0)
            while ArcLogCat.tell() < tam_cat:
                c = pickle.load(ArcLogCat)
                if c.estado.strip() == "A":
                    print(str(c.nro_categoria) + ". " + c.nombre_categoria.strip())

            # Selección y validación de categoría
            cat_encontrada = False
            cat_elegida = None
            while not cat_encontrada:
                opc_cat = input("\nElija el número de categoría: ").strip()
                if opc_cat.isdigit():
                    nro_sel = int(opc_cat)
                    ArcLogCat.seek(0, 0)
                    while ArcLogCat.tell() < tam_cat and not cat_encontrada:
                        c = pickle.load(ArcLogCat)
                        if c.nro_categoria == nro_sel and c.estado.strip() == "A":
                            cat_encontrada = True
                            cat_elegida = c
                    if not cat_encontrada:
                        print("El número ingresado no corresponde a una categoría activa.")
                else:
                    print("Por favor, ingrese un número válido.")

            # Carga de opciones de la categoría a un arreglo estático de tamaño fijo
            cant_opc = contar_opciones_categoria(cat_elegida.nro_categoria)
            if cant_opc < 2:
                print("\nLa categoría seleccionada no tiene suficientes opciones (mínimo 2).")
                input("Presione Enter para regresar al menú...")
            else:
                arreglo_opc = [None] * cant_opc
                ArcLogOpc.seek(0, 0)
                tam_opc = os.path.getsize(ArcFisiOpc)
                idx_carga = 0
                while ArcLogOpc.tell() < tam_opc:
                    op_reg = pickle.load(ArcLogOpc)
                    if op_reg.nro_categoria == cat_elegida.nro_categoria:
                        arreglo_opc[idx_carga] = op_reg
                        idx_carga = idx_carga + 1

                # Arreglo estático de tamaño fijo para registrar qué opciones ya aparecieron
                usados = [False] * cant_opc

                # Preparar las opciones iniciales sin repetir
                idx1 = random.randint(0, cant_opc - 1)
                usados[idx1] = True

                idx2 = random.randint(0, cant_opc - 1)
                while usados[idx2]:
                    idx2 = random.randint(0, cant_opc - 1)
                usados[idx2] = True

                op_actual = arreglo_opc[idx1]
                op_nueva = arreglo_opc[idx2]

                aciertos = 0
                ronda = 1
                limpiar_pantalla()

                while ronda <= 6:
                    print("================================================================================")
                    print("Categoría: " + cat_elegida.nombre_categoria.strip())
                    print("Ronda " + str(ronda) + " de 6 | Aciertos acumulados: " + str(aciertos))
                    print("================================================================================")
                    print("\nPregunta: " + cat_elegida.pregunta.strip())
                    print("1. " + op_actual.objeto.strip() + "  /  2. " + op_nueva.objeto.strip())

                    eleccion = input("\n¿Cuál opción responde a la pregunta? (1 o 2): ").strip()
                    while eleccion != "1" and eleccion != "2":
                        eleccion = input("Opción inválida. Ingrese 1 o 2: ").strip()

                    print("\n--- VALORES ---")
                    print(op_actual.objeto.strip() + " (" + str(op_actual.valor) + ")  /  " +
                          op_nueva.objeto.strip() + " (" + str(op_nueva.valor) + ")")

                    # Manejo de empate y verificación de respuesta correcta
                    if op_actual.valor == op_nueva.valor:
                        print(">> ¡EMPATE! Ambas opciones tienen el mismo valor (" + str(op_actual.valor) + ").")
                        print(">> Como los valores son iguales, tu respuesta se considera CORRECTA. Sumas 1 punto.")
                        aciertos = aciertos + 1
                        if eleccion == "1":
                            op_ganadora = op_actual
                        else:
                            op_ganadora = op_nueva
                    elif op_actual.valor > op_nueva.valor:
                        correcta = 1
                        op_ganadora = op_actual
                        if int(eleccion) == correcta:
                            print(">> ¡RESPUESTA CORRECTA! Sumas 1 punto.")
                            aciertos = aciertos + 1
                        else:
                            print(">> RESPUESTA INCORRECTA. No sumas puntos.")
                    else:
                        correcta = 2
                        op_ganadora = op_nueva
                        if int(eleccion) == correcta:
                            print(">> ¡RESPUESTA CORRECTA! Sumas 1 punto.")
                            aciertos = aciertos + 1
                        else:
                            print(">> RESPUESTA INCORRECTA. No sumas puntos.")

                    # Preparar siguiente ronda si no es la última
                    if ronda < 6:
                        input("\nPresione Enter para continuar a la siguiente ronda...")
                        limpiar_pantalla()
                        op_actual = op_ganadora

                        # Verificar si quedan opciones sin usar en el arreglo
                        quedan_libres = False
                        for k in range(cant_opc):
                            if not usados[k]:
                                quedan_libres = True

                        # Si se utilizaron todas, se vuelven a habilitar las que no sean la opción actual
                        if not quedan_libres:
                            for k in range(cant_opc):
                                if arreglo_opc[k].objeto.strip() != op_actual.objeto.strip():
                                    usados[k] = False

                        # Buscar nueva opción que no haya aparecido previamente
                        idx_nuevo = random.randint(0, cant_opc - 1)
                        while usados[idx_nuevo]:
                            idx_nuevo = random.randint(0, cant_opc - 1)
                        usados[idx_nuevo] = True
                        op_nueva = arreglo_opc[idx_nuevo]

                    ronda = ronda + 1

                # Fin de las 6 rondas
                print("\n================================================================================")
                print("                        RESULTADO DE LA PARTIDA                                 ")
                print("================================================================================")
                print("Aciertos obtenidos: " + str(aciertos) + " de 6 rondas.")

                # Para ganar se deben contestar al menos 4 bien
                if aciertos >= 4:
                    print("¡FELICITACIONES! Has ganado la partida (4 o más correctas).")
                    jugador_actual.creditos = jugador_actual.creditos + apuesta
                    jugador_actual.juegos[0][0] = jugador_actual.juegos[0][0] + 1
                else:
                    print("HAS PERDIDO LA PARTIDA (menos de 4 correctas).")
                    jugador_actual.creditos = jugador_actual.creditos - apuesta
                    jugador_actual.juegos[1][0] = jugador_actual.juegos[1][0] + 1

                print("Crédito actualizado de " + jugador_actual.nombre.strip() + ": $" +
                      str(round(jugador_actual.creditos, 2)))
                guardar_jugador_actual()
                input("\nPresione Enter para regresar al menú principal...")


# ==============================================================================
# JUEGO B: NÚMERO SECRETO
# ==============================================================================
def jugar_numero_secreto():
    """
    Procedimiento del Juego Número Secreto.
    5 intentos para adivinar un número aleatorio entre 1 y 100.
    Actualiza la fila de ganadas/perdidas para el juego 1 en Jugadores.dat.
    """
    global jugador_actual

    limpiar_pantalla()
    print("================================================================================")
    print("                      ADIVINAR EL NÚMERO SECRETO                                ")
    print("================================================================================")

    identificar_jugador()

    numero_secreto = random.randint(1, 100)
    intentos_restantes = 5
    intentos_usados = 0
    adivino = False

    input("\nPresione Enter para comenzar los intentos...")
    limpiar_pantalla()

    while intentos_restantes > 0 and not adivino:
        print("================================================================================")
        print("Te quedan " + str(intentos_restantes) + " intento(s) para adivinar.")
        print("================================================================================")

        num_valido = False
        numero_usuario = 0
        while not num_valido:
            entrada = input("Ingrese un número entre 1 y 100: ").strip()
            if entrada.isdigit():
                numero_usuario = int(entrada)
                if numero_usuario >= 1 and numero_usuario <= 100:
                    num_valido = True
                else:
                    print("El número debe estar comprendido entre 1 y 100.")
            else:
                print("Entrada inválida. Ingrese solo números enteros.")

        intentos_usados = intentos_usados + 1

        if numero_usuario == numero_secreto:
            adivino = True
            print("\n¡FELICITACIONES " + jugador_actual.nombre.strip() + "! ¡Descubriste el número secreto!")
            print("Te llevó " + str(intentos_usados) + " intento(s).")
            jugador_actual.juegos[0][1] = jugador_actual.juegos[0][1] + 1
        else:
            intentos_restantes = intentos_restantes - 1
            if intentos_restantes > 0:
                if numero_secreto > numero_usuario:
                    print("El número que pensó la máquina es MAYOR.")
                else:
                    print("El número que pensó la máquina es MENOR.")
            print("")

    if not adivino:
        print("================================================================================")
        print("¡PERDISTE " + jugador_actual.nombre.strip() + "! Se agotaron los 5 intentos.")
        print("El número que pensó la máquina era: " + str(numero_secreto))
        print("================================================================================")
        jugador_actual.juegos[1][1] = jugador_actual.juegos[1][1] + 1

    guardar_jugador_actual()
    input("\nPresione Enter para regresar al menú principal...")


# ==============================================================================
# JUEGO C: BLACKJACK
# ==============================================================================
def nombre_figura_carta(num):
    """
    Función que devuelve la representación en texto de la carta (A, J, Q, K o número).
    """
    res = str(num)
    if num == 1:
        res = "A"
    elif num == 11:
        res = "J"
    elif num == 12:
        res = "Q"
    elif num == 13:
        res = "K"
    return res


def calcular_puntos_blackjack(mano, cant):
    """
    Función que suma los puntos de una mano de Blackjack considerando el valor del As (11 o 1).
    """
    puntos = 0
    ases = 0
    for i in range(cant):
        carta = mano[i]
        if carta == 1:
            ases = ases + 1
            puntos = puntos + 11
        elif carta >= 10:
            puntos = puntos + 10
        else:
            puntos = puntos + carta

    while puntos > 21 and ases > 0:
        puntos = puntos - 10
        ases = ases - 1

    return puntos


def mostrar_mano(cartas, cant):
    """
    Procedimiento para mostrar las cartas de una mano en formato legible.
    """
    texto = "["
    for i in range(cant):
        if i > 0:
            texto = texto + ", "
        texto = texto + nombre_figura_carta(cartas[i])
    texto = texto + "]"
    print(texto)


def jugar_blackjack():
    """
    Procedimiento del Juego Blackjack (El 21).
    Mazo de 52 cartas sin repetición, arreglos estáticos de tamaño fijo,
    reglas simplificadas de crupier y jugador, y registro en Jugadores.dat.
    """
    global jugador_actual

    limpiar_pantalla()
    print("================================================================================")
    print("                            BLACKJACK (EL 21)                                   ")
    print("================================================================================")

    identificar_jugador()

    otra_partida = "S"
    while otra_partida == "S":
        limpiar_pantalla()
        print("================================================================================")
        print("                     NUEVA PARTIDA DE BLACKJACK                                 ")
        print("================================================================================")

        # Creación del mazo de 52 cartas (arreglo de tamaño fijo)
        mazo = [0] * 52
        pos_mazo = 0
        for palo in range(4):
            for v in range(1, 14):
                mazo[pos_mazo] = v
                pos_mazo = pos_mazo + 1

        # Mezcla del mazo (sin repetición)
        for i in range(51, 0, -1):
            j = random.randint(0, i)
            aux = mazo[i]
            mazo[i] = mazo[j]
            mazo[j] = aux

        tope_mazo = 0

        # Reparto inicial: 2 al jugador y 2 a la banca
        cartas_jugador = [0] * 15
        cant_jug = 2
        cartas_jugador[0] = mazo[tope_mazo]
        tope_mazo = tope_mazo + 1
        cartas_jugador[1] = mazo[tope_mazo]
        tope_mazo = tope_mazo + 1

        cartas_banca = [0] * 15
        cant_ban = 2
        cartas_banca[0] = mazo[tope_mazo]
        tope_mazo = tope_mazo + 1
        cartas_banca[1] = mazo[tope_mazo]
        tope_mazo = tope_mazo + 1

        pts_jug = calcular_puntos_blackjack(cartas_jugador, cant_jug)

        print("\nTus cartas:")
        mostrar_mano(cartas_jugador, cant_jug)
        print("Puntuación actual: " + str(pts_jug))

        print("\nCarta visible de la Banca:")
        print("[" + nombre_figura_carta(cartas_banca[0]) + ", ?]")

        se_planto = False
        se_paso = False

        # Turno del Jugador
        while not se_planto and not se_paso:
            if pts_jug == 21:
                print("\n¡Alcanzaste 21 puntos! Pasa automáticamente el turno a la banca.")
                se_planto = True
            else:
                opc_accion = input("\n¿Deseas 'Pedir' otra carta o 'Plantarte'?: ").strip().upper()
                while opc_accion != "PEDIR" and opc_accion != "PLANTARTE":
                    opc_accion = input("Opción inválida. Ingrese 'Pedir' o 'Plantarte': ").strip().upper()

                if opc_accion == "PEDIR":
                    cartas_jugador[cant_jug] = mazo[tope_mazo]
                    tope_mazo = tope_mazo + 1
                    cant_jug = cant_jug + 1
                    pts_jug = calcular_puntos_blackjack(cartas_jugador, cant_jug)

                    print("\nHas recibido: " + nombre_figura_carta(cartas_jugador[cant_jug - 1]))
                    print("Tus cartas ahora:")
                    mostrar_mano(cartas_jugador, cant_jug)
                    print("Puntuación actual: " + str(pts_jug))

                    if pts_jug > 21:
                        print("================================================================================")
                        print("¡Te pasaste de 21 puntos! Pierdes automáticamente la partida.")
                        print("================================================================================")
                        se_paso = True
                else:
                    se_planto = True

        # Turno de la Banca si el jugador no se pasó
        if se_paso:
            jugador_actual.juegos[1][2] = jugador_actual.juegos[1][2] + 1
        else:
            pts_ban = calcular_puntos_blackjack(cartas_banca, cant_ban)
            print("\n--------------------------------------------------------------------------------")
            print("Turno de la Banca:")
            print("Cartas de la Banca:")
            mostrar_mano(cartas_banca, cant_ban)
            print("Puntos de la Banca: " + str(pts_ban))

            # La banca pide si tiene 16 o menos, se planta con 17 o más
            while pts_ban < 17:
                print("La banca tiene menos de 17. Debe pedir carta obligatoriamente...")
                cartas_banca[cant_ban] = mazo[tope_mazo]
                tope_mazo = tope_mazo + 1
                cant_ban = cant_ban + 1
                pts_ban = calcular_puntos_blackjack(cartas_banca, cant_ban)
                print("La banca recibió: " + nombre_figura_carta(cartas_banca[cant_ban - 1]))
                mostrar_mano(cartas_banca, cant_ban)
                print("Puntos de la Banca: " + str(pts_ban))

            print("\n========================= RESOLUCIÓN =========================")
            print("Tus puntos: " + str(pts_jug))
            print("Puntos de la Banca: " + str(pts_ban))

            if pts_ban > 21:
                print("¡La banca se pasó de 21! ¡Ganaste la partida!")
                jugador_actual.juegos[0][2] = jugador_actual.juegos[0][2] + 1
            elif pts_jug > pts_ban:
                print("¡Ganaste la partida! Superaste a la banca.")
                jugador_actual.juegos[0][2] = jugador_actual.juegos[0][2] + 1
            elif pts_jug < pts_ban:
                print("Gana la banca.")
                jugador_actual.juegos[1][2] = jugador_actual.juegos[1][2] + 1
            else:
                print("¡Empate! Mismo puntaje.")
            print("==============================================================")

        guardar_jugador_actual()

        otra_partida = input("\n¿Desea jugar otra partida de Blackjack? (S/N): ").strip().upper()
        while otra_partida != "S" and otra_partida != "N":
            otra_partida = input("Opción inválida. Ingrese 'S' para sí o 'N' para no: ").strip().upper()


# ==============================================================================
# JUEGO D: PAR O IMPAR
# ==============================================================================
def jugar_par_impar():
    """
    Procedimiento del Juego Par o Impar.
    Lanza dos números aleatorios del 1 al 6 (dados) y permite apostar crédito.
    Actualiza la fila de ganadas/perdidas y créditos del jugador en Jugadores.dat.
    """
    global jugador_actual

    limpiar_pantalla()
    print("================================================================================")
    print("                             PAR O IMPAR                                        ")
    print("================================================================================")

    identificar_jugador()

    if jugador_actual.creditos <= 0:
        print("\nNo tienes crédito disponible ($0) para apostar. Con cero ya no podrás jugar.")
        input("Presione Enter para regresar al menú...")
    else:
        print("\nCrédito disponible: $" + str(round(jugador_actual.creditos, 2)))
        apuesta = pedir_apuesta(jugador_actual.creditos)

        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2

        eleccion = input("\n¿Crees que la suma de los números es 'Par' o 'Impar'?: ").strip().upper()
        while eleccion != "PAR" and eleccion != "IMPAR":
            eleccion = input("Opción inválida. Ingrese 'Par' o 'Impar': ").strip().upper()

        es_par = (suma % 2 == 0)

        print("\n--- RESULTADO DE LOS DADOS ---")
        print("Dado 1: " + str(dado1) + " | Dado 2: " + str(dado2) + " -> Suma total: " + str(suma))

        if (eleccion == "PAR" and es_par) or (eleccion == "IMPAR" and not es_par):
            print("\n¡ACERTASTE! Ganaste $" + str(apuesta) + ".")
            jugador_actual.creditos = jugador_actual.creditos + apuesta
            jugador_actual.juegos[0][3] = jugador_actual.juegos[0][3] + 1
        else:
            print("\n¡NO ACERTASTE! Perdiste $" + str(apuesta) + ".")
            jugador_actual.creditos = jugador_actual.creditos - apuesta
            jugador_actual.juegos[1][3] = jugador_actual.juegos[1][3] + 1

        print("Tu nuevo crédito actual es: $" + str(round(jugador_actual.creditos, 2)))
        guardar_jugador_actual()
        input("\nPresione Enter para regresar al menú principal...")


# ==============================================================================
# OPCIÓN E: REPORTE
# ==============================================================================
def contar_total_jugadores():
    """
    Función que cuenta cuántos registros de jugadores hay almacenados en Jugadores.dat.
    """
    cant = 0
    tam = os.path.getsize(ArcFisiJug)
    if tam > 0:
        ArcLogJug.seek(0, 0)
        while ArcLogJug.tell() < tam:
            aux = pickle.load(ArcLogJug)
            cant = cant + 1
    return cant


def reporte():
    """
    Procedimiento del Submenú de Reportes.
    Permite ver listado ordenado por crédito (Falso Burbuja) o estadísticas por jugador.
    """
    opc_rep = ""
    while opc_rep != "C":
        limpiar_pantalla()
        print("================================================================================")
        print("                          SUBMENÚ DE REPORTES                                   ")
        print("================================================================================")
        print("  a. Lista de jugadores ordenados de mayor a menor por cantidad de créditos")
        print("  b. Juegos jugados por un jugador")
        print("  c. Volver al menú principal")
        print("================================================================================")

        opc_rep = input("\nElija una opción (a-c): ").strip().upper()
        while opc_rep != "A" and opc_rep != "B" and opc_rep != "C":
            opc_rep = input("Opción inválida. Ingrese A, B o C: ").strip().upper()

        if opc_rep == "A":
            limpiar_pantalla()
            print("================================================================================")
            print("     LISTA DE JUGADORES ORDENADOS POR CRÉDITO (MAYOR A MENOR)                   ")
            print("================================================================================")

            cant_jug = contar_total_jugadores()
            if cant_jug == 0:
                print("No hay jugadores registrados en el sistema.")
            else:
                # Arreglo estático de tamaño fijo para jugadores
                arr_jug = [None] * cant_jug
                ArcLogJug.seek(0, 0)
                for i in range(cant_jug):
                    arr_jug[i] = pickle.load(ArcLogJug)

                # Ordenamiento por método Falso Burbuja según teoría (slide 5 de Arreglos)
                for i in range(cant_jug - 1):
                    for j in range(i + 1, cant_jug):
                        if arr_jug[i].creditos < arr_jug[j].creditos:
                            aux = arr_jug[i]
                            arr_jug[i] = arr_jug[j]
                            arr_jug[j] = aux

                print("Puesto  |  Nombre del Jugador            |  Créditos Acumulados")
                print("----------------------------------------------------------------")
                for k in range(cant_jug):
                    nom_mostrar = arr_jug[k].nombre.strip().ljust(30, " ")
                    cred_mostrar = ("$" + str(round(arr_jug[k].creditos, 2))).rjust(15, " ")
                    print(str(k + 1).rjust(6, " ") + "  |  " + nom_mostrar + "  |  " + cred_mostrar)

            input("\nPresione Enter para continuar...")

        elif opc_rep == "B":
            limpiar_pantalla()
            print("================================================================================")
            print("                       HISTORIAL DE UN JUGADOR                                  ")
            print("================================================================================")

            nom_buscado = input("Ingrese el nombre del jugador a consultar: ").strip()
            while nom_buscado == "":
                nom_buscado = input("El nombre no puede estar vacío. Ingrese el nombre: ").strip()

            pos = buscar_jugador(nom_buscado)
            if pos == -1:
                print("\nEl jugador ingresado no existe en los registros.")
            else:
                ArcLogJug.seek(pos, 0)
                jug = pickle.load(ArcLogJug)

                print("\n----------------------------------------------------------------")
                print("Jugador: " + jug.nombre.strip())
                print("Créditos acumulados actuales: $" + str(round(jug.creditos, 2)))
                print("----------------------------------------------------------------")
                print("Detalle de partidas:")

                nombres_juegos = ["Juego del menor-mayor", "Número secreto", "Blackjack", "Par o impar"]
                for c in range(4):
                    ganadas = jug.juegos[0][c]
                    perdidas = jug.juegos[1][c]
                    total = ganadas + perdidas
                    print("\n- " + nombres_juegos[c] + ":")
                    if total == 0:
                        print("  Aún no ha disputado partidas en este juego.")
                    else:
                        print("  Partidas ganadas : " + str(ganadas))
                        print("  Partidas perdidas: " + str(perdidas))
                        print("  Total jugadas    : " + str(total))

            input("\nPresione Enter para continuar...")


# ==============================================================================
# OPCIÓN F: ADMINISTRACIÓN DE JUEGOS
# ==============================================================================
def alta_categoria():
    """
    Procedimiento para dar de alta una nueva categoría.
    Valida nombres repetidos, pregunta y asigna número consecutivo a partir del último.
    """
    limpiar_pantalla()
    print("================================================================================")
    print("                     ADMINISTRAR CATEGORÍAS - ALTA                              ")
    print("================================================================================")

    nom = input("Ingrese el nombre de la nueva categoría: ").strip()
    while nom == "":
        nom = input("El nombre no puede estar vacío. Ingrese el nombre: ").strip()

    # Validar que no haya otra categoría con el mismo nombre
    ya_existe = False
    tam_cat = os.path.getsize(ArcFisiCat)
    if tam_cat > 0:
        ArcLogCat.seek(0, 0)
        while ArcLogCat.tell() < tam_cat and not ya_existe:
            cat_aux = pickle.load(ArcLogCat)
            if cat_aux.nombre_categoria.strip().upper() == nom.upper():
                ya_existe = True

    if ya_existe:
        print("\nError: Ya existe una categoría registrada con el nombre '" + nom + "'.")
    else:
        preg = input("Ingrese la pregunta asociada a la categoría: ").strip()
        while preg == "":
            preg = input("La pregunta no puede estar vacía. Ingrese la pregunta: ").strip()

        # Generar número consecutivo secuencial al partir del último
        max_nro = 0
        if tam_cat > 0:
            ArcLogCat.seek(0, 0)
            while ArcLogCat.tell() < tam_cat:
                c = pickle.load(ArcLogCat)
                if c.nro_categoria > max_nro:
                    max_nro = c.nro_categoria

        nuevo_nro = max_nro + 1

        reg_nueva = Categoria()
        reg_nueva.nro_categoria = nuevo_nro
        reg_nueva.nombre_categoria = nom
        reg_nueva.pregunta = preg
        reg_nueva.estado = "A"
        formatear_categoria(reg_nueva)

        ArcLogCat.seek(0, 2)
        pickle.dump(reg_nueva, ArcLogCat)
        ArcLogCat.flush()

        print("\n¡Categoría creada con éxito!")
        print("Número asignado: " + str(nuevo_nro))
        print("Nombre: " + nom)
        print("Estado: Activa ('A')")

    input("\nPresione Enter para continuar...")


def modificacion_categoria():
    """
    Procedimiento para modificar el nombre de una categoría activa.
    """
    limpiar_pantalla()
    print("================================================================================")
    print("                 ADMINISTRAR CATEGORÍAS - MODIFICACIÓN                          ")
    print("================================================================================")

    tam_cat = os.path.getsize(ArcFisiCat)
    cant_activas = 0
    if tam_cat > 0:
        print("Categorías Activas disponibles:")
        ArcLogCat.seek(0, 0)
        while ArcLogCat.tell() < tam_cat:
            c = pickle.load(ArcLogCat)
            if c.estado.strip() == "A":
                print("  Nro: " + str(c.nro_categoria) + " - Nombre: " + c.nombre_categoria.strip())
                cant_activas = cant_activas + 1

    if cant_activas == 0:
        print("No existen categorías activas para modificar.")
    else:
        nro_ing = input("\nIngrese el número de categoría a modificar: ").strip()
        while not nro_ing.isdigit():
            nro_ing = input("Entrada inválida. Ingrese un número de categoría: ").strip()
        nro_sel = int(nro_ing)

        # Buscar la categoría y validar que su estado sea 'A'
        pos_encontrada = -1
        cat_a_modificar = None
        ArcLogCat.seek(0, 0)
        while ArcLogCat.tell() < tam_cat and pos_encontrada == -1:
            pos_act = ArcLogCat.tell()
            c = pickle.load(ArcLogCat)
            if c.nro_categoria == nro_sel and c.estado.strip() == "A":
                pos_encontrada = pos_act
                cat_a_modificar = c

        if pos_encontrada == -1:
            print("\nError: La categoría número " + str(nro_sel) + " no existe o no se encuentra Activa ('A').")
        else:
            print("Nombre actual: " + cat_a_modificar.nombre_categoria.strip())
            nuevo_nom = input("Ingrese el nuevo nombre para la categoría: ").strip()
            while nuevo_nom == "":
                nuevo_nom = input("El nombre no puede estar vacío. Ingrese el nuevo nombre: ").strip()

            cat_a_modificar.nombre_categoria = nuevo_nom
            formatear_categoria(cat_a_modificar)

            ArcLogCat.seek(pos_encontrada, 0)
            pickle.dump(cat_a_modificar, ArcLogCat)
            ArcLogCat.flush()
            print("\n¡Nombre de categoría modificado exitosamente!")

    input("\nPresione Enter para continuar...")


def baja_categoria():
    """
    Procedimiento para dar de baja lógica a una categoría (cambiar estado a 'I').
    """
    limpiar_pantalla()
    print("================================================================================")
    print("                     ADMINISTRAR CATEGORÍAS - BAJA                              ")
    print("================================================================================")

    tam_cat = os.path.getsize(ArcFisiCat)
    cant_activas = 0
    if tam_cat > 0:
        print("Categorías Activas disponibles:")
        ArcLogCat.seek(0, 0)
        while ArcLogCat.tell() < tam_cat:
            c = pickle.load(ArcLogCat)
            if c.estado.strip() == "A":
                print("  Nro: " + str(c.nro_categoria) + " - Nombre: " + c.nombre_categoria.strip())
                cant_activas = cant_activas + 1

    if cant_activas == 0:
        print("No existen categorías activas para dar de baja.")
    else:
        nro_ing = input("\nIngrese el número de categoría a dar de baja: ").strip()
        while not nro_ing.isdigit():
            nro_ing = input("Entrada inválida. Ingrese un número de categoría: ").strip()
        nro_sel = int(nro_ing)

        pos_encontrada = -1
        cat_a_baja = None
        ArcLogCat.seek(0, 0)
        while ArcLogCat.tell() < tam_cat and pos_encontrada == -1:
            pos_act = ArcLogCat.tell()
            c = pickle.load(ArcLogCat)
            if c.nro_categoria == nro_sel and c.estado.strip() == "A":
                pos_encontrada = pos_act
                cat_a_baja = c

        if pos_encontrada == -1:
            print("\nError: La categoría número " + str(nro_sel) + " no existe o no se encuentra Activa ('A').")
        else:
            cat_a_baja.estado = "I"
            formatear_categoria(cat_a_baja)

            ArcLogCat.seek(pos_encontrada, 0)
            pickle.dump(cat_a_baja, ArcLogCat)
            ArcLogCat.flush()
            print("\n¡La categoría '" + cat_a_baja.nombre_categoria.strip() + "' ha sido dada de baja (Estado 'I')!")

    input("\nPresione Enter para continuar...")


def administrar_categorias():
    """
    Submenú de gestión de categorías.
    """
    opc_cat = ""
    while opc_cat != "4":
        limpiar_pantalla()
        print("================================================================================")
        print("                       ADMINISTRAR CATEGORÍAS                                   ")
        print("================================================================================")
        print("  1- Alta")
        print("  2- Modificación")
        print("  3- Baja")
        print("  4- Volver: Vuelve al menú anterior")
        print("================================================================================")

        opc_cat = input("\nIngrese una opción (1-4): ").strip()
        while opc_cat != "1" and opc_cat != "2" and opc_cat != "3" and opc_cat != "4":
            opc_cat = input("Opción inválida. Ingrese 1, 2, 3 o 4: ").strip()

        if opc_cat == "1":
            alta_categoria()
        elif opc_cat == "2":
            modificacion_categoria()
        elif opc_cat == "3":
            baja_categoria()


def alta_opcion():
    """
    Procedimiento para dar de alta una nueva opción vinculada a una categoría activa.
    """
    limpiar_pantalla()
    print("================================================================================")
    print("                      ADMINISTRAR OPCIONES - ALTA                               ")
    print("================================================================================")

    tam_cat = os.path.getsize(ArcFisiCat)
    cant_activas = 0
    if tam_cat > 0:
        print("Categorías Activas disponibles:")
        ArcLogCat.seek(0, 0)
        while ArcLogCat.tell() < tam_cat:
            c = pickle.load(ArcLogCat)
            if c.estado.strip() == "A":
                print("  Nro: " + str(c.nro_categoria) + " - Nombre: " + c.nombre_categoria.strip())
                cant_activas = cant_activas + 1

    if cant_activas == 0:
        print("Antes de registrar opciones se deben dar de alta categorías.")
    else:
        nro_ing = input("\nIngrese el número de la categoría elegida: ").strip()
        while not nro_ing.isdigit():
            nro_ing = input("Entrada inválida. Ingrese el número de categoría: ").strip()
        nro_sel = int(nro_ing)

        # Validar existencia de la categoría activa
        valida = False
        cat_sel = None
        ArcLogCat.seek(0, 0)
        while ArcLogCat.tell() < tam_cat and not valida:
            c = pickle.load(ArcLogCat)
            if c.nro_categoria == nro_sel and c.estado.strip() == "A":
                valida = True
                cat_sel = c

        if not valida:
            print("\nError: La categoría ingresada no existe o no se encuentra Activa.")
        else:
            print("Categoría seleccionada: " + cat_sel.nombre_categoria.strip())
            print("Pregunta: " + cat_sel.pregunta.strip())

            obj = input("\nIngrese el Objeto / Elemento: ").strip()
            while obj == "":
                obj = input("El objeto no puede estar vacío. Ingrese el objeto: ").strip()

            val_ing = input("Ingrese el Valor numérico de respuesta: ").strip()
            while not val_ing.isdigit():
                val_ing = input("Valor inválido. Ingrese un número entero: ").strip()
            val_num = int(val_ing)

            # Calcular el NroOpción correspondiente para esta categoría
            cant_opcs = contar_opciones_categoria(nro_sel)
            nro_nueva_opc = cant_opcs + 1

            reg_opc = Opcion()
            reg_opc.nro_categoria = nro_sel
            reg_opc.nro_opcion = nro_nueva_opc
            reg_opc.objeto = obj
            reg_opc.valor = val_num
            formatear_opcion(reg_opc)

            ArcLogOpc.seek(0, 2)
            pickle.dump(reg_opc, ArcLogOpc)
            ArcLogOpc.flush()

            print("\n¡Opción guardada exitosamente!")
            print("Categoría: " + str(nro_sel) + " | Opción Nro: " + str(nro_nueva_opc) +
                  " | Objeto: " + obj + " | Valor: " + str(val_num))

    input("\nPresione Enter para continuar...")


def consulta_opciones():
    """
    Procedimiento para consultar la pregunta y todas las opciones de una categoría.
    """
    limpiar_pantalla()
    print("================================================================================")
    print("                    ADMINISTRAR OPCIONES - CONSULTA                             ")
    print("================================================================================")

    tam_cat = os.path.getsize(ArcFisiCat)
    if tam_cat == 0:
        print("No hay categorías registradas en el sistema.")
    else:
        print("Listado general de categorías:")
        ArcLogCat.seek(0, 0)
        while ArcLogCat.tell() < tam_cat:
            c = pickle.load(ArcLogCat)
            est = "Activa"
            if c.estado.strip() == "I":
                est = "Inactiva"
            print("  Nro: " + str(c.nro_categoria) + " - " + c.nombre_categoria.strip() + " (" + est + ")")

        nro_ing = input("\nIngrese el número de categoría a consultar: ").strip()
        while not nro_ing.isdigit():
            nro_ing = input("Entrada inválida. Ingrese un número: ").strip()
        nro_sel = int(nro_ing)

        # Buscar categoría
        encontrada = False
        cat_info = None
        ArcLogCat.seek(0, 0)
        while ArcLogCat.tell() < tam_cat and not encontrada:
            c = pickle.load(ArcLogCat)
            if c.nro_categoria == nro_sel:
                encontrada = True
                cat_info = c

        if not encontrada:
            print("\nError: La categoría ingresada no existe.")
        else:
            print("\n----------------------------------------------------------------")
            print("Categoría: " + cat_info.nombre_categoria.strip())
            print("Pregunta : " + cat_info.pregunta.strip())
            print("----------------------------------------------------------------")
            print("Opciones y respuestas numéricas:")

            tam_opc = os.path.getsize(ArcFisiOpc)
            hay_opcs = False
            if tam_opc > 0:
                ArcLogOpc.seek(0, 0)
                while ArcLogOpc.tell() < tam_opc:
                    op = pickle.load(ArcLogOpc)
                    if op.nro_categoria == nro_sel:
                        print("  Opción " + str(op.nro_opcion) + ": " +
                              op.objeto.strip().ljust(40, " ") + " | Valor: " + str(op.valor))
                        hay_opcs = True

            if not hay_opcs:
                print("  No hay opciones registradas para esta categoría.")

    input("\nPresione Enter para continuar...")


def administrar_opciones():
    """
    Submenú de gestión de opciones.
    """
    opc_op = ""
    while opc_op != "3":
        limpiar_pantalla()
        print("================================================================================")
        print("                        ADMINISTRAR OPCIONES                                    ")
        print("================================================================================")
        print("  1- Alta")
        print("  2- Consulta")
        print("  3- Volver")
        print("================================================================================")

        opc_op = input("\nIngrese una opción (1-3): ").strip()
        while opc_op != "1" and opc_op != "2" and opc_op != "3":
            opc_op = input("Opción inválida. Ingrese 1, 2 o 3: ").strip()

        if opc_op == "1":
            alta_opcion()
        elif opc_op == "2":
            consulta_opciones()


def administracion_juegos():
    """
    Procedimiento para la opción F del menú principal.
    Requiere autenticación con contraseña oculta (máximo 3 intentos).
    """
    limpiar_pantalla()
    print("================================================================================")
    print("                     ACCESO A ADMINISTRACIÓN DE JUEGOS                          ")
    print("================================================================================")

    intentos = 3
    clave_correcta = False

    while intentos > 0 and not clave_correcta:
        clave = getpass.getpass("Ingrese la contraseña de administrador: ")
        if clave == CLAVE_ADMIN:
            clave_correcta = True
        else:
            intentos = intentos - 1
            if intentos > 0:
                print("Contraseña incorrecta. Le quedan " + str(intentos) + " intento(s).\n")
            else:
                print("\nSuperó los 3 intentos de ingresar contraseña, salga e intente nuevamente")
                input("Presione Enter para regresar al menú principal...")

    if clave_correcta:
        opc_adm = ""
        while opc_adm != "3":
            limpiar_pantalla()
            print("================================================================================")
            print("                       ADMINISTRACIÓN DE JUEGOS                                 ")
            print("================================================================================")
            print("  1. Administrar Categorías")
            print("  2. Administrar Opciones")
            print("  3. Volver: Vuelve al menú anterior")
            print("================================================================================")

            opc_adm = input("\nIngrese una opción (1-3): ").strip()
            while opc_adm != "1" and opc_adm != "2" and opc_adm != "3":
                opc_adm = input("Opción inválida. Ingrese 1, 2 o 3: ").strip()

            if opc_adm == "1":
                administrar_categorias()
            elif opc_adm == "2":
                administrar_opciones()


# ==============================================================================
# OPCIÓN G: SALIR DEL PROGRAMA
# ==============================================================================
def salir_del_programa():
    """
    Procedimiento para la opción G. Muestra el mensaje reglamentario antes de cerrar.
    """
    limpiar_pantalla()
    print("================================================================================")
    print("           Gracias por jugar, no apueste, juega por diversión                   ")
    print("================================================================================")
    input("\nPresione Enter para finalizar...")


# ==============================================================================
# PROGRAMA PRINCIPAL
# ==============================================================================
abrir_archivos()
inicializar_datos_si_vacio()
mostrar_advertencia()

opc_menu = ""
while opc_menu != "G":
    MENU()
    opc_menu = input("\nIngrese su opción (a-g): ").strip().upper()
    while opc_menu != "A" and opc_menu != "B" and opc_menu != "C" and \
          opc_menu != "D" and opc_menu != "E" and opc_menu != "F" and opc_menu != "G":
        opc_menu = input("Opción inválida. Ingrese una opción entre a y g: ").strip().upper()

    if opc_menu == "A":
        jugar_menor_mayor()
        limpiar_pantalla()
    elif opc_menu == "B":
        jugar_numero_secreto()
        limpiar_pantalla()
    elif opc_menu == "C":
        jugar_blackjack()
        limpiar_pantalla()
    elif opc_menu == "D":
        jugar_par_impar()
        limpiar_pantalla()
    elif opc_menu == "E":
        reporte()
        limpiar_pantalla()
    elif opc_menu == "F":
        administracion_juegos()
        limpiar_pantalla()
    elif opc_menu == "G":
        salir_del_programa()

cerrar_archivos()
