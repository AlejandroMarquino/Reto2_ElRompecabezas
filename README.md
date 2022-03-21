# Reto2_ElRompecabezas
Reto 2 para prueba de alto nivel Python - El rompecabezas ( slider puzzle )

Descripción del reto
Un rompecabezas deslizante es un rompecabezas combinado que desafía al jugador a
deslizar piezas (con frecuencia planas) a lo largo de ciertas rutas (generalmente en un
tablero) para establecer una configuración final determinada.
Su objetivo para este reto es escribir una función que produzca una secuencia de
movimientos de fichas que resuelva el rompecabezas.


Input del algoritmo
Una matriz/lista n x n compuesta por valores enteros que van de 0 a n^2 - 1 (inclusive), que
representa una cuadrícula cuadrada.
Ten en cuenta que siempre habrá una ficha vacía (representada por 0) para permitir el
movimiento de fichas adyacentes.
Output del algoritmo
Una matriz/lista compuesta por cualquiera (pero no necesariamente todos) de los números
enteros de 1 a n^2 - 1, inclusive.
Esto representa la secuencia de movimientos de fichas para una transición exitosa del
estado inicial sin resolver al estado resuelto. Si el rompecabezas no se puede resolver,
devolverá None (Python).

Detalles importantes para la prueba
● El input debe ser válido.
● El rango de valores para n es: 10 >= n >= 3
