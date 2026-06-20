# Factorización vía el orden

## El método

Si ya se conoce $r$ = orden de $a$ módulo $N$, y $r$ es **par**, los dos factores no triviales de $N$ aparecen como:

$$\gcd(a^{r/2}-1, N) \quad\text{y}\quad \gcd(a^{r/2}+1, N)$$

(siempre que $a^{r/2}\not\equiv-1\pmod N$ — si fuera así, el método falla en esa ronda y hay que repetir con otro $a$).

## Ejemplo trabajado: $N=12155$, $a=3$, $r=240$

$N=5\times11\times13\times17$. Calculando $3^{120}\bmod p$ vía el orden de 3 en cada factor primo:

| Primo $p$ | $3^{120}\bmod p$ |
|---|---|
| 5 | 1 |
| 11 | 1 |
| 13 | 1 |
| 17 | $-1$ (16) |

Por CRT: $3^{120}\equiv10726\pmod{12155}$.

$$\gcd(3^{120}-1,N)=\gcd(10725,12155)=5\times11\times13=715$$
$$\gcd(3^{120}+1,N)=\gcd(10727,12155)=17$$

**Factores encontrados: 715 y 17** (verificación: $715\times17=12155$ ✓).

## Por qué funciona (y cuándo falla)

El método funciona porque hay una **discrepancia de signo** entre los factores primos de $N$ al evaluar $a^{r/2}\bmod p_i$: algunos primos dan $+1$, otros dan $-1$. Esa discrepancia es justo lo que permite que el $\gcd$ "separe" a $N$ en piezas no triviales.

**Si todos los primos hubieran dado el mismo signo** (todos $+1$ o todos $-1$), el método habría fallado en esa ronda — pese a que $r$ fuera perfectamente correcto. En ese caso, simplemente se elige otro $a$ al azar y se repite.

Ver `banco-de-problemas/estimacion-de-fase-y-shor.md` (Problema 4).
