# Conjuntos universales de compuertas

## Qué significa "universal"

Un conjunto de compuertas es universal si permite aproximar **cualquier** operación unitaria (sobre cualquier número de qubits) con precisión arbitraria, usando solo compuertas de ese conjunto. El teorema de **Solovay-Kitaev** garantiza además que el número de compuertas necesario crece de forma eficiente (poli-logarítmica) con la precisión deseada.

## Universalidad es estructural, no específica de compuertas

Esto es lo que más vale la pena internalizar: **no existe una única "receta" de compuertas necesaria**. Lo que se necesita, a nivel estructural, es:

- Suficiente **entrelazamiento de 2 qubits** (cualquier compuerta entrelazante no-Clifford-trivial sirve: CNOT, CZ, iSWAP, controlled-S, etc.)
- Suficiente **diversidad de rotaciones de 1 qubit** para escapar del grupo de Clifford (T es la elección clásica, pero no la única).

Por eso existen **infinitos** conjuntos universales distintos.

## Ejemplo: ¿es $\{H, T, \text{controlled-}S\}$ universal?

Sí. La clave es notar que $\text{CS}^2 = \text{CZ}$ (porque $S^2=Z$), así que aplicar controlled-$S$ dos veces da controlled-$Z$. Y $\text{CZ}$ se convierte en CNOT usando Hadamards:

$$\text{CNOT} = (I\otimes H)\,\text{CZ}\,(I\otimes H)$$

Entonces $\{H,T,\text{CS}\}$ puede generar $\{H,T,\text{CNOT}\}$ — el conjunto "Clifford+T" estándar, que ya se sabe universal.

## Lo que NO es cierto

- **No** se necesita ninguna compuerta de 3 qubits (Toffoli, Fredkin) — $\{H,T,\text{CNOT}\}$ usa solo 1 y 2 qubits.
- **No** se necesita CNOT específicamente — cualquier compuerta entrelazante equivalente funciona igual.

Ver `banco-de-problemas/costo-de-circuitos-y-compuertas.md` (Problema 4).
