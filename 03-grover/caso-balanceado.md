# El caso balanceado: cuando Grover no da ninguna ventaja

## Configuración

Función balanceada: $M=N/2$. Entonces $\sin\theta=\sqrt{1/2}\Rightarrow\theta=45°$.

## El resultado, paso a paso

Probabilidad tras $k$ iteraciones:

$$P_k=\sin^2\big((2k+1)\times45°\big)$$

Como $(2k+1)\times45°$ siempre es un **múltiplo impar de $45°$** (es decir, $45°, 135°, 225°, 315°,\ldots$), y $\sin^2$ de cualquier múltiplo impar de $45°$ vale exactamente $\frac12$ (porque todos esos ángulos tienen $|\sin|=\frac{\sqrt2}{2}$):

$$P_k=\frac12 \quad\text{para todo } k$$

## Por qué pasa esto

$\theta=45°$ es exactamente el caso degenerado donde el sistema queda "atrapado" oscilando entre dos configuraciones que tienen siempre la misma probabilidad — nunca converge hacia probabilidad 1, a diferencia de lo que pasa cuando $M\ll N$.

## La lección práctica

La superposición uniforme inicial (sin aplicar ninguna iteración de Grover) **ya** da probabilidad $\frac12$ de medir un elemento marcado, simplemente porque la mitad del espacio está marcado. Aplicar Grover acá no mejora nada — cada iteración solo "rebota" el estado entre dos configuraciones igualmente buenas (o igualmente malas).

**Moraleja:** Grover solo da ventaja real cuando $M\ll N$ (pocos elementos marcados). Cuando la fracción marcada es grande, la ventaja se diluye, y en el caso balanceado se anula por completo.

Ver `banco-de-problemas/algoritmo-de-grover.md` (Problema 1).
