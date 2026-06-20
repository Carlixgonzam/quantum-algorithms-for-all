# Simulación cuántica de circuitos booleanos

## El problema

Las compuertas AND, OR y FANOUT clásicas **no son reversibles** en su forma directa (pierden información sobre las entradas). Pero toda compuerta cuántica tiene que ser unitaria — y por lo tanto, reversible. ¿Cómo se convierte un circuito booleano arbitrario en su versión cuántica?

## La solución estándar

Por cada puerta AND, OR o FANOUT del circuito booleano, se agrega **un único qubit de trabajo** (workspace qubit), inicializado en $|0\rangle$, y se usa una compuerta tipo Toffoli (CCX) o su análoga para escribir el resultado en ese qubit nuevo — preservando intactos los valores de entrada en sus propios qubits.

- **NOT** no necesita qubit extra: se implementa directamente con una compuerta $X$, que ya es reversible por sí misma.
- **AND, OR, FANOUT** sí necesitan su qubit auxiliar cada una.

## Por qué esto importa para el costo

Como solo se necesita **un** qubit extra por puerta (no dos), y cada puerta booleana se traduce en un número constante de compuertas cuánticas, el tamaño total del circuito cuántico resultante crece **linealmente** con el tamaño del circuito booleano original — no cuadráticamente.

## La idea de fondo

La reversibilidad se "compra" con **espacio** (qubits auxiliares), no con tiempo extra ni con pérdida de información. Esta es la misma razón por la que Grover puede correr sobre cualquier función para la que se conozca un circuito booleano: esta construcción es el puente que convierte cualquier función clásica en un oráculo cuántico unitario utilizable.

Ver `banco-de-problemas/costo-de-circuitos-y-compuertas.md` (Problema 2).
