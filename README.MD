Algoritmos y Estructura de Datos TP1 2026
Contenido
INSTRUCCIONES DEL PROGRAMA .................................................................... 2
1. Inicio..................................................................................................... 2
2. Programación de los juegos.................................................................... 2
A. Juego del menor-mayor:...................................................................... 2
B. Número secreto: ................................................................................ 2
C. Blackjack:.......................................................................................... 3
D. Par o impar: ....................................................................................... 3
E. Reporte: ............................................................................................ 3
3. Determinación de la nota ....................................................................... 3
4. ANEXO.................................................................................................. 4
Algoritmos y Estructura de Datos TP1 2026
INSTRUCCIONES DEL PROGRAMA
Desarrollo de Suite de Juegos "Azar y Lógica" en Python
1. Inicio.
Cuando el programa inicie debe mostrar un cartel, grande, dibujado con caracteres,
donde se indique que los juegos de apuesta están prohibidos para los menores y es
perjudicial para la salud.
Luego de que el usuario o jugadore hace clic en la tecla “Enter”, dicho cartel debe
borrarse y en su lugar aparecer un menú de opciones iterativo como el siguiente:
A. Juego del menor-mayor
B. Adivinar el número secreto
C. Blackjack
D. Par o impar
E. Reporte
F. Salir del programa
La programación de este menú será dada por la cátedra.
2. Programación de los juegos
Se deberá realizar al menos un procedimiento por cada juego.
A. Juego del menor-mayor:
En este caso, cuando inicie el juego el programa pedirá el nombre del jugador.
Luego, deberá mostrar de manera aleatoria un número entre el 1 y el 1000. A
partir de ahí, el programa pedirá al usuario que ingrese la palabra “Mayor” si
creé que el siguiente número es mayor o “Menor” si cree que el siguiente
número es menor al número que se muestra en pantalla. No deberá importar si
el usuario escribe en mayúsculas o minúsculas, el programa debe reconocerlo.
Si usuario acierta, es decir, que el siguiente número es mayor y eligió mayor o si
eligió menor y es menor, el programa debe sumar a la racha de aciertos un
punto.
Si el jugador elige mayor y el número es menor o el jugador elige menor y el
número es mayor, el programa deberá indicar con un mensaje que el juego está
terminado y mostrar el nombre del jugador y la racha de acierto, es decir, que
cantidad de veces acertó.
Aplicar para la generación de números aleatorios la función de Python
“random”. Investigar como funciona.
B. Número secreto:
Al iniciar, le programa, debe solicitar el nombre del jugador.
Algoritmos y Estructura de Datos TP1 2026
El programa debe generar un número aleatorio y no mostrarlo.
El jugador tendrá 6 intentos de adivinar el número. Cada vez que el jugador
indique un número, si no adivina el programa deberá indicar si el número que
pensó la máquina es mayor o menor. El jugador, deberá a ingresar otro número
para intentar adivinar.
Previo a que el jugador, ingrese un número la máquina deberá mostrar cuantos
intentos le queda por adivinar.
Al final, si adivina mostrar la cantidad de intentos que le llevó adivinar y, en caso
de no adivinar mostrar un mensaje indicando que el jugador perdió y el número
que pensó la máquina.
Se deberá llevar registro de la cantidad de veces que el usuario jugó, la cantidad
que acertó y la cantidad de veces que perdió el juego.
Aquí también usar la función de Python “random”.
C. Blackjack:
Si el jugador elige esta opción, mostrar un cartel que indique “Juego en
construcción” y que al presionar “Enter” retorne al menú principal.
D. Par o impar:
También en este caso el programa debe solicitar al jugador, su nombre.
En esta primera etapa el programa deberá generar 2 números aleatorios del 1 al
6 y sumarlos.
Sin mostrarlos el usuario debe indicar, a solicitud del programa, si la suma de
los números es par o impar. Si acierta, mostrar que ganó y si pierde mostrar que
perdió.
Se debe llevar la cuenta de la cantidad de veces que acertó.
E. Reporte:
Si se elige esta opción el programa deberá mostrar, para cada juego, aunque
se salga de cada juego y se vuelva a jugar:
- Nombre de jugador
- Cantidad de veces que jugó a cada juego.
- En el caso de menor-mayor, mayor racha alcanzada
- En el resto de los juegos, Cantidad de veces que perdió y que ganó.
A. Salir del programa: Mostrar un cartel que diga: “Gracias por jugar, no apueste,
juega por diversión” y luego de presionar “enter”, el programa se cierra.
3. Determinación de la nota
Algoritmos y Estructura de Datos TP1 2026
- Si no se entrega no hay nota. Recordar que todos los integrantes del
grupo deben entregarlo.
- En este primer trabajo, debido a varias factores, los grupos que
defiendan se determinarán por sorteo durante la clase de la defensa.
Se tomarán defensas durante las dos clases de la sola semana
posterior al domingo de la entrega. Para aspirar a la aprobación del
trabajo práctico, todos los alumnos deben estar presente les toque
defender o no, por lo que se tomará asistencia, sea o no elegido para
defender. Se tomará asistencia tanto en la primera como en la
segunda clase de defensa y, aunque un alumno ya haya defendido en
la primera de las dos clases de defensa, igualmente deberá asistir a
la segunda clase sin excusas. Aquel alumno que no esté presente
obtendrá una nota de “2” si el trabajo está realizado correctamente y
“1” si el trabajo no funciona.
- Cada integrante del equipo que le toque defender podrá obtener una
nota entre 2 y 10 dependiendo de cómo funcione el programa y de
cómo sea su defensa individual. La nota es individual, es decir, que
no necesariamente la nota de todos los integrantes del grupo será la
misma.
- Aquellos alumnos a los que no les toque defender, hayan hecho el
trabajo y estén presentes podrán tener una nota entre 2 y 10
dependiendo de los criterios de evaluación indicado en el documento
de premisas generales.
4. ANEXO
Esqueleto del programa
“””
Nombre de los integrantes del grupo.
Declaración de variables con su tipo.
“””
def juego1():
def juego2():
def juego3():
Algoritmos y Estructura de Datos TP1 2026
def juego4():
def reporte():
Luego sigue como se indica en el documento de preguntas frecuentes.