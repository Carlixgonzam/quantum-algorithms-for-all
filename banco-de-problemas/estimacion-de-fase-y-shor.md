# Estimación de fase y Shor

## Problema 1 — QFT aplicada dos veces

**Enunciado.** ¿Qué representa $\text{QFT}_N^2$?

$$\text{QFT}_N^2:|x\rangle\mapsto\frac1N\sum_z\Big(\sum_y\omega_N^{y(x+z)}\Big)|z\rangle$$

La suma interna vale $N$ solo cuando $x+z\equiv0\pmod N$, es decir $z\equiv-x$, y $0$ en cualquier otro caso.

**Respuesta:** $\text{QFT}_N^2:|x\rangle\mapsto|-x\rangle$.

*Intuición:* análogo directo a $\mathcal F^2[f](x)=f(-x)$ en la transformada de Fourier continua clásica. Implica $\text{QFT}_N^4=\mathbb I$.

---

## Problema 2 — Identificar una compuerta misteriosa con estimación de fase

**Enunciado.** $U$ es $\mathbb I$ o $H$, no se sabe cuál. Circuito de un qubit de control (H–CU–H–medición). ¿Qué estado $|\psi\rangle$ hace que la medición sea 0 si $U=\mathbb I$ y 1 si $U=H$, ambos con probabilidad 1?

Si $|\psi\rangle$ es eigenvector de $U$ con eigenvalor $\lambda$, el control queda en $\frac12\big[(1+\lambda)|0\rangle+(1-\lambda)|1\rangle\big]$.

- Para $U=\mathbb I$: cualquier estado es eigenvector con $\lambda=1$ → da 0 siempre, automático.
- Para $U=H$, necesito medición = 1 con certeza → $\lambda=-1$.

Los eigenvectores de $H$ están en los ángulos $\pi/8$ (eigenvalor $+1$) y $5\pi/8$ (eigenvalor $-1$) de la esfera de Bloch.

**Respuesta:** $|\psi\rangle=\cos(5\pi/8)|0\rangle+\sin(5\pi/8)|1\rangle$.

*Intuición:* la estimación de fase nunca "mide" $U$ directamente — mide la fase relativa que $U$ imprime sobre un eigenvector específico. Si $|\psi\rangle$ no fuera eigenvector compartido de ambas opciones, el resultado no sería determinista.

---

## Problema 3 — Costo de la estimación de fase

**Enunciado.** Con $m$ qubits de control y $U$ unitaria de $n$ qubits, ¿cómo se distribuye el costo entre las 4 partes del circuito?

- Hadamards: $O(m)$
- Mediciones: $O(m)$
- QFT (sobre $m$ qubits): $O(m^2)$
- **Operaciones $U$ controladas: el costo varía según $U$** — no hay cota fija en términos de $n$ sin saber más sobre la estructura específica de $U$.

*Intuición:* las partes "genéricas" tienen costo fijo en función de $m$ (que elegimos libremente según la precisión deseada). El costo real de resolver el problema concreto recae enteramente en implementar $U$ controlada — la estimación de fase como marco no resuelve eso, lo hereda.

---

## Problema 4 — Factorizar usando el orden

**Enunciado.** $N=12155$, $a=3$, $r=240$ (orden de 3 mod $N$, correcto y par). ¿Qué factores se descubren?

$N=5\times11\times13\times17$. Calculando $3^{120}\bmod p$ para cada primo (vía orden de 3 mod cada uno): $\equiv1$ mod 5, 11, 13; $\equiv-1$ mod 17. Por CRT: $3^{120}\equiv10726\pmod{12155}$.

$$\gcd(3^{120}-1,N)=\gcd(10725,12155)=5\times11\times13=715$$
$$\gcd(3^{120}+1,N)=\gcd(10727,12155)=17$$

**Respuesta: 715 y 17** (verificación: $715\times17=12155$ ✓).

*Intuición:* el método funciona porque hay una **discrepancia de signo** entre los factores primos de $N$ al evaluar $a^{r/2}\bmod p_i$. Si todos hubieran dado el mismo signo, el gcd habría fallado en separar $N$ pese a que $r$ era correcto.

---

## Problema 5 — Calcular el orden de 13 módulo 231

**Enunciado.** ¿Orden de 13 mod 231?

$231=3\times7\times11$. Orden de 13 mod cada primo: mod 3 → 1; mod 7 → 2 ($13\equiv-1$); mod 11 → 10 (13≡2, que resulta ser raíz primitiva mod 11).

$$\text{orden}(13,231)=\text{lcm}(1,2,10)=\boxed{10}$$

*Intuición:* el factor que domina es mod 11, donde 2 es raíz primitiva (orden máximo posible, $10=11-1$) — eso "arrastra" el orden combinado, ya que el lcm con órdenes más chicos no lo reduce.
