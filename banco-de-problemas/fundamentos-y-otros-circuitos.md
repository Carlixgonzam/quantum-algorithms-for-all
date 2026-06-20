# Fundamentos y otros circuitos

## Problema 1 — Afirmación falsa sobre matrices unitarias

**Enunciado.** ¿Cuál de estas es falsa?

*"Every eigenvalue of a unitary matrix is a real number in the range $[0,2\pi)$"* → **Falsa.**

Confunde el eigenvalor con su fase. El eigenvalor es $\lambda=e^{i\theta}$, un número **complejo** (salvo en los casos especiales $\theta=0,\pi$). Lo real y en $[0,2\pi)$ es $\theta$, no $\lambda$.

Verdaderas: toda matriz unitaria tiene base ortonormal de eigenvectores (es normal); si todos los eigenvalores son 1, la matriz es la identidad; los eigenvalores viven en el círculo unitario; si los únicos eigenvalores son $\pm1$ (reales), la matriz es necesariamente Hermitiana (normal + eigenvalores reales ⟹ Hermitiana).

---

## Problema 2 — Afirmación falsa sobre el modelo de consultas

**Enunciado.** ¿Cuál es falsa?

*"El costo de construir las compuertas de consulta típicamente se toma en cuenta al analizar la eficiencia de algoritmos cuánticos de consulta"* → **Falsa.**

Es exactamente lo contrario: el modelo de consultas trata al oráculo como caja negra de **costo unitario**, ignorando deliberadamente cómo está construido por dentro. Solo se cuenta el número de consultas.

Verdaderas: el oráculo representa el input del problema; en el entorno cuántico hay que asegurar que las compuertas de consulta sean unitarias (a diferencia del clásico, donde el oráculo puede ser cualquier función); el modelo es útil teóricamente pero no siempre refleja problemas con importancia práctica real.

*Intuición:* esto conecta con el Problema 4 de esta misma sección — la abstracción que hace poderoso al modelo (ignorar el costo de construcción del oráculo) es la misma que limita su aplicabilidad práctica directa.

---

## Problema 3 — Swap test

**Enunciado.** Circuito H–controlled-SWAP–H sobre un qubit de control, con $|\varphi\rangle=\alpha|0\rangle+\beta|1\rangle$ y $|\psi\rangle=\gamma|0\rangle+\delta|1\rangle$ en los otros dos registros. ¿Probabilidad de medir 1?

Tras el circuito completo:

$$\frac12|0\rangle\big(|\varphi\rangle|\psi\rangle+|\psi\rangle|\varphi\rangle\big)+\frac12|1\rangle\big(|\varphi\rangle|\psi\rangle-|\psi\rangle|\varphi\rangle\big)$$

$$P(1)=\frac14\Big\||\varphi\rangle|\psi\rangle-|\psi\rangle|\varphi\rangle\Big\|^2=\frac12\big(1-|\langle\varphi|\psi\rangle|^2\big)$$

Usando la identidad de normalización $(\alpha\gamma+\beta\delta)^2+(\alpha\delta-\beta\gamma)^2=1$ (válida porque ambos estados están normalizados):

$$P(1)=\boxed{\frac12|\alpha\delta-\beta\gamma|^2}$$

*Intuición:* si $|\varphi\rangle=|\psi\rangle$, entonces $\alpha\delta-\beta\gamma=0$ → $P(1)=0$ (nunca falla en confirmar identidad). Si son ortogonales, $P(1)=1/2$ — la probabilidad máxima posible de detectar la diferencia en una sola ejecución.
