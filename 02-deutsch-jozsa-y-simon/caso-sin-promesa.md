# Deutsch-Jozsa sin promesa

## La pregunta interesante

¿Qué pasa si corremos el circuito de Deutsch-Jozsa sobre una función que **no** es ni constante ni balanceada? La fórmula general sigue siendo válida:

$$P(0^n)=\left|\frac{1}{2^n}\sum_x(-1)^{f(x)}\right|^2$$

Esto se cumple para **cualquier** $f$, no solo las que cumplen la promesa — la derivación del circuito (Hadamard, oráculo de fase, Hadamard) nunca usó la promesa, solo la usamos después para interpretar el resultado como determinista.

## Ejemplo trabajado

Si $f$ tiene exactamente $2^{n-2}$ entradas con $f(x)=1$ (un cuarto del espacio total, ni constante ni balanceada):

$$\sum_x(-1)^{f(x)} = \big(2^n-2^{n-2}\big)-2^{n-2} = 2^{n-1}$$

$$P(0^n)=\left|\frac{2^{n-1}}{2^n}\right|^2=\left(\frac12\right)^2=\frac14$$

## Cómo interpretar este resultado

Es un punto intermedio perfectamente coherente entre los dos extremos conocidos:

| Tipo de $f$ | $P(0^n)$ |
|---|---|
| Constante | 1 |
| Un cuarto de salidas en 1 | **1/4** |
| Balanceada (mitad y mitad) | 0 |

Fuera de la promesa estricta, el algoritmo deja de ser determinista y se comporta de forma genuinamente probabilística — la probabilidad depende suavemente de cuánto se aleja $f$ del punto de balance exacto.

Ver `banco-de-problemas/deutsch-jozsa-y-simon.md` (Problema 1).
