# Semana 3 · CodeFlow Studio

Se construyó **CodeFlow Studio**, un entorno de programación visual que permite escribir código, ejecutarlo paso a paso, ver su estado interno y modificarlo desde diagramas de flujo interactivos. Todo el proyecto se generó con ayuda de IA, iterando sobre una secuencia de prompts.

- **Repositorio del proyecto:** <https://github.com/kkokotero/codeflow-studio>
- **Sitio principal:** <https://codeflow-studio.kkoko.dev>
- **Sitio alterno:** <https://codeflow-studio-one.vercel.app>

El código de la aplicación vive en el repositorio enlazado; en esta carpeta se conservan la bitácora de prompts que se usaron para construirla y la presentación del proyecto.

## Archivos

- [`propmts.md`](./propmts.md) — bitácora de los 6 prompts que se aplicaron, en orden, con índice y el texto original de cada uno.
- [`presentacion-codeflow-studio.pdf`](./presentacion-codeflow-studio.pdf) — presentación del proyecto en PDF, 12 diapositivas.

## Presentación

El deck de 12 diapositivas recorre el proyecto de la idea a la prueba:

| # | Diapositiva | Contenido |
| --- | --- | --- |
| 1 | Portada | CodeFlow Studio: «Mira tu código como lo ve el programa». |
| 2 | El problema | Leer código línea a línea no muestra el camino completo; las condiciones anidadas, bucles y retornos esconden qué se ejecuta y cuándo. |
| 3 | La idea | El código es texto, la lógica es un camino: cada programa se convierte en un diagrama de flujo. |
| 4 | Cómo funciona | Del código al diagrama mediante análisis estático, sin ejecutar código arbitrario. |
| 5 | Ejemplo | `sumTo(limit)` convertido en su flujo. |
| 6 | Símbolos | Cada figura tiene un significado; el diagrama usa simbología estándar. |
| 7 | Espacio de trabajo | Proyectos, paquetes `.codeflow.json`, archivos y carpetas. |
| 8 | Progreso | Experiencia con XP, insignias y logros, y la sugerencia del siguiente paso. |
| 9 | Lenguajes | JavaScript, TypeScript, Python, Java, C, C++, C#, Go, Rust y Lua con la misma visualización. |
| 10 | Audiencia | Principiantes, estudiantes y avanzados. |
| 11 | Seguridad | Análisis estático y ejecución sin código arbitrario. |
| 12 | Pruébalo | Código QR y enlace a la demo en Vercel. |

## Cómo se construyó

El proyecto se construyó de forma iterativa: cada prompt parte del estado anterior y agrega o corrige algo concreto.

1. **Prompt maestro** — descripción compacta del producto: interfaz tipo IDE, lenguajes soportados, visualización, runtime, editor visual, arquitectura y entrega.
2. **Especificación detallada** — 15 secciones que profundizan identidad visual (Material 3 Expressive), sistema de diagramas, visualización de loops y condicionales, motor de ejecución, menús contextuales, gestor de proyectos, estilos de diagramas, sincronización bidireccional, arquitectura y UX.
3. **Corrección del generador de diagramas** — lógica de Flowchart real, con la simbología estándar (rombos para decisiones, paralelogramos para entrada/salida, óvalos para inicio y fin) y conexiones que respetan la secuencia lógica.
4. **Aplicación de correcciones** — instrucciones para corregir los problemas detectados en el análisis previo modificando directamente el código del proyecto.
5. **Layout y ejecución** — reorganización de los diagramas de arriba hacia abajo (Top to Bottom) y habilitación de la ejecución real de JavaScript y Python.
6. **Logros y progresión** — sistema de niveles y logros que se desbloquean al usar la plataforma, escribir código y ejecutar programas.

## Alcance definido en los prompts

**Interfaz:** panel de archivos, editor con resaltado de sintaxis, canvas central de diagramas, inspector de variables, consola y barra de control de ejecución, con paneles redimensionables.

**Lenguajes:** JavaScript, TypeScript, Python, Lua, Java, C, C++, C#, Go y Rust, mediante adaptadores extensibles y detección automática.

**Visualización:** el código se convierte en nodos y conexiones que representan funciones, variables, condiciones, bucles, llamadas, eventos, clases, objetos y dependencias. El nodo activo se resalta durante la ejecución.

**Runtime:** ejecución, pausa, reanudación, detención, reinicio, paso a paso, velocidad ajustable, breakpoints y seguimiento del estado; se inspeccionan variables locales y globales, pila de llamadas, argumentos y valores de retorno.

**Editor visual:** los nodos se pueden arrastrar y modificar, y los cambios se reflejan en el código fuente en ambos sentidos, con resolución de conflictos.

**Funciones adicionales:** historial de ejecución, snapshots, comparación de estados, búsqueda de variables, zoom, exportación e importación de archivos y proyectos con múltiples archivos.

## Stack

React, TypeScript, Monaco Editor, React Flow, Material 3 Expressive con Material Color Utilities, Zustand para el estado global y Motion para las animaciones. La ejecución del código se aísla en runtimes separados (Workers, WebAssembly o sandboxes de backend según el lenguaje), con límites de CPU, memoria y tiempo; nunca se ejecuta código arbitrario en el contexto principal del navegador.
