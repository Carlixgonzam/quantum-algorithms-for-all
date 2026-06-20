# Laboratorio de Algoritmos Cuánticos

Notas de estudio, derivaciones completas y banco de problemas que armé mientras cursaba *Fundamentals of Quantum Algorithms* (IBM Quantum). No es un resumen pasivo del curso — es la versión que me hubiera gustado tener antes de empezar: con las cuentas hechas hasta el final, los porqués explicados (no solo el resultado), y los errores típicos marcados justo donde más duelen en un parcial.

Cubre desde matrices unitarias y el modelo de consultas hasta Deutsch-Jozsa, Simon, Grover, estimación de fase, la QFT y Shor. Si estás preparando un examen de algoritmos cuánticos, monitoreando un curso, o simplemente queriendo entender *por qué* funciona cada algoritmo y no solo memorizar la fórmula final, esto te debería servir.

## Cómo está organizado

```
laboratorio-de-algoritmos-cuanticos/
├── 00-fundamentos/                          → matrices unitarias, modelo de consultas
├── 01-costo-de-circuitos-y-compuertas/      → size/depth, conjuntos universales, simulación de circuitos booleanos
├── 02-deutsch-jozsa-y-simon/                → con y sin phase kickback, qué pasa sin promesa
├── 03-grover/                               → geometría, iteraciones óptimas, límites del speedup
├── 04-estimacion-de-fase/                   → el bloque de construcción detrás de Shor
├── 05-qft/                                  → la transformada cuántica de Fourier y sus propiedades
├── 06-shor-y-orden-modular/                 → factorización vía el problema del orden
├── 07-swap-test-y-otros-circuitos/          → medir similitud entre estados
├── banco-de-problemas/                      → preguntas tipo examen, organizadas por tema, con solución razonada
├── hojas-de-referencia/                     → fórmulas + tabla comparativa de los cuatro algoritmos
└── recursos/                                → diagramas reutilizables
```

Cada módulo temático (`00` a `07`) sigue la misma estructura interna:

- **Teoría** (`*.md`): la derivación completa, no solo el resultado. Si una fórmula aparece, vas a ver de dónde sale.
- **`notebooks/`**: implementaciones en Qiskit para verificar todo numéricamente — porque confiar ciegamente en una derivación a mano es la forma más rápida de arrastrar un error tres preguntas más adelante.
- **`ejercicios/`**: preguntas tipo examen específicas de ese tema, con solución explicada paso a paso.

## Por qué existe este repo

Porque la diferencia entre "entender Grover" y "saber resolver un problema de Grover" es enorme, y casi todo el material que circula se queda en la primera parte. Cada documento de este repo intenta cerrar esa brecha: parte de la intuición geométrica o algebraica, pero siempre termina en números concretos y en la pregunta de "¿y si rompo la promesa del problema, qué pasa?" — porque ahí es donde realmente se entiende un algoritmo.

## Stack

- Python 3.11+ / Qiskit
- Jupyter
- Markdown + LaTeX para la notación (compatible con GitHub y con Obsidian)

## Estado

🚧 En construcción activa — lo voy llenando a medida que avanzo en el curso y repaso para los parciales. Si encontrás un error o una derivación que se puede explicar mejor, abrí un issue.

## Licencia

MIT para el código, CC-BY-SA para las notas en prosa. Ver `LICENCIA`.
