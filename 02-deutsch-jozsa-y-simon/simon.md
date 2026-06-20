# Algoritmo de Simon

## El problema y la promesa

Dado $f:\Sigma^n\to\Sigma^n$ tal que $f(x)=f(x')$ si y solo si $x'=x$ o $x'=x\oplus s$ para algún $s$ fijo (función "2-a-1" con período oculto $s$), encontrar $s$.

## Por qué la promesa importa tanto

Bajo la promesa, cada valor de salida tiene **exactamente 2** preimágenes: $x_0$ y $x_0\oplus s$. Al medir el segundo registro, el primer registro colapsa a $\frac{1}{\sqrt2}(|x_0\rangle+|x_0\oplus s\rangle)$, y al aplicar $H^{\otimes n}$, la interferencia concentra **toda** la probabilidad sobre el subespacio ortogonal a $s$ (es decir, se mide $y$ con $y\cdot s=0$, siempre). Repitiendo el proceso $\sim n$ veces se junta un sistema de ecuaciones lineales suficiente para resolver $s$.

## Qué pasa si se rompe la promesa

Ver el ejemplo completo en `banco-de-problemas/deutsch-jozsa-y-simon.md` (Problema 3): si $f$ tiene preimágenes de tamaño $2^{n-1}$ en vez de 2 (por ejemplo, $f(x)=0^n$ si $x\cdot s=0$ y $f(x)=s$ si $x\cdot s=1$), la interferencia ya no concentra la probabilidad de forma tan limpia. En ese caso particular:

$$P(\text{medir }y=s)=\frac12$$

— un resultado nada despreciable, muy distinto de lo que pasaría con un oráculo genuinamente 2-a-1, donde medir exactamente $y=s$ sería prácticamente imposible salvo coincidencia algebraica.

## La lección de fondo

El tamaño de las preimágenes del oráculo cambia completamente qué tan "limpio" es el patrón de interferencia resultante. Cuanto más estructurado el oráculo (preimágenes pequeñas y bien definidas), más determinista es el resultado final.
