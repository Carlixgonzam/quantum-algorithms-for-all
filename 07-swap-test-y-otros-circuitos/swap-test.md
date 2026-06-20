# El swap test

## Para qué sirve

Medir qué tan similares son dos estados cuánticos $|\varphi\rangle$ y $|\psi\rangle$ **sin necesidad de conocer sus amplitudes individuales** — solo con la probabilidad de un único bit de medición.

## El circuito

Un qubit de control en superposición, una compuerta **controlled-SWAP** (Fredkin) entre los dos registros a comparar, y Hadamard antes y después del control — exactamente la estructura de un circuito de estimación de fase sobre la operación SWAP.

## Derivación completa

$$|0\rangle|\varphi\rangle|\psi\rangle\xrightarrow{H}\frac{1}{\sqrt2}(|0\rangle+|1\rangle)|\varphi\rangle|\psi\rangle\xrightarrow{\text{c-SWAP}}\frac{1}{\sqrt2}\big[|0\rangle|\varphi\rangle|\psi\rangle+|1\rangle|\psi\rangle|\varphi\rangle\big]$$

$$\xrightarrow{H}\frac12|0\rangle\big(|\varphi\rangle|\psi\rangle+|\psi\rangle|\varphi\rangle\big)+\frac12|1\rangle\big(|\varphi\rangle|\psi\rangle-|\psi\rangle|\varphi\rangle\big)$$

$$P(1)=\frac14\Big\||\varphi\rangle|\psi\rangle-|\psi\rangle|\varphi\rangle\Big\|^2=\frac12\Big(1-|\langle\varphi|\psi\rangle|^2\Big)$$

## Simplificación para un qubit con coeficientes reales

Si $|\varphi\rangle=\alpha|0\rangle+\beta|1\rangle$ y $|\psi\rangle=\gamma|0\rangle+\delta|1\rangle$ (normalizados), usando la identidad $(\alpha\gamma+\beta\delta)^2+(\alpha\delta-\beta\gamma)^2=1$:

$$\boxed{P(1)=\frac12|\alpha\delta-\beta\gamma|^2}$$

## Los dos extremos

- Si $|\varphi\rangle=|\psi\rangle$: $\alpha\delta-\beta\gamma=0$ → $P(1)=0$ con certeza. El test nunca falla en confirmar identidad.
- Si $|\varphi\rangle\perp|\psi\rangle$ (ortogonales, ej. $|0\rangle$ y $|1\rangle$): $\alpha\delta-\beta\gamma=1$ → $P(1)=1/2$, la probabilidad máxima posible de detectar la diferencia en una sola ejecución.

Ver `banco-de-problemas/fundamentos-y-otros-circuitos.md` (Problema 3).
