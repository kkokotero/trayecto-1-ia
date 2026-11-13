# Semana 1 · Una idea que cambió

## Programa a una persona

Una persona hace de «computador» y solo ejecuta literalmente lo que le dicen; otra escribe las instrucciones.

**Objetivo:** ordenar tres tarjetas con números de menor a mayor con pasos que sirvan aunque los números cambien.

**Restricciones:**
- Solo se puede comparar dos tarjetas e intercambiarlas.
- No vale decir «ordénalas».

**Pruebas:**
- Con `7, 2, 5`
- Con `2, 2, 9`

Además, hay que **mejorar una instrucción ambigua**, señalando dónde hay una decisión «si ocurre esto, haz aquello».

---

## Entrena a un clasificador humano

Cada equipo recibe **seis mensajes de entrenamiento** con su etiqueta y escribe las pistas que sirven para reconocer un mensaje no deseado.

### Mensajes de entrenamiento

| Etiqueta | Mensaje |
| --- | --- |
| No deseado | «Ganaste un premio. Haz clic para reclamarlo». |
| No deseado | «Oferta exclusiva: paga hoy y recibe el doble». |
| No deseado | «Tu cuenta será bloqueada. Entra a este enlace y confirma tu clave». |
| Deseado | «La clase de mañana comienza a las 10:00». |
| Deseado | «La entrega del proyecto será el viernes». |
| Deseado | «Adjunto el acta de la reunión del equipo». |

### Prueba

Después llegan **dos mensajes de prueba sin etiqueta**: hay que **predicir** y **justificar** cada uno.

---

## Diseña el primer asistente

1. Elijan **una sola necesidad de estudio**.
2. Dibujen una **pantalla sencilla**.
3. Tracen el **recorrido de una consulta** (4 a 6 pasos).
4. Marquen cada paso con:
   - **R** — lo que se resuelve con reglas.
   - **M** — donde ayudaría un modelo.
   - **H** — donde una persona revisa.
5. Añadan un **mensaje visible de límite**.

---

## Prueba cruzada

- **Intercambien los bocetos** con otro equipo.
- Prueben el asistente recibido con:
  - Una **pregunta fuera de tema**.
  - Una pregunta que **el material no permite responder con seguridad**.
- Entreguen una **sugerencia concreta**, que puede ser:
  - Una regla que falta.
  - Una respuesta que requiere revisión humana.
  - Una frase de límite más clara.

---

## Cierre y evidencia

Cada equipo entrega:

- Su **boceto**.
- El **flujo marcado con R, M y H**.
- La frase: *«Nuestro asistente ayuda a ___, pero todavía no debe ___»*.

---

## Archivos de esta semana

- [`OrdenarTresNumeros.psc`](./OrdenarTresNumeros.psc) — algoritmo en PSeInt que ordena tres números usando solo comparaciones e intercambios, sin listas ni funciones de ordenamiento.
- [`OrdenarTresNumeros.svg`](./OrdenarTresNumeros.svg) — diagrama de actividad del algoritmo.
