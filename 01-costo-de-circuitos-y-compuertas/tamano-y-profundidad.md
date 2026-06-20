# Tamaño (size) y profundidad (depth) de un circuito

## Definiciones

- **Size:** número total de puertas del circuito, sin importar en qué qubit actúen.
- **Depth:** longitud del camino más largo de dependencias entre puertas — es decir, cuántos "pasos secuenciales" mínimos hacen falta para ejecutar el circuito si las puertas que no comparten qubits se pueden correr en paralelo.

## El error más común: confundir columnas visuales con depth real

Cuando dibujás un circuito, las puertas suelen alinearse visualmente en columnas — pero esas columnas **no siempre corresponden a la profundidad real**. Dos puertas pueden parecer estar en la misma columna del diagrama y, sin embargo, pertenecer a capas de dependencia distintas si actúan sobre qubits que se usaron en momentos diferentes.

## Método correcto: scheduling por capas

1. Inicializá un contador de "capa actual" en 0 para cada qubit.
2. Recorré las puertas del circuito en su orden real (de izquierda a derecha, como están dibujadas, qubit por qubit).
3. Para cada puerta, su capa = `max(capa de cada qubit que toca) + 1`.
4. Actualizá la capa de todos los qubits que toca esa puerta.
5. El depth final es el máximo de todas las capas asignadas.

## Ejemplo trabajado

Circuito de 5 qubits: H en q0,q1,q2 → CNOT(q0→q4) → T(q0) → CNOT(q1→q2) → Y(q3) → CNOT(q3→q2) → Z(q1) → CNOT(q4→q2).

| Capa | Puertas |
|---|---|
| 1 | H(q0), H(q1), H(q2), Y(q3) |
| 2 | CNOT(q0→q4), CNOT(q1→q2) |
| 3 | T(q0), CNOT(q3→q2), Z(q1) |
| 4 | CNOT(q4→q2) |

**Size = 10** (cuento todas las puertas). **Depth = 4** (la última CNOT depende de q4, usado en capa 2, y de q2, usado en capa 3).

Ver `banco-de-problemas/costo-de-circuitos-y-compuertas.md` (Problema 1) para la versión completa con todas las opciones de respuesta descartadas.
