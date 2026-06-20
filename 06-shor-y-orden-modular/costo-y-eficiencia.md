# Costo y eficiencia en el contexto de Shor

## La exponenciación modular (algoritmo "power") es cúbica, no cuadrática

Repeated squaring para calcular $a^b\bmod m$ (con $b$ de $n$ bits) necesita $O(n)$ multiplicaciones modulares. Cada multiplicación modular de números de $n$ bits cuesta $O(n^2)$ con el algoritmo estándar.

$$\text{Costo total} = O(n)\times O(n^2) = O(n^3)$$

Este es un error muy común: asumir que el costo es $O(n^2)$ porque "una multiplicación es cuadrática" — pero hay que multiplicar el número de multiplicaciones por el costo de cada una.

## El algoritmo de Euclides (GCD) ya era eficiente

El cálculo final de $\gcd(a^{r/2}\pm1, N)$ en Shor es **trivial computacionalmente**: el algoritmo de Euclides resuelve GCD en tiempo $O(n^2)$, y se conoce desde hace más de 2000 años. No hay ningún misterio ni dificultad ahí.

## Por qué esto importa para entender dónde está la dificultad real de Shor

Toda la dificultad de factorizar $N$ recae en **encontrar el orden $r$**, no en el paso final del GCD. Una vez que $r$ es conocido (gracias a la parte cuántica del algoritmo), todo lo que queda —exponenciación modular y GCD— es clásico y eficiente, aunque exponenciación modular sea cúbica y no cuadrática.

## Otras afirmaciones útiles sobre costo computacional

- La suma de enteros en binario es $O(n)$ — lineal.
- Identificar un algoritmo de costo polinomial **no es el paso final** en términos de eficiencia: el grado del polinomio y las constantes siguen importando muchísimo en la práctica.
- Formalmente, el análisis de costo asume un esquema de codificación fijo para las entradas — pero en la práctica no importa cuál, porque los esquemas razonables son polinomialmente equivalentes entre sí.

Ver `banco-de-problemas/costo-de-circuitos-y-compuertas.md` (Problema 3).
