# El problema del orden modular

## Definición

El orden de $a$ módulo $N$ (con $\gcd(a,N)=1$) es el menor entero positivo $r$ tal que:

$$a^r\equiv1\pmod N$$

## Cómo calcularlo a mano vía el Teorema Chino del Resto

1. Factorizar $N=p_1\times p_2\times\cdots\times p_k$ en sus primos.
2. Calcular el orden de $a$ módulo cada $p_i$ por separado (esto es mucho más manejable que trabajar directamente con $N$).
3. Combinar con el **mínimo común múltiplo**:

$$\text{orden}(a,N) = \text{lcm}\big(\text{orden}(a,p_1),\ldots,\text{orden}(a,p_k)\big)$$

## Ejemplo trabajado: orden de 13 módulo 231

$231=3\times7\times11$.

| Primo $p$ | $13\bmod p$ | Orden de 13 mod $p$ |
|---|---|---|
| 3 | 1 | 1 |
| 7 | 6 ($\equiv-1$) | 2 |
| 11 | 2 | 10 |

$$\text{orden}(13,231)=\text{lcm}(1,2,10)=\boxed{10}$$

El factor que domina es el módulo 11, donde $2$ resulta ser **raíz primitiva** (orden máximo posible, $10=11-1$) — eso "arrastra" el orden combinado, ya que el lcm con órdenes más chicos no lo reduce.

## Por qué este subproblema es el corazón de Shor

Toda la dificultad de factorizar $N$ vía el algoritmo de Shor se reduce exactamente a este problema: encontrar el orden de un $a$ elegido al azar módulo $N$. La parte cuántica (estimación de fase aplicada a multiplicación modular) resuelve esto con ventaja exponencial sobre cualquier método clásico conocido — ver `factorizacion-via-orden.md` para cómo se usa $r$ una vez encontrado.

Ver `banco-de-problemas/estimacion-de-fase-y-shor.md` (Problema 5).
