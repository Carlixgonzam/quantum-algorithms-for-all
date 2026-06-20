# Deutsch-Jozsa y Simon

## Problema 1 — Deutsch-Jozsa sobre una función sin promesa

**Enunciado.** $f:\Sigma^n\to\Sigma$ con $|\{x:f(x)=1\}|=2^{n-2}$ (un cuarto de las entradas). ¿Probabilidad de medir $0^n$?

$$P(0^n)=\left|\frac{1}{2^n}\sum_x(-1)^{f(x)}\right|^2$$

Conteo de signos: $(2^n-2^{n-2})-2^{n-2}=2^{n-1}$. Entonces:

$$P(0^n)=\left|\frac{2^{n-1}}{2^n}\right|^2=\left(\frac12\right)^2=\boxed{\frac14}$$

*Intuición:* constante da $P=1$, balanceada da $P=0$ — este caso "un cuarto" cae exactamente en un punto intermedio, mostrando que fuera de la promesa estricta el algoritmo se vuelve genuinamente probabilístico.

---

## Problema 2 — El algoritmo original de Deutsch (sin phase kickback)

**Enunciado.** Circuito con el segundo qubit inicializado en $|0\rangle$ (no en $|-\rangle$). ¿Probabilidades de medir 0 si $f$ es constante vs. balanceada?

Tras H – $U_f$ – H sobre el primer qubit, el estado final es:

$$\frac12|0\rangle\big(|f(0)\rangle+|f(1)\rangle\big)+\frac12|1\rangle\big(|f(0)\rangle-|f(1)\rangle\big)$$

- **Constante** ($f(0)=f(1)$): el término con $|1\rangle$ se cancela → $P(\text{medir }0)=1$.
- **Balanceada** ($f(0)\neq f(1)$): los dos términos del segundo registro son ortogonales → $P(\text{medir }0)=\frac14+\frac14=\boxed{\frac12}$.

*Intuición:* esta versión (1985) es más débil que la moderna — distingue 100% vs. 50%, no 100% vs. 0%. La mejora de Cleve-Ekert-Macchiavello-Mosca (usar $|-\rangle$ para activar phase kickback) es lo que la convierte en una separación perfectamente determinista.

---

## Problema 3 — Algoritmo de Simon sobre una función sin promesa

**Enunciado.** $f(x)=0^n$ si $x\cdot s=0$, $f(x)=s$ si $x\cdot s=1$ (no es genuinamente 2-a-1, viola la promesa de Simon). ¿Probabilidad de que el circuito mida exactamente $y=s$?

Tras $U_f$, el estado se separa en dos ramas (según el registro 2 mida $0^n$ o $s$), cada una con probabilidad $1/2$, colapsando el registro 1 a la superposición uniforme sobre $A_0=\{x:x\cdot s=0\}$ o $A_1=\{x:x\cdot s=1\}$ respectivamente.

Aplicando $H^{\otimes n}$ a cada rama:
- Rama $A_0$: $H^{\otimes n}|\varphi_0\rangle=\frac{1}{\sqrt2}|0\rangle+\frac{1}{\sqrt2}|s\rangle$
- Rama $A_1$: $H^{\otimes n}|\varphi_1\rangle=\frac{1}{\sqrt2}|0\rangle-\frac{1}{\sqrt2}|s\rangle$

Probabilidad total de medir $y=s$ (sumando ambas ramas, cada una con peso $1/2$):

$$P(y=s)=\frac12\cdot\frac12+\frac12\cdot\frac12=\boxed{\frac12}$$

*Intuición:* contraste fuerte con Simon "real" (2-a-1 genuino), donde cada salida tiene solo 2 preimágenes y la interferencia concentra la probabilidad casi exclusivamente en el subespacio ortogonal a $s$ — acá, con preimágenes enormes ($2^{n-1}$ elementos cada una), el patrón de interferencia colapsa de forma mucho más concentrada, dando una probabilidad nada despreciable de obtener justo $y=s$.
