# El modelo de consultas (query model)

## La idea central

El modelo de consultas mide la complejidad de un algoritmo contando **cuántas veces consulta a un oráculo** (caja negra), tratando cada consulta como una unidad de costo fijo — sin importar qué tan complicado sea el oráculo por dentro.

Esto es lo que permite, por ejemplo, decir que "Deutsch-Jozsa resuelve el problema con 1 consulta cuántica vs. $2^{n-1}+1$ consultas clásicas en el peor caso" sin tener que especificar nunca cómo está implementado $f$.

## Punto clave: qué SÍ y qué NO se cuenta

- **El oráculo representa el input del problema.** No se tiene acceso a su estructura interna, solo a las respuestas que da.
- **El costo de construir el oráculo NO se cuenta.** Esto es exactamente lo contrario de lo que muchas veces se asume por error — el modelo abstrae *deliberadamente* ese costo, no lo incluye.
- **En el entorno cuántico, las compuertas de consulta deben ser unitarias.** A diferencia del caso clásico (donde el oráculo puede ser cualquier función, incluso no reversible), construir una versión cuántica del oráculo requiere cuidado especial para garantizar reversibilidad — normalmente vía un "phase oracle" o kickback de fase.

## La tensión que vale la pena recordar

El modelo de consultas es poderoso *porque* ignora el costo de construcción del oráculo (eso es lo que lo hace una herramienta limpia para comparar algoritmos). Pero esa misma abstracción es su mayor limitación: **no siempre refleja problemas reales**, donde construir el oráculo mismo puede ser el verdadero cuello de botella computacional.

Ver `banco-de-problemas/fundamentos-y-otros-circuitos.md` (Problema 2) para la pregunta tipo examen sobre este tema.
