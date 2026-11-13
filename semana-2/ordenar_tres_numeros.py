"""Ordena tres números enteros de menor a mayor.

Restricciones de la actividad: solo input, if, else y comparaciones.
Sin listas, sin ciclos y sin sorted().

El algoritmo son tres comparaciones con intercambio: al terminar,
A <= B <= C. Funciona con valores repetidos y con números negativos.
"""

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))

# Primera comparación: deja A <= B.
if a > b:
    aux = a
    a = b
    b = aux

# Segunda comparación: deja B <= C.
if b > c:
    aux = b
    b = c
    c = aux

# Tercera comparación: el segundo intercambio pudo volver a desordenar A y B.
if a > b:
    aux = a
    a = b
    b = aux

print("Numeros ordenados de menor a mayor:")
print(a)
print(b)
print(c)
