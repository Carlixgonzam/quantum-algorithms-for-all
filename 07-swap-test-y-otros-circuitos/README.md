# 07 — Swap test y otros circuitos de interés

El swap test es la herramienta estándar para medir qué tan similares son dos estados cuánticos sin necesidad de conocer sus amplitudes individuales — solo con la probabilidad de un único bit de medición.

## Contenido

- **`swap-test.md`** — derivación completa usando una compuerta Fredkin (controlled-SWAP) entre un qubit de control en superposición y dos registros a comparar. Resultado final:
$$P(\text{medir } 1) = \frac{1}{2}\Big(1-|\langle\varphi|\psi\rangle|^2\Big) = \frac{1}{2}|\alpha\delta-\beta\gamma|^2$$
Si los estados son idénticos, $P(1)=0$ con certeza. Si son ortogonales, $P(1)=1/2$ — la probabilidad máxima posible de detectar la diferencia en una sola ejecución.
