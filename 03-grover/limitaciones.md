# Qué SÍ y qué NO promete Grover

## Lo que sí es cierto

- **Speedup cuadrático demostrable:** $O(\sqrt N)$ consultas vs. $O(N)$ en el mejor algoritmo clásico para búsqueda no estructurada. Esto es un resultado riguroso de teoría de la complejidad de consultas, no una expectativa — está probado.
- **No está limitado al modelo de consultas puro:** se puede correr sobre cualquier función para la que exista un circuito booleano conocido (ver `01-costo-de-circuitos-y-compuertas/simulacion-de-circuitos-booleanos.md`).
- **La técnica subyacente (amplitude amplification) es ampliamente generalizable** — se reutiliza en muchos otros algoritmos cuánticos más allá de la búsqueda no estructurada (estimación de cuentas, optimización, etc.).
- **Cada iteración rota el estado en un subespacio de 2 dimensiones** — ver `geometria-de-grover.md`. Esto es literal, no una metáfora.
- **El número de iteraciones es $O(2^{n/2})$** para un espacio de $N=2^n$ elementos — el speedup cuadrático explícito.

## Lo que NO es realista esperar

**Que Grover dé una ventaja práctica a corto plazo sobre la computación clásica.** Esta es la trampa más común en preguntas tipo examen sobre este tema.

La razón: una mejora *cuadrática* necesita un $N$ astronómicamente grande para que la ventaja supere el overhead de corrección de errores, decoherencia, y tasas de error de las compuertas en el hardware actual (era NISQ). En contraste con algoritmos de speedup *exponencial* (como Shor, o simulación de sistemas cuánticos), Grover es de gran interés **teórico**, pero no es el candidato típico para impacto práctico cercano.

## Por qué vale la pena tener esta distinción clara

Confundir "existe una ventaja cuántica demostrable" (verdadero, en el sentido de complejidad de consultas) con "esa ventaja es explotable en hardware real pronto" (falso, para Grover específicamente) es exactamente el tipo de matiz que se pregunta en examen.

Ver `banco-de-problemas/algoritmo-de-grover.md` (Problema 5).
