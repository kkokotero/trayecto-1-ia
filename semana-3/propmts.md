# CodeFlow Studio · Bitácora de prompts

Registro de los prompts que se usaron para construir **CodeFlow Studio** con ayuda de IA, en el orden en que se aplicaron. Cada prompt parte del estado anterior del proyecto y agrega o corrige algo concreto.

El texto de cada prompt se reproduce tal cual se envió al modelo; solo se reorganizó la estructura para poder leerlo y compararlo con ease.

## Índice

| # | Prompt | Qué trabaja |
| --- | --- | --- |
| 1 | [Prompt maestro](#1-prompt-maestro) | Define el producto completo de una sola vez: interfaz, lenguajes, visualización, runtime, editor visual, arquitectura y entrega. |
| 2 | [Especificación detallada](#2-especificación-detallada) | 15 secciones que profundizan identidad visual, sistema de diagramas, motor de ejecución, proyectos, estilos de diagrama y UX. |
| 3 | [Corrección del generador de Flowcharts](#3-corrección-del-generador-de-flowcharts) | Lógica real de flowchart, simbología estándar y diagramas más compactos. |
| 4 | [Aplicación de las correcciones](#4-aplicación-de-las-correcciones) | Corrige diagramas, analizadores de JavaScript y Python, parser de expresiones y aislamiento de los runtimes. |
| 5 | [Layout vertical y ejecución de código](#5-layout-vertical-y-ejecución-de-código) | Orientación Top to Bottom, distribución visual y ejecución real de JavaScript y Python desde la interfaz. |
| 6 | [Sistema de logros y progresión](#6-sistema-de-logros-y-progresión) | Niveles de dificultad, logros que se desbloquean al usar la plataforma, panel de progreso y persistencia. |

---

## 1. Prompt maestro

**Objetivo:** plantear el producto completo en un solo mensaje, con la estructura y las restricciones de alto nivel.

Desarrolla una aplicación web avanzada llamada CodeFlow Studio, una plataforma interactiva para escribir, ejecutar, visualizar y modificar código mediante diagramas dinámicos en tiempo real.

OBJETIVO: Crear un entorno de programación visual que permita introducir código en múltiples lenguajes, analizar su estructura, generar diagramas interactivos y ejecutar el código paso a paso mostrando el estado interno del programa.

INTERFAZ: Diseña una interfaz profesional tipo IDE, moderna y oscura, con panel de archivos, editor de código con resaltado de sintaxis, canvas central de diagramas, inspector de variables, consola y barra de control de ejecución.

LENGUAJES: JavaScript, TypeScript, Python, Lua, Java, C, C++, C#, Go, Rust y otros mediante adaptadores extensibles. Detecta el lenguaje automáticamente o permite seleccionarlo.

VISUALIZACIÓN: Convierte el código en nodos y conexiones que representen funciones, variables, condiciones, bucles, llamadas, eventos, clases, objetos y dependencias. Muestra el flujo de ejecución mediante animaciones y resalta el nodo activo.

RUNTIME: Implementa ejecución, pausa, reanudación, detención, reinicio, ejecución paso a paso, velocidad ajustable, breakpoints y seguimiento del estado de ejecución. Permite inspeccionar variables locales y globales, pila de llamadas, memoria lógica, argumentos, valores de retorno y cambios de estado en tiempo real.

EDITOR VISUAL: Permite arrastrar nodos, crear conexiones, modificar condiciones, valores, operaciones y estructuras. Los cambios en los diagramas deben actualizar el código fuente y los cambios en el código deben actualizar los diagramas. Implementa sincronización bidireccional y resolución de conflictos.

FUNCIONES ADICIONALES: Historial de ejecución, snapshots, comparación de estados, búsqueda de variables, seguimiento de dependencias, zoom, navegación por diagramas, exportación de diagramas, importación de archivos, proyectos con múltiples archivos y ejemplos interactivos.

ARQUITECTURA: Utiliza React, TypeScript, Monaco Editor, React Flow o una alternativa equivalente para diagramas, AST parsers y adaptadores de instrumentación por lenguaje. Para ejecutar código utiliza runtimes aislados, Web Workers, WebAssembly o contenedores sandbox en backend según el lenguaje. No ejecutes código arbitrario en el contexto principal del navegador. Implementa límites de CPU, memoria y tiempo, aislamiento y controles de seguridad.

IMPORTANTE: No simules la ejecución mostrando animaciones falsas. Los valores, las variables, los pasos y los diagramas deben derivarse del estado real del programa instrumentado. Si un lenguaje no tiene soporte completo de ejecución, indica claramente sus capacidades y limitaciones.

DISEÑO: Interfaz oscura profesional, estilo IDE futurista, tipografía monoespaciada, paneles redimensionables, nodos diferenciados por colores, animaciones fluidas y diseño responsive.

ENTREGA: Construye una aplicación funcional, no solamente una maqueta visual. Implementa primero JavaScript y Python de manera funcional, con arquitectura extensible para los demás lenguajes. Incluye proyectos de demostración, manejo de errores, documentación y pruebas. Prioriza la precisión del seguimiento de ejecución y la sincronización bidireccional entre código y diagramas.

---

## 2. Especificación detallada

**Objetivo:** ampliar el prompt maestro a una especificación completa por secciones, que sirva como referencia de construcción y de auditoría de lo implementado.

### CODEFLOW STUDIO — ADVANCED VISUAL PROGRAMMING ENVIRONMENT

Actúa como un equipo senior de ingeniería de software, arquitectura de sistemas, diseño UX/UI y desarrollo de herramientas de programación. Diseña y construye una aplicación web profesional llamada CodeFlow Studio.

El objetivo es desarrollar un entorno de programación visual donde los usuarios puedan escribir código, ejecutarlo, observar cada operación interna, visualizar algoritmos mediante diagramas de flujo detallados, modificar los diagramas y sincronizar los cambios con el código fuente.

No construyas una simple maqueta. Desarrolla una aplicación funcional, modular, escalable y con una experiencia de usuario de nivel profesional.

### 1. IDENTIDAD VISUAL: MATERIAL 3 EXPRESSIVE

Toda la aplicación debe seguir Material 3 Expressive de Google.

Utiliza:
- Material 3 Expressive como sistema de diseño.
- Material Color Utilities para generar paletas dinámicas.
- Material Symbols para iconografía.
- Tipografía y jerarquías visuales coherentes con Material Design.
- Formas expresivas, contenedores, superficies tonales y componentes adaptativos.
- Animaciones con movimiento expresivo, transiciones suaves y estados visuales claros.

#### Paleta dinámica

Implementa un sistema de colores basado en Material Color Utilities:
- Permitir seleccionar un color semilla.
- Generar automáticamente esquemas tonales.
- Soportar light mode y dark mode.
- Implementar esquemas Dynamic Color.
- Utilizar roles de color semánticos: primary, secondary, tertiary, surface, surfaceContainer, outline, error, etc.
- Adaptar los colores de nodos, conexiones, indicadores y paneles según el tema.
- Mantener contraste y accesibilidad WCAG.

Los diagramas deben tener un sistema cromático semántico independiente, pero derivado de la paleta dinámica.

### 2. SISTEMA AVANZADO DE DIAGRAMAS

Este es el núcleo principal del producto.

No conviertas una operación completa en un único bloque genérico. Descompón cada instrucción en sus operaciones internas y representa cada una de manera visual.

Ejemplo:

Código:
total = (a + b) * c - d

Debe representarse como un árbol de operaciones:

1. Obtener a.
2. Obtener b.
3. Ejecutar suma a + b.
4. Obtener c.
5. Multiplicar el resultado por c.
6. Obtener d.
7. Ejecutar resta.
8. Asignar el resultado a total.

Cada operación debe tener su propio nodo, conexiones de entrada y salida, valor calculado y estado de ejecución.

Implementa:
- Árboles de expresiones.
- Grafos de flujo de control (CFG).
- Grafos de dependencias de datos.
- Diagramas de flujo tradicionales.
- Descomposición de operaciones aritméticas.
- Diagramas de llamadas entre funciones.
- Representación de objetos y estructuras.
- Relaciones entre variables.
- Subgrafos expandibles y contraíbles.

Permite cambiar entre diferentes niveles de detalle:
- Nivel 1: vista general del programa.
- Nivel 2: funciones y estructuras.
- Nivel 3: instrucciones individuales.
- Nivel 4: operaciones internas y expresiones.
- Nivel 5: evaluación paso a paso de cada operación.

Implementa navegación jerárquica para entrar y salir de secciones del diagrama.

### 3. VISUALIZACIÓN ESPECIALIZADA DE LOOPS

Los loops deben tener una representación visual completamente diferenciada.

No deben mostrarse como simples bloques de texto.

Implementa representaciones específicas para:
- for
- while
- do while
- forEach
- iteradores
- loops anidados

Cada bucle debe visualizar:
- Inicialización.
- Condición de continuación.
- Evaluación de la condición.
- Ejecución del cuerpo.
- Incremento o decremento.
- Regreso al punto de evaluación.
- Salida del bucle.
- Número de iteración actual.
- Número total de iteraciones, cuando sea conocido.

#### Animación de recorrido

Cuando se ejecute un loop, debe verse físicamente cómo el flujo recorre el diagrama.

El flujo debe:
1. Entrar al nodo del bucle.
2. Ejecutar la inicialización.
3. Llegar a la condición.
4. Resaltar la condición y mostrar su resultado.
5. Si es true, animar el recorrido hacia el cuerpo.
6. Mostrar cada operación interna.
7. Ejecutar el incremento.
8. Animar el retorno a la condición.
9. Repetir el proceso.
10. Si es false, animar la salida del bucle.

Diferencia visualmente:
- Camino de entrada.
- Camino de repetición.
- Camino de salida.
- Camino de break.
- Camino de continue.
- Camino de excepciones.

Cada iteración debe mostrar un identificador y un estado independiente.

Para bucles anidados, utiliza contenedores visuales anidados, cada uno con su propio contador, estado y recorrido.

Implementa una opción para visualizar simultáneamente todas las iteraciones o solamente la iteración actual.

### 4. CONDICIONALES E IF AVANZADOS

Diferencia visualmente todas las estructuras condicionales:

- if
- else
- else if
- switch
- match
- operadores ternarios
- condiciones compuestas

Las condiciones deben descomponerse en operaciones individuales.

Ejemplo:

if (a > 10 && b < 20)

Representar:
- Obtener a.
- Comparar a > 10.
- Obtener b.
- Comparar b < 20.
- Evaluar AND.
- Obtener resultado booleano.
- Seleccionar la rama correspondiente.

Los caminos true y false deben tener colores y conexiones distinguibles.

Durante la ejecución:
- Resaltar las comparaciones.
- Mostrar sus operandos.
- Mostrar el resultado de cada comparación.
- Animar el camino seleccionado.
- Indicar por qué se eligió una rama.

### 5. VISUALIZACIÓN DE OPERACIONES ARITMÉTICAS Y LÓGICAS

Implementa nodos especializados para:
- Suma.
- Resta.
- Multiplicación.
- División.
- Módulo.
- Potencias.
- Comparaciones.
- AND, OR y NOT.
- Incrementos y decrementos.
- Asignaciones.
- Conversiones de tipos.

Cada nodo debe mostrar:
- Operadores.
- Valores de entrada.
- Tipo de dato.
- Resultado.
- Dependencias.
- Estado de ejecución.

Permite expandir cada operación para inspeccionar su evaluación.

Implementa evaluación visual de expresiones siguiendo la precedencia real de operadores y los paréntesis.

### 6. SISTEMA DE CONTROL DE EJECUCIÓN Y TIMING

Construye un motor de ejecución instrumentado con control granular del tiempo.

No utilices un simple setTimeout para simular una ejecución real. El tiempo visual debe controlar la presentación de eventos reales de ejecución instrumentada.

#### Intervalos configurables

Permite establecer:
- Intervalo entre instrucciones.
- Intervalo entre operaciones.
- Intervalo entre iteraciones.
- Intervalo entre funciones.
- Tiempo de transición de animaciones.
- Tiempo de visualización de cambios de variables.

Ofrece:
- Modo instantáneo.
- Modo rápido.
- Modo normal.
- Modo lento.
- Modo paso a paso.
- Velocidad personalizada.

Añade controles independientes para cada intervalo.

Permite configurar intervalos en milisegundos y guardar perfiles de velocidad.

El usuario debe poder modificar la velocidad durante la ejecución sin reiniciar el programa.

#### Time Travel Debugging

Implementa:
- Historial de estados.
- Snapshots.
- Reproducción.
- Avance y retroceso.
- Breakpoints.
- Watchpoints.
- Ejecución desde un estado anterior.
- Comparación entre dos estados.

El retroceso debe utilizar snapshots y registros de eventos, sin asumir que todos los programas pueden revertirse automáticamente. Los efectos externos deben identificarse y tratarse mediante reproducción determinista o limitaciones explícitas.

### 7. SISTEMA DE CONTEXT MENUS CON CLIC DERECHO

Implementa menús contextuales personalizados en toda la aplicación.

No utilices exclusivamente el menú contextual nativo del navegador.

El menú debe abrirse mediante clic derecho y adaptarse al elemento seleccionado.

#### Canvas de diagramas

Al hacer clic derecho sobre el canvas:
- Crear nueva sección.
- Crear nuevo nodo.
- Crear conexión.
- Crear grupo.
- Añadir comentario.
- Crear anotación.
- Insertar condición.
- Insertar operación.
- Insertar bucle.
- Crear subdiagrama.
- Pegar elementos.
- Seleccionar elementos.
- Ajustar zoom.
- Organizar automáticamente.
- Cambiar estilo de visualización.

Al hacer clic derecho sobre un nodo:
- Editar.
- Duplicar.
- Eliminar.
- Desactivar temporalmente.
- Expandir o contraer.
- Ver código asociado.
- Ver dependencias.
- Añadir breakpoint.
- Añadir watchpoint.
- Inspeccionar valores.
- Crear una sección a partir del nodo.

#### Explorador de archivos

Al hacer clic derecho sobre el explorador:
- Nuevo proyecto.
- Nueva carpeta.
- Nuevo archivo.
- Renombrar.
- Duplicar.
- Eliminar.
- Importar.
- Exportar.
- Abrir en otra pestaña.
- Crear sección de trabajo.
- Configurar como archivo principal.

Al hacer clic derecho sobre un archivo:
- Abrir.
- Renombrar.
- Duplicar.
- Eliminar.
- Copiar ruta.
- Ejecutar.
- Analizar.
- Generar diagrama.
- Añadir al proyecto.

#### Gestión de context menus

Los menús deben:
- Aparecer en la posición del cursor.
- Evitar salir de los límites de la ventana.
- Soportar submenús.
- Tener iconos.
- Mostrar atajos de teclado.
- Soportar navegación mediante teclado.
- Cerrar con Escape y al hacer clic fuera.
- Adaptarse al contexto y selección actual.
- Respetar los permisos y el estado de ejecución.

### 8. SISTEMA DE PROYECTOS Y EXPLORADOR DE ARCHIVOS

Implementa una arquitectura real de múltiples proyectos.

Cada proyecto debe tener:
- Identificador único.
- Nombre.
- Descripción.
- Lenguaje principal.
- Archivos.
- Carpetas.
- Configuración.
- Diagramas.
- Snapshots.
- Historial.
- Dependencias.
- Configuración de ejecución.

Permite tener múltiples proyectos abiertos simultáneamente y cambiar entre ellos mediante pestañas o un selector de proyectos.

Cada proyecto debe mantener su propio contexto.

El explorador debe permitir:
- Árbol jerárquico de archivos.
- Carpetas anidadas.
- Drag and drop.
- Renombrar.
- Crear.
- Eliminar.
- Mover.
- Copiar.
- Pegar.
- Búsqueda global.
- Filtros por extensión.
- Archivos abiertos recientemente.
- Indicadores de modificaciones sin guardar.

Los diagramas deben poder vincularse a archivos, funciones, clases o secciones específicas.

### 9. SECCIONES Y SUBDIAGRAMAS

Permite dividir los diagramas en secciones independientes.

Por ejemplo:
- Main.
- Initialization.
- Data Processing.
- Validation.
- Calculations.
- Output.

Cada sección puede contener múltiples nodos, conexiones y subdiagramas.

Permite:
- Crear secciones desde el menú contextual.
- Mover nodos entre secciones.
- Crear relaciones entre secciones.
- Contraer secciones.
- Expandir secciones.
- Navegar entre ellas.
- Ejecutar una sección individualmente cuando sea semánticamente posible.
- Ver dependencias entre secciones.

### 10. SISTEMA DE ESTILOS DE DIAGRAMAS

Implementa varios estilos visuales seleccionables.

No todos los diagramas deben tener el mismo aspecto.

Incluye:

A. Flowchart clásico:
Símbolos tradicionales, decisiones en rombos y procesos rectangulares.

B. Node Graph:
Nodos conectados con puertos de entrada y salida.

C. AST Tree:
Árbol jerárquico de sintaxis y expresiones.

D. Data Flow:
Visualización de datos, transformaciones y dependencias.

E. Execution Flow:
Animaciones que muestran el recorrido real de ejecución.

F. Blueprint:
Estética de programación visual basada en nodos.

G. Sequence Diagram:
Interacciones entre funciones y componentes a través del tiempo.

H. Minimal:
Representación limpia, compacta y con mínima decoración.

Cada estilo debe tener:
- Colores configurables.
- Formas de nodos configurables.
- Grosor de conexiones.
- Tipo de conectores.
- Espaciado.
- Animaciones.
- Tipografía.
- Densidad visual.
- Indicadores de ejecución.

Permite guardar presets personalizados y asignar estilos diferentes a diferentes diagramas.

### 11. EDITOR DE CÓDIGO Y SINCRONIZACIÓN

Utiliza Monaco Editor o equivalente.

Implementa:
- Resaltado de sintaxis.
- Autocompletado.
- Diagnósticos.
- Navegación entre funciones.
- Búsqueda.
- Múltiples pestañas.
- Breakpoints.
- Indicadores de ejecución.
- Selección sincronizada entre código y diagrama.

Los cambios en el código deben actualizar los diagramas.

Los cambios en los nodos deben actualizar el código.

Utiliza una representación intermedia del programa y transformaciones controladas para evitar perder comentarios, formato y estructuras que no puedan representarse visualmente.

Los conflictos deben detectarse y ofrecer una resolución explícita.

### 12. VARIABLES, MEMORIA Y ESTADO

Construye un inspector avanzado.

Mostrar:
- Variables globales.
- Variables locales.
- Variables de funciones.
- Parámetros.
- Objetos.
- Arrays.
- Diccionarios.
- Punteros cuando el lenguaje los soporte.
- Tipos.
- Valores.
- Cambios.
- Historial.
- Ámbito.

Implementa visualización de referencias y relaciones entre objetos.

Resalta automáticamente las variables modificadas en cada paso.

### 13. ARQUITECTURA TÉCNICA

Frontend:
- React.
- TypeScript.
- Material 3 Expressive.
- Material Color Utilities.
- Monaco Editor.
- React Flow / XYFlow.
- Zustand o equivalente para estado global.
- Motion para animaciones.

Backend y ejecución:
- Runtime adapters por lenguaje.
- AST parsers.
- Instrumentación de ejecución.
- Workers o runtimes aislados.
- WebAssembly cuando corresponda.
- Sandboxes de backend para lenguajes que lo necesiten.
- Comunicación mediante eventos estructurados.
- Persistencia de proyectos.

Separa:
1. Code Parser.
2. Intermediate Representation.
3. Diagram Engine.
4. Execution Engine.
5. State Inspector.
6. Timeline Engine.
7. Bidirectional Synchronizer.
8. Project Manager.
9. Context Menu System.
10. Theme Engine.

Los diagramas deben derivarse de estructuras semánticas reales del código y los datos de ejecución deben proceder del runtime, no de simulaciones.

Implementa límites de recursos, aislamiento de código, cancelación efectiva y manejo seguro de errores.

### 14. UX Y EXPERIENCIA DE USUARIO

La interfaz debe sentirse como un IDE profesional de nueva generación.

Incluye:
- Paneles redimensionables.
- Layouts personalizables.
- Docking de paneles.
- Atajos de teclado.
- Command Palette.
- Búsqueda global.
- Tooltips.
- Breadcrumbs.
- Undo/Redo.
- Historial.
- Notificaciones.
- Estados vacíos bien diseñados.
- Skeleton loading.
- Accesibilidad.
- Responsive design.

Permite guardar diferentes layouts y restaurarlos.

La navegación debe ser fluida incluso con diagramas grandes.

Implementa virtualización y renderizado eficiente para evitar problemas de rendimiento.

### 15. OBJETIVO FINAL Y CRITERIOS DE CALIDAD

Construye un producto funcional y no una demostración estática.

Prioriza en este orden:
1. Precisión del análisis semántico.
2. Diagramas detallados.
3. Visualización real de loops y condiciones.
4. Control de ejecución por pasos e intervalos.
5. Variables en tiempo real.
6. Edición bidireccional.
7. Gestión de proyectos y archivos.
8. Context menus.
9. Personalización de diagramas.
10. Identidad visual Material 3 Expressive.

Implementa primero JavaScript y Python de forma completa, y prepara adaptadores extensibles para Lua, TypeScript, Java, C, C++, Rust y Go.

Incluye pruebas automatizadas, ejemplos de proyectos, documentación técnica y manejo de errores.

No presentes funciones como implementadas si solo son elementos visuales. Cada interacción debe tener un comportamiento funcional y verificable.

El resultado debe sentirse como una combinación de IDE, debugger avanzado, herramienta de análisis algorítmico y entorno de programación visual.

---

## 3. Corrección del generador de Flowcharts

**Objetivo:** corregir el generador de diagramas para que siga la convención estándar de flowchart y no genere bloques genéricos ni diagramas ilegibles.

Mejora de la lógica y generación de diagramas de flujo (Flowcharts)

Quiero que modifiques la lógica de generación de diagramas para que estos sigan las convenciones y la estructura de un diagrama de flujo (Flowchart) estándar.

**1. Implementar lógica real de Flowchart**

El diagrama debe representar correctamente el flujo lógico del proceso, identificando automáticamente:

- **Decisiones:** condiciones que generan diferentes caminos (Sí/No, Verdadero/Falso).
- **Bucles:** procesos que se repiten hasta cumplir una condición.
- **Procesos:** acciones, operaciones o etapas generales.
- **Entradas y salidas:** información que ingresa o resultados que se generan.
- **Conectores:** enlaces entre diferentes etapas del proceso.
- **Inicio y fin:** puntos de entrada y terminación del flujo.

Las conexiones deben representar la secuencia lógica real, no simplemente unir los elementos de forma consecutiva.

**2. Respetar la simbología estándar**

Cada elemento debe utilizar la figura geométrica correspondiente a su función:

- **Óvalo:** inicio y fin del proceso.
- **Rectángulo:** procesos, acciones u operaciones.
- **Rombo:** decisiones y condiciones que generan bifurcaciones.
- **Paralelogramo:** entradas y salidas de datos.
- **Círculo:** conectores internos del diagrama, cuando sean necesarios.
- **Flechas:** dirección y continuidad del flujo.

No utilizar rectángulos genéricos para representar todos los elementos. La forma debe comunicar visualmente el tipo de operación que representa cada nodo.

**3. Priorizar la simplicidad y legibilidad**

Evitar diagramas excesivamente detallados que terminen siendo difíciles de interpretar.

Actualmente, el diagrama puede generar demasiados cuadros para representar acciones pequeñas o demasiado específicas. Quiero cambiar este comportamiento.

Aplicar los siguientes criterios:

- Agrupar acciones pequeñas que formen parte de un mismo proceso.
- Representar las etapas principales, no cada instrucción individual.
- Evitar crear nodos para acciones triviales, redundantes o que no aporten valor al entendimiento del flujo.
- Simplificar procesos complejos sin perder su lógica principal.
- Reducir cruces innecesarios entre flechas.
- Mantener una distribución visual ordenada y equilibrada.
- Utilizar nombres cortos, descriptivos y fáciles de entender en cada nodo.
**4. Representar correctamente las decisiones y los bucles**

Las decisiones deben utilizar rombos y tener salidas claramente identificadas según sus posibles resultados.

Los bucles deben mostrar visualmente el retorno hacia la etapa que se repite y la condición que permite salir del ciclo.

Evitar representar decisiones o ciclos como simples secuencias lineales de rectángulos.

**5. Objetivo final**

El resultado debe ser un diagrama de flujo profesional, intuitivo y fácil de leer.

La prioridad debe ser comunicar correctamente la lógica general del proceso, no representar cada pequeño detalle de implementación.

Regla principal: menos nodos, pero mejor representados. Cada figura debe tener un propósito lógico y visual. El diagrama debe poder entenderse rápidamente sin necesidad de leer una gran cantidad de cuadros.

---

## 4. Aplicación de las correcciones

**Objetivo:** pasar del análisis a la implementación: corregir la simbología, los analizadores de JavaScript y Python, el parser de expresiones y el aislamiento de la ejecución, y validarlo con pruebas.

Quiero que procedas a implementar las correcciones identificadas en el análisis anterior. No te limites a describir los problemas: modifica directamente el código del proyecto.

Prioriza las siguientes tareas:

**1. Corregir la generación de diagramas Flowchart**

Implementa la simbología estándar:

- Óvalos para inicio y fin.
- Rectángulos para procesos.
- Rombos para decisiones.
- Paralelogramos para entradas y salidas.
- Círculos para conectores.

Cada nodo debe utilizar la figura correspondiente a su función lógica, no solamente cambiar colores o bordes.

**2. Corregir la lógica de ejecución de JavaScript y Python**

Revisa y corrige el analizador de ambos lenguajes para que los diagramas representen fielmente el flujo de ejecución.

En particular:

- Corregir la secuencia de instrucciones dentro de funciones y clases de Python.
- Representar correctamente los retornos (return).
- Corregir las rutas de break y continue.
- Corregir la estructura y conexiones de los bucles do while.
- Representar correctamente las condiciones de entrada, repetición y salida de los ciclos.
- Evitar conexiones que contradigan el comportamiento real del código.
**3. Reducir la complejidad de los diagramas**

Esta es una prioridad importante.

Eliminar la generación de nodos individuales para variables, literales y expresiones pequeñas.
Agrupar instrucciones relacionadas en procesos generales.
Mostrar únicamente las operaciones que aporten valor para comprender el flujo.
Mantener las decisiones y los bucles como elementos independientes.
Establecer un límite razonable de nodos para evitar diagramas excesivamente grandes.
Evitar que la simplificación elimine información importante sobre la lógica del programa.

El objetivo es que los diagramas sean compactos, profesionales y fáciles de entender.

**4. Corregir el parser de expresiones Python**

- Comprobar que se consuman todos los tokens durante el análisis.
- Corregir la interpretación de diccionarios.
- Soportar correctamente comprensiones y expresiones multilínea.
- Evitar aceptar análisis parciales como si fueran correctos.
- Manejar construcciones no soportadas sin generar diagramas engañosos.

**5. Revisar la seguridad de los entornos de ejecución**

- El análisis identificó que los mecanismos actuales de aislamiento de JavaScript y Python pueden ser evadidos.
- No confiar en ocultar o reemplazar globales como mecanismo de seguridad.
- Revisar las capacidades accesibles desde los workers.
- Implementar aislamiento real mediante mecanismos adecuados.
- Si no es posible garantizarlo, no permitir ejecutar código no confiable y documentar claramente la limitación.
**6. Pruebas y validación**

Después de implementar los cambios:

- Ejecutar las pruebas existentes.
- Agregar pruebas para decisiones, bucles, funciones, retornos, break y continue.
- Probar ejemplos equivalentes en JavaScript y Python.
- Verificar que las conexiones de los diagramas coincidan con el flujo real.
- Comprobar que los diagramas simplificados sigan siendo correctos.
- Ejecutar la verificación de TypeScript y corregir los errores que aparezcan.

**Consideraciones importantes**

- No elimines funcionalidades existentes.
- No rompas la compatibilidad con los diagramas actuales sin necesidad.
- Mantén la arquitectura y el estilo visual del proyecto.
- Evita soluciones superficiales o únicamente visuales.
- Refactoriza los componentes necesarios si la arquitectura actual impide implementar correctamente estas mejoras.

**Resultado esperado**

Un generador de diagramas de flujo que represente correctamente la lógica de JavaScript y Python, utilice simbología estándar, produzca diagramas compactos y legibles, y tenga un entorno de ejecución con garantías de seguridad adecuadas.

Al finalizar, presenta un resumen de los archivos modificados, las mejoras implementadas, las pruebas realizadas y cualquier limitación que permanezca.

No te detengas después de identificar problemas. Implementa, prueba y corrige hasta completar el trabajo.

---

## 5. Layout vertical y ejecución de código

**Objetivo:** rehacer la distribución visual de los diagramas en vertical y habilitar la ejecución real de JavaScript y Python, con su aislamiento resuelto.

Continuar mejoras del generador de diagramas y habilitar ejecución de código

Quiero que continúes trabajando sobre el estado actual del proyecto. No empieces desde cero ni reviertas las correcciones anteriores. Ahora quiero enfocarme en mejorar la distribución visual de los diagramas y habilitar correctamente la ejecución de código JavaScript y Python.

**1. Cambiar la orientación de los diagramas: Top to Bottom**

Todos los diagramas deben organizarse de arriba hacia abajo (Top to Bottom).

- El inicio del flujo debe ubicarse en la parte superior.
- Las acciones deben distribuirse verticalmente.
- Las decisiones deben generar bifurcaciones claras hacia abajo.
- Los ciclos deben mostrar sus retornos sin desorganizar el resto del diagrama.
- El final del flujo debe quedar en la parte inferior.
- Evitar distribuciones horizontales excesivas.

La dirección principal del flujo debe ser vertical, incluso cuando existan decisiones, condiciones o múltiples caminos.

**2. Corregir la distribución y el aspecto visual de los diagramas**

Actualmente, los diagramas se visualizan como si todo el contenido estuviera encerrado dentro de un gran cubo o bloque compacto. Quiero corregir completamente ese comportamiento visual.

Implementa lo siguiente:

- Evitar que los nodos se agrupen formando grandes bloques cuadrados o rectangulares.
- Utilizar una distribución vertical natural y equilibrada.
- Aprovechar mejor el espacio disponible en el lienzo.
- Mantener una separación adecuada entre nodos.
- Evitar que las flechas atraviesen otros nodos.
- Reducir los cruces de conexiones.
- Evitar que las bifurcaciones de decisiones se amontonen.
- Mantener los ciclos visualmente separados de las secuencias principales.
- Evitar espacios vacíos exagerados entre elementos.
- Permitir que el diagrama crezca verticalmente según su complejidad.

El resultado debe parecer un diagrama de flujo profesional, no un conjunto de elementos comprimidos dentro de un cubo.

**3. Mejorar las conexiones y el recorrido visual**

Las flechas deben seguir una dirección lógica y fácil de interpretar.

- Priorizar conexiones verticales.
- Utilizar conexiones laterales únicamente cuando sean necesarias para bifurcaciones.
- Identificar claramente las salidas de los rombos (Sí/No o Verdadero/Falso).
- Mostrar los retornos de los ciclos de manera clara.
- Evitar conexiones superpuestas, innecesariamente largas o confusas.
- Mantener una jerarquía visual clara entre el flujo principal y los caminos secundarios.

**4. Habilitar la ejecución de JavaScript y Python**

Quiero que la ejecución de código JavaScript y Python esté habilitada y funcione correctamente desde la interfaz del proyecto.

JavaScript:

- Habilitar la ejecución del código introducido por el usuario.
- Mostrar los resultados de ejecución.
- Capturar y mostrar errores.
- Permitir volver a ejecutar el código después de modificarlo.
- Evitar que la ejecución bloquee la interfaz.

Python:

- Habilitar la ejecución del código introducido por el usuario.
- Mostrar resultados y salidas de consola.
- Capturar y mostrar errores de ejecución.
- Permitir ejecutar nuevamente después de editar el código.
- Mantener una experiencia consistente con JavaScript.

**5. Seguridad de la ejecución**

Antes de habilitar la ejecución, corrige las vulnerabilidades de aislamiento identificadas anteriormente.

- No considerar el ocultamiento de variables globales como un mecanismo de seguridad.
- No ejecutar código potencialmente no confiable en el contexto principal de la aplicación.
- Utilizar un entorno aislado con límites de recursos y tiempo.
- No exponer acceso innecesario al navegador, sistema, archivos, red o secretos.
- Si una modalidad de ejecución no puede garantizar un aislamiento adecuado, no presentarla como segura.

La funcionalidad debe estar habilitada sin comprometer la seguridad de la aplicación.

**6. Validación final**

Después de implementar los cambios:

- Probar diagramas sencillos y complejos.
- Probar diagramas con decisiones anidadas.
- Probar ciclos for, while y do while.
- Verificar que todos los diagramas mantengan la orientación de arriba hacia abajo.
- Comprobar que las flechas y bifurcaciones sean legibles.
- Ejecutar código JavaScript y Python válido.
- Probar errores de sintaxis y errores de ejecución.
- Comprobar que la interfaz siga respondiendo mientras se ejecuta el código.
- Ejecutar todas las pruebas y la verificación de TypeScript.

**Resultado esperado**

Quiero dos mejoras funcionales y visibles:

- **Diagramas:** una distribución vertical (Top to Bottom), limpia, espaciosa y profesional, sin esa apariencia de cubo o bloque compacto.
- **Ejecución:** poder escribir, editar y ejecutar código JavaScript y Python directamente desde la aplicación, visualizar sus resultados y recibir sus errores.

Implementa los cambios directamente en el proyecto. No te limites a hacer ajustes de CSS ni a describir lo que habría que hacer. Revisa la arquitectura, modifica los componentes y la lógica necesarios, ejecuta las pruebas y corrige los problemas encontrados.

---

## 6. Sistema de logros y progresión

**Objetivo:** agregar un sistema de logros por niveles de dificultad que premie el uso de la plataforma, la escritura de código y la ejecución de programas.

Implementar sistema de logros y progresión (Achievements)

Quiero implementar un sistema completo de logros dentro de la aplicación, enfocado en recompensar el aprendizaje, la experimentación y el progreso del usuario al programar.

La idea es que el usuario pueda desbloquear logros a medida que utiliza las funcionalidades de la plataforma, escribe código, ejecuta programas y aprende nuevos conceptos.

**1. Sistema de niveles de dificultad**

Los logros deben estar organizados en diferentes niveles de dificultad.

Propongo las siguientes categorías:

- **Principiante:** primeros pasos e interacciones básicas con el editor.
- **Intermedio:** dominio de estructuras básicas, condiciones y ciclos.
- **Avanzado:** resolución de problemas y uso de estructuras más complejas.
- **Experto:** retos de programación más exigentes y dominio de funcionalidades.
- **Legendario:** logros especiales, difíciles de conseguir y destinados a usuarios destacados.

Cada categoría debe tener una identidad visual propia, manteniendo coherencia con el diseño actual de la aplicación.

**2. Primeros logros**

Crear inicialmente una colección de logros como los siguientes:

**Principiante**

- ¡Hola, mundo! — Escribe tu primer Hello World.
- Primeros pasos — Escribe tu primera línea de código.
- ¡Funciona! — Ejecuta correctamente tu primer programa.
- Sin errores — Ejecuta un programa sin errores por primera vez.
- Curioso — Ejecuta código varias veces experimentando con diferentes resultados.

**Intermedio**

- Pensamiento lógico — Utiliza tu primera estructura condicional (if).
- Decisiones — Implementa una estructura if/else.
- Repetición — Crea tu primer ciclo (for o while).
- Coleccionista — Utiliza un array o una lista.
- Reutilización — Crea y ejecuta tu primera función.

**Avanzado**

- Control del flujo — Combina condiciones y ciclos.
- Arquitecto de procesos — Genera tu primer diagrama con decisiones y bifurcaciones.
- Cazador de errores — Corrige un error de ejecución.
- Multilenguaje — Ejecuta correctamente código tanto en JavaScript como en Python.

**Experto**

- Pensamiento estructurado — Construye un diagrama con múltiples decisiones y ciclos.
- Resolutor — Encuentra y corrige el error que impide que un programa con funciones y ciclos funcione.
- Viaje en el tiempo — Retrocede la ejecución a un estado anterior y retoma desde ahí con el mismo resultado.

**Legendario**

- Maestro de flujos — Genera un diagrama complejo con bucles anidados, decisiones y caminos de retorno.
- Constructor de sistemas — Crea un proyecto con varios archivos y diagramas sincronizados con el código.
- Eterno estudiante — Desbloquea al menos un logro de cada una de las categorías.

**3. Desbloqueo y seguimiento de eventos**

Define cada logro con: identificador, nombre, descripción, categoría, icono, condición de desbloqueo y estado.

El sistema debe emitir eventos a partir de las acciones reales del usuario:

- Código escrito o modificado.
- Programa ejecutado por primera vez.
- Ejecución completada sin errores.
- Estructura condicional utilizada.
- Ciclo creado.
- Array o lista utilizado.
- Función creada y ejecutada.
- Diagrama generado con decisiones o bifurcaciones.
- Modificación de un nodo del diagrama sincronizada con el código.
- Breakpoint o watchpoint añadido.
- Programa ejecutado en más de un lenguaje.
- Proyecto creado con varios archivos.
- Logro desbloqueado.

Cada logro se evalúa en el momento en que ocurre el evento que cumple su condición, sin recargar la aplicación ni bloquear la ejecución.

- Un logro desbloqueado se notifica una sola vez y queda registrado con fecha.
- Un logro ya desbloqueado no vuelve a notificarse.
- Los logros se evalúan de forma determinista: el mismo evento produce siempre el mismo resultado.
- La evaluación no debe alterar el código, el diagrama ni el estado de la ejecución.

**4. Progresión y rangos**

- Cada categoría tiene su propio progreso, calculado sobre los logros que la componen.
- La aplicación muestra un progreso global, la suma de todos los logros desbloqueados.
- El usuario asciende de rango a medida que desbloquea logros:
  - Principiante, Intermedio, Avanzado, Experto, Legendario.
- El rango actual se muestra junto con el progreso global.
- Al completar el 100% de una categoría, se muestra un distintivo de categoría completada.
- La barra de progreso se actualiza en vivo, sin recargar.

**5. Interfaz de logros**

- Panel lateral con la retícula de logros agrupados por categoría.
- Los logros bloqueados se muestran atenuados, con su condición descrita y sin revelar información interna.
- Detalle al seleccionar un logro: descripción, categoría, progreso y fecha de desbloqueo.
- Notificación al desbloquear un logro, con animación breve y sonido opcional.
- Contador de logros con acceso rápido en la barra superior.
- Resumen de progreso visible en la pantalla de inicio.
- Coherencia con Material 3 Expressive: color propio por categoría, adaptación a modo claro y oscuro, iconografía de Material Symbols y animaciones con Motion.
- El panel de logros no debe interrumpir la edición ni la ejecución del código.

**6. Persistencia**

- Guardar el estado de cada logro, su fecha de desbloqueo y el progreso por categoría.
- Conservar el progreso al cerrar y reabrir la aplicación y al recargar la página.
- Guardar el progreso global y el progreso por proyecto, sin mezclar ambos.
- Si la aplicación ya tiene infraestructura de sincronización, reutilizarla para el progreso.
- El reinicio del progreso debe ser una acción explícita y confirmada.

**7. Validación**

- Cada logro debe tener al menos un caso de prueba que verifique que se desbloquea cuando corresponde.
- Verificar también los casos en que un logro no debe desbloquearse.
- Verificar que un evento repetido no genera notificaciones duplicadas.
- Probar el desbloqueo en cada lenguaje con soporte de ejecución.
- Comprobar que el progreso persiste tras recargar la aplicación.
- Comprobar que la interfaz sigue respondiendo mientras se evalúan los logros.
- Ejecutar todas las pruebas y la verificación de TypeScript.

**Resultado esperado**

El usuario ve su progreso dentro de la propia aplicación: logros que se desbloquean mientras programa y ejecuta código, un panel organizado por categorías y un progreso que se conserva entre sesiones.

Cada logro debe corresponderse con una acción real del usuario y ser verificable mediante un evento, nunca con un estado simulado.
