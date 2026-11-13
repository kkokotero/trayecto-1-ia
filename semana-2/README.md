# Semana 2 · Dos actividades

En la semana 2 se realizaron dos actividades:

1. **De dos a tres números** — se implementó un algoritmo que ordena tres números enteros con solo `if` y comparaciones, y se comparó con las soluciones de dos modelos de IA que recibieron la misma instrucción.
2. **Tres cupos, ocho estudiantes** — se usó una IA para proponer quiénes deberían recibir los cupos de un programa de acompañamiento, se revisó su respuesta y se contrastó con una segunda consulta.

## Archivos

- [`ordenar_tres_numeros.py`](./ordenar_tres_numeros.py) — solución propia de la actividad de algoritmos.
- [`riwi-tres-cupos.md`](./riwi-tres-cupos.md) — bitácora completa de la actividad de clase: el caso, la elección individual, las dos consultas a la IA con sus respuestas, las observaciones del equipo y la conclusión.

---

# Actividad 1 · De dos a tres números

## Qué hicimos

Escribimos un programa en Python que pide tres números enteros y los muestra de menor a mayor, usando solo `input`, `if` y comparaciones: sin listas, sin ciclos y sin `sorted()`.

La instrucción se copió igual en dos asistentes de IA para comparar las tres soluciones con los mismos casos de prueba.

## La solución

[`ordenar_tres_numeros.py`](./ordenar_tres_numeros.py) aplica tres comparaciones con intercambio, la misma estructura del algoritmo de la semana 1:

1. Si `a > b`, se intercambian.
2. Si `b > c`, se intercambian.
3. Si `a > b`, se intercambian.

La tercera comparación es necesaria porque el segundo intercambio puede volver a desordenar `a` y `b`. Al terminar, `a <= b <= c`.

```python
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))

if a > b:
    aux = a
    a = b
    b = aux

if b > c:
    aux = b
    b = c
    c = aux

if a > b:
    aux = a
    a = b
    b = aux

print("Numeros ordenados de menor a mayor:")
print(a)
print(b)
print(c)
```

## Registro de pruebas

Las tres soluciones se evalúan con los mismos casos:

| Caso | Entrada | Salida esperada | Algoritmo propio | Modelo 1 | Modelo 2 |
| --- | --- | --- | --- | --- | --- |
| 1 | `7, 2, 5` | `2, 5, 7` | Correcto | | |
| 2 | `2, 2, 9` | `2, 2, 9` | Correcto | | |
| 3 | `-3, 7, 0` | `-3, 0, 7` | Correcto | | |
| 4 | `10, -5, 4` | `-5, 4, 10` | Correcto | | |

El caso 1 parte de una entrada sin ordenar. El caso 2 tiene valores repetidos. Los casos 3 y 4 incluyen números negativos. La solución propia pasó los cuatro casos; las respuestas de los modelos no se versionaron en el repositorio.

## Conclusión

El algoritmo propio pasó los cuatro casos del registro y cumple las restricciones de la consigna: solo `input`, `if` y comparaciones, sin listas, sin ciclos y sin `sorted()`. Es el mismo algoritmo de la semana 1, con la sintaxis de Python.

---

# Actividad 2 · Tres cupos, ocho estudiantes

En un curso de programación hay ocho estudiantes y solo tres cupos disponibles para un programa de acompañamiento. El equipo usó una IA para proponer quiénes deberían recibirlos, revisó lo que respondió y lo contrastó con una segunda consulta que ya incluía la información del programa.

La bitácora completa, con el caso, las dos consultas y respuestas, las observaciones y la conclusión, está en [`riwi-tres-cupos.md`](./riwi-tres-cupos.md).
