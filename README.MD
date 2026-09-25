# Algoritmos y Estructuras de Datos - TP3 2026 (UTN FRRO)

**Comisión:** 103  
**Integrantes:**
- Alexis Byrne
- Tomás García
- Dante Lamboglia
- Luca Colombo

---

## Suite de Juegos "Azar y Lógica"

El presente proyecto corresponde al **Trabajo Práctico Nro. 3** de la cátedra **Algoritmos y Estructuras de Datos**, implementado íntegramente en lenguaje Python, respetando las pautas metodológicas de programación estructurada modular descendente (Top-Down) y la teoría de registros y archivos dictada en clases.

---

## Modelo de Datos y Archivos Físicos

El sistema trabaja con persistencia permanente de información mediante archivos binarios de acceso directo gestionados con la biblioteca `pickle`:

1. **`Categorias.dat`**
   - `NroCategoria`: `int` (consecutivo secuencial desde 1)
   - `NombreCategoria`: `str(30)`
   - `Pregunta`: `str(200)`
   - `Estado`: `str(1)` ('A' Activa / 'I' Inactiva)
2. **`Opciones.dat`**
   - `NroCategoria`: `int` (clave foránea que relaciona con Categorias)
   - `NroOpción`: `int` (secuencial dentro de la categoría)
   - `objeto`: `str(100)`
   - `valor`: `int` (valor numérico de comparación)
3. **`Jugadores.dat`** (sin ningún orden)
   - `Nombre`: `str(30)`
   - `Creditos`: `float` (crédito inicial de $10.000,00 al registrarse)
   - `Juegos`: matriz de 2 x 4 de enteros
     - Fila 0: partidas ganadas
     - Fila 1: partidas perdidas
     - Columnas: 0 = Menor/Mayor, 1 = Número Secreto, 2 = Blackjack, 3 = Par/Impar

> **Ubicación de archivos:** Por requerimiento de cátedra, los archivos de datos se almacenan en `c:\tp3\`. Si la carpeta no existiera, el sistema la crea automáticamente al iniciar. Asimismo, se proveen los archivos con 3 categorías activas y 10 opciones precargadas por categoría.

---

## Menú de Opciones y Juegos

- **a. Juego del menor-mayor:** El jugador apuesta créditos y selecciona una categoría temática. Disputa 6 rondas dinámicas donde debe indicar qué opción responde a la pregunta de la categoría. Si acierta 4 o más, duplica su apuesta; en caso contrario, la pierde.
- **b. Adivinar el número secreto:** 5 intentos para acertar un número aleatorio del 1 al 100 con pistas de mayor/menor e indicación de intentos restantes.
- **c. Blackjack (El 21):** Juego clásico contra la banca con baraja de 52 cartas sin repetición, utilizando arreglos de tamaño fijo y reglas formales de croupier (la banca pide con 16 o menos y se planta con 17 o más).
- **d. Par o impar:** Apuesta de créditos sobre la suma de dos dados (1 al 6). El usuario intenta acertar si la suma es par o impar.
- **e. Reporte:** 
  - Listado de jugadores ordenados de mayor a menor por crédito usando el algoritmo **Falso Burbuja**.
  - Consulta detallada de historial de partidas y créditos de un jugador puntual.
- **f. Administración de Juegos:** Acceso protegido por contraseña oculta (máximo 3 intentos). Permite alta, modificación y baja lógica de categorías, así como alta y consulta de opciones.
- **g. Salir del programa:** Muestra el cartel reglamentario y cierra los archivos de forma limpia.

---

## Pautas Metodológicas y Restricciones Cumplidas

- **Programación estilo principiante:** Código modular, estructurado, limpio y fácil de leer.
- **Control de flujo estructurado:** 
  - Cero sentencias `break`.
  - Cero sentencias `exit()`.
  - Cero sentencias `while True`.
  - Funciones con un único punto de retorno (`return`) al final de la misma.
  - Procedimientos implementados sin sentencia `return`.
- **Estructuras de datos:** 
  - Prohibido el uso de listas dinámicas (`.append()`, `.pop()`, `.extend()`, etc.).
  - Uso exclusivo de arreglos estáticos de tamaño fijo (`[0] * N`, `[None] * N`, matrices `[[0] * 4 for i in range(2)]`).
- **Algoritmos teóricos:** Búsqueda secuencial en archivos directos con puntero en bytes (`seek`, `tell`), Falso Burbuja para ordenamiento, formateo de campos con `.ljust()`.





