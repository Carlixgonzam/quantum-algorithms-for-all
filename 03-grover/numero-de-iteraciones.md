# Número óptimo de iteraciones

## La fórmula

$$t \approx \frac{\pi}{4}\sqrt{\frac{N}{M}}$$

redondeado al entero más cercano, donde $N=2^n$ es el tamaño del espacio de búsqueda y $M$ el número de elementos marcados.

Viene directamente de la geometría (`geometria-de-grover.md`): querés llevar el ángulo $(2k+1)\theta$ lo más cerca posible de $90°$, donde la probabilidad de éxito es máxima.

## Ejemplo trabajado

$N=128$ ($n=7$), $M=19$:

$$t\approx\frac\pi4\sqrt{\frac{128}{19}}\approx\frac\pi4\times2.595\approx2.04\rightarrow\boxed{2}$$

## El fenómeno de "overshooting"

Iterar **de más** no es gratis — el estado sigue rotando más allá del punto óptimo y la probabilidad puede empeorar. Pero si el ángulo $\theta$ divide limpiamente a $90°$, el sistema es periódico y puede volver a tocar probabilidad 1 en iteraciones posteriores.

**Ejemplo:** con $M=2^{n-2}$ (un cuarto del espacio marcado), $\theta=30°$. Tras $k=1$ ($90°$) la probabilidad ya es 1. Tras $k=2,3$ baja a $1/4$ (overshooting). Tras $k=4$ ($270°$) vuelve a ser exactamente 1. Ver `banco-de-problemas/algoritmo-de-grover.md` (Problema 4) para la tabla completa.

## La raíz de por qué Grover es "solo" cuadrático

Esa raíz cuadrada en la fórmula de $t$ es precisamente la fuente del speedup cuadrático de Grover sobre la búsqueda clásica ($O(N)$) — y también la razón por la que, a diferencia de Shor, no se espera ventaja práctica real a corto plazo (ver `limitaciones.md`).
