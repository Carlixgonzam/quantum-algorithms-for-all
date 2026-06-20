# Geometría de Grover

## La imagen que lo explica todo

Grover's algorithm se reduce a una **rotación dentro de un plano de 2 dimensiones**, generado por:

- el subespacio "bueno": superposición uniforme de los $M$ estados marcados
- el subespacio "malo": superposición uniforme de los $N-M$ estados restantes

El estado inicial (superposición uniforme de los $N=2^n$ estados) está a un ángulo $\theta$ del eje "malo", donde:

$$\sin\theta=\sqrt{\frac{M}{N}}$$

## Qué hace cada iteración

Cada iteración de Grover aplica dos reflexiones consecutivas (el oráculo de fase + el operador de difusión), y la composición de dos reflexiones es una **rotación**. El ángulo de rotación por iteración es $2\theta$.

Tras $k$ iteraciones, el estado está a un ángulo $(2k+1)\theta$ del eje "malo", y la probabilidad de medir un estado marcado es:

$$P_k=\sin^2\big((2k+1)\theta\big)$$

## El operador de difusión, explícitamente

$$D = 2|s\rangle\langle s| - I$$

donde $|s\rangle$ es la superposición uniforme sobre **todo** el espacio. Geométricamente, $D$ es una **reflexión respecto a $|s\rangle$**.

**Ejemplo trabajado:** si $|A_0\rangle$ y $|A_1\rangle$ son las superposiciones uniformes sobre los estados con $f(x)=0$ y $f(x)=1$ respectivamente, y $|A_0|=|A_1|$ (caso balanceado), entonces $|s\rangle$ está exactamente a 45° entre ambos, y reflejar sobre esa bisectriz intercambia los dos vectores: $D|A_0\rangle=|A_1\rangle$, $D|A_1\rangle=|A_0\rangle$. Ver `banco-de-problemas/algoritmo-de-grover.md` (Problema 2).

## Por qué esto importa

Una vez que tenés esta imagen geométrica clara, el número óptimo de iteraciones (`numero-de-iteraciones.md`) y el caso degenerado balanceado (`caso-balanceado.md`) son consecuencias directas — no hay que memorizarlos por separado.
