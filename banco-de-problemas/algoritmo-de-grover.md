# Algoritmo de Grover

## Problema 1 — Grover sobre una función balanceada

**Enunciado.** $f$ balanceada ($|A_1|=2^{n-1}$). ¿Qué pasa al correr Grover y medir?

Ángulo de Grover: $\sin\theta=\sqrt{1/2} \Rightarrow \theta=\pi/4$. Probabilidad tras $k$ iteraciones: $P_k=\sin^2\big((2k+1)\pi/4\big)$. Como $(2k+1)\pi/4$ siempre es un múltiplo impar de $45°$, y $\sin^2$ de cualquier múltiplo impar de $45°$ vale $1/2$:

**Respuesta:** la probabilidad de medir $f(x)=1$ es **$1/2$ sin importar cuántas iteraciones se corran.**

*Intuición:* este es el caso degenerado de Grover — cuando exactamente la mitad del espacio está marcado, el algoritmo no da ninguna ventaja sobre simplemente medir la superposición uniforme inicial.

---

## Problema 2 — El operador de difusión de Grover

**Enunciado.** ¿Qué hace $H^{\otimes n}Z_{\text{OR}}H^{\otimes n}$ sobre $|A_0\rangle$ y $|A_1\rangle$ (superposiciones uniformes sobre $f^{-1}(0)$ y $f^{-1}(1)$, con $f$ balanceada)?

$Z_{\text{OR}} = 2|0^n\rangle\langle 0^n|-I$, así que $H^{\otimes n}Z_{\text{OR}}H^{\otimes n} = 2|s\rangle\langle s|-I = D$ (el operador de difusión). Como $|A_0|=|A_1|$, el estado uniforme $|s\rangle = \frac{1}{\sqrt2}|A_0\rangle+\frac{1}{\sqrt2}|A_1\rangle$ está exactamente a 45° entre ambos.

**Respuesta:** $D|A_0\rangle=|A_1\rangle$ y $D|A_1\rangle=|A_0\rangle$.

*Intuición:* $D$ es una reflexión respecto a $|s\rangle$ — y reflejar sobre la bisectriz exacta de dos vectores ortogonales intercambia ambos ejes.

---

## Problema 3 — Número de iteraciones sugerido

**Enunciado.** $N=2^7=128$, $M=19$ elementos marcados. ¿Iteraciones óptimas?

$$t \approx \frac{\pi}{4}\sqrt{\frac{128}{19}} \approx \frac{\pi}{4}\times 2.595 \approx 2.04 \rightarrow \boxed{2}$$

*Intuición:* la raíz cuadrada en la fórmula es precisamente la fuente del speedup cuadrático de Grover sobre la búsqueda clásica.

---

## Problema 4 — Cuatro iteraciones sobre $M=2^{n-2}$

**Enunciado.** $M=2^{n-2}$ (un cuarto del espacio marcado). Tras **4** iteraciones, ¿probabilidad de éxito?

$\sin\theta=\sqrt{1/4}=1/2 \Rightarrow \theta=30°$. Tras $k=4$: ángulo $=(2\cdot4+1)\times30°=270°$, $\sin^2(270°)=1$.

**Respuesta: probabilidad = 1** (éxito garantizado).

*Intuición:* como $\theta=30°$ divide limpiamente a $90°$, el algoritmo alcanza probabilidad 1 ya en $k=1$ (a $90°$), se "pasa" de largo (overshooting) bajando la probabilidad en $k=2,3$, y vuelve a tocar probabilidad 1 en $k=4$ (a $270°$) por periodicidad — buen ejemplo de que más iteraciones no siempre es monótonamente mejor, pero en casos especiales puede volver a serlo.

---

## Problema 5 — Afirmación falsa sobre Grover

**Enunciado.** ¿Cuál de estas es falsa?

*"Grover's algorithm is widely expected to provide a near-term practical advantage of quantum computing over classical computing."* → **Falsa.**

El speedup de Grover es cuadrático — necesita un $N$ astronómico para justificar el overhead de corrección de errores y decoherencia actual. Es de gran interés teórico, no se espera ventaja práctica en el horizonte cercano (a diferencia de Shor, que sí tiene speedup exponencial y es el candidato más citado para impacto real).

Las demás afirmaciones (Grover no se limita al modelo de consultas; la amplitude amplification se generaliza ampliamente; cada iteración rota en un subespacio 2D; usa $O(2^{n/2})$ iteraciones) son verdaderas.
