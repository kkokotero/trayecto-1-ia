
Algoritmo OrdenarTresNumeros

    Definir A, B, C, AUX Como Entero

    Escribir "Ingrese el primer numero:"
    Leer A

    Escribir "Ingrese el segundo numero:"
    Leer B

    Escribir "Ingrese el tercer numero:"
    Leer C

    Si A > B Entonces
        AUX <- A
        A <- B
        B <- AUX
    FinSi

    Si B > C Entonces
        AUX <- B
        B <- C
        C <- AUX
    FinSi

    Si A > B Entonces
        AUX <- A
        A <- B
        B <- AUX
    FinSi

    Escribir "Numeros ordenados de menor a mayor:"
    Escribir A
    Escribir B
    Escribir C

FinAlgoritmo
