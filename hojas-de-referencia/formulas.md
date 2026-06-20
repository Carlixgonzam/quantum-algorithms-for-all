# Fórmulas clave

Todo lo que necesito tener a mano antes de un parcial, en un solo lugar.

## Matrices unitarias
- Eigenvalores: $\lambda = e^{i\theta}$, $\theta \in [0,2\pi)$ — el eigenvalor es complejo, el *ángulo* es lo que es real.
- Toda matriz unitaria es normal → diagonalizable con base ortonormal de eigenvectores.

## Modelo de consultas
- El costo se mide en número de consultas al oráculo, **no** en el costo de construir el oráculo.

## Deutsch-Jozsa
- $P(0^n) = \left|\frac{1}{2^n}\sum_x (-1)^{f(x)}\right|^2$ — fórmula general, válida incluso sin promesa.
- Constante → $P(0^n)=1$. Balanceada → $P(0^n)=0$.

## Simon
- Bajo la promesa: medir $y$ tal que $y\cdot s = 0$ con certeza (requiere repetir $\sim n$ veces para resolver el sistema lineal y obtener $s$).

## Grover
- Ángulo de Grover: $\sin\theta = \sqrt{M/N}$
- Probabilidad de éxito tras $k$ iteraciones: $P_k = \sin^2\big((2k+1)\theta\big)$
- Número óptimo de iteraciones: $t \approx \dfrac{\pi}{4}\sqrt{\dfrac{N}{M}}$, redondeado al entero más cercano.
- Operador de difusión: $D = 2|s\rangle\langle s| - I$, donde $|s\rangle$ es la superposición uniforme.

## QFT
- $\text{QFT}_N : |x\rangle \mapsto \frac{1}{\sqrt N}\sum_y \omega_N^{xy}|y\rangle$, con $\omega_N = e^{2\pi i/N}$
- $\text{QFT}_N^2 : |x\rangle \mapsto |-x \bmod N\rangle$
- $\text{QFT}_N^4 = \mathbb{I}$

## Estimación de fase
- Costo: Hadamards $O(m)$, QFT $O(m^2)$, mediciones $O(m)$; costo de $U$ controlada depende del problema.

## Shor / orden modular
- Si $r$ es par y $a^{r/2}\not\equiv -1 \pmod N$: $\gcd(a^{r/2}-1, N)$ y $\gcd(a^{r/2}+1, N)$ dan factores no triviales de $N$.
- Orden módulo $N = p_1 p_2 \cdots p_k$: $\text{orden}(a, N) = \text{lcm}\big(\text{orden}(a,p_1), \ldots, \text{orden}(a,p_k)\big)$.
- Exponenciación modular (repeated squaring): $O(n^3)$.
- Algoritmo de Euclides (GCD): $O(n^2)$, eficiente desde siempre.

## Swap test
$$P(\text{medir } 1) = \frac{1}{2}\Big(1-|\langle\varphi|\psi\rangle|^2\Big)$$
Para estados reales de un qubit: $P(1) = \frac{1}{2}|\alpha\delta - \beta\gamma|^2$.

## Costo de simulación de circuitos booleanos
- 1 qubit de trabajo por puerta AND/OR/FANOUT → tamaño del circuito cuántico **lineal** en el tamaño del circuito booleano.
