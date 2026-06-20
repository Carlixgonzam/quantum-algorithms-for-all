# 06 — Shor y el problema del orden modular

Todo el poder del algoritmo de Shor se reduce a un solo subproblema: encontrar el **orden** de $a$ módulo $N$ (el menor $r$ tal que $a^r \equiv 1 \pmod N$). La parte cuántica (estimación de fase aplicada a la multiplicación modular) resuelve ese subproblema con ventaja exponencial; la parte clásica que queda (Euclides + Teorema Chino del Resto) es trivial computacionalmente — el algoritmo de Euclides ya era eficiente desde hace más de 2000 años.

## Contenido

- **`orden-modular.md`** — cómo calcular el orden de $a$ módulo $N$ vía el Teorema Chino del Resto: se factoriza $N$ en sus primos, se calcula el orden módulo cada primo por separado, y se combina con el mínimo común múltiplo.

- **`factorizacion-via-orden.md`** — por qué $\gcd(a^{r/2}\pm 1, N)$ revela factores no triviales de $N$, y cuándo el método falla: cuando todos los factores primos de $N$ "votan" el mismo signo en $a^{r/2} \bmod N$ (es decir, cuando no hay discrepancia de signo entre ellos).

- **`costo-y-eficiencia.md`** — la exponenciación modular vía repeated squaring cuesta $O(n^3)$ (no $O(n^2)$: son $O(n)$ multiplicaciones, cada una de costo $O(n^2)$ con el algoritmo estándar). El algoritmo de Euclides para GCD ya es eficiente, $O(n^2)$.

- **`ejercicios/`** — banco de problemas de este tema.
