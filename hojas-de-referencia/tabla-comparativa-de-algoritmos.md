# Tabla comparativa: Deutsch-Jozsa, Simon, Grover, Shor

La pregunta que más vale la pena tener clara antes de un examen: **¿qué promete exactamente cada algoritmo, bajo qué promesa sobre la función, y qué pasa si esa promesa se rompe?**

| | Deutsch-Jozsa | Simon | Grover | Shor |
|---|---|---|---|---|
| **Problema que resuelve** | Determinar si $f$ es constante o balanceada | Encontrar el período oculto $s$ de una función 2-a-1 | Encontrar un elemento marcado en un espacio no estructurado | Factorizar $N$ vía orden modular |
| **Promesa requerida** | $f$ es constante o balanceada (no hay término medio) | $f(x)=f(x')$ si y solo si $x'=x$ o $x'=x\oplus s$ | Ninguna especial — pero el número de elementos marcados $M$ se asume conocido (o se estima) | $\gcd(a,N)=1$ |
| **Tipo de ventaja** | Determinista con 1 consulta (vs. exponencial clásico) | Exponencial (vs. exponencial clásico determinista) | **Cuadrática**: $O(\sqrt N)$ vs. $O(N)$ | **Exponencial** (vs. el mejor algoritmo clásico conocido) |
| **¿Es realista esperar ventaja práctica a corto plazo?** | No es el objetivo — es un resultado de prueba de concepto | No es el objetivo — el mismo rol que Deutsch-Jozsa pero más general | **No** (ampliamente esperado que no, por el tamaño de $N$ necesario para justificar el overhead) | Sí es el candidato más citado para ventaja práctica real, una vez existan computadoras cuánticas suficientemente grandes y tolerantes a fallos |
| **¿Qué pasa si se rompe la promesa?** | Deja de ser determinista — probabilidad de éxito $\in (0,1)$, calculable exactamente con $\left\|\frac{1}{2^n}\sum_x(-1)^{f(x)}\right\|^2$ | Deja de ser determinista — puede dar resultados que no corresponden a ningún período real | No aplica una "promesa" en el mismo sentido — pero si $M=N/2$ (balanceado), no hay ventaja: probabilidad de éxito fija en 1/2 sin importar las iteraciones | Si $r$ es impar, o si todos los factores primos "votan" el mismo signo en $a^{r/2}\bmod N$, el método de gcd falla en encontrar factores no triviales en esa ronda — hay que repetir con otro $a$ |
| **Bloque cuántico central** | Phase kickback + interferencia (Hadamard-oráculo-Hadamard) | Phase kickback generalizado a $n$ qubits | Amplitude amplification (rotación geométrica en plano 2D) | Estimación de fase aplicada a multiplicación modular |

## La idea que conecta todo

Los cuatro algoritmos son, en el fondo, la misma receta aplicada a problemas distintos: **usar interferencia cuántica para amplificar la probabilidad de la respuesta correcta y cancelar la de las incorrectas**. Lo que cambia entre ellos es qué tan estructurado está el problema (Deutsch-Jozsa y Simon necesitan estructura muy específica; Grover funciona en espacios completamente no estructurados) y por eso qué tan grande es la ventaja que se puede extraer (cuadrática para problemas no estructurados, exponencial cuando hay estructura algebraica que explotar, como en Simon y Shor).
