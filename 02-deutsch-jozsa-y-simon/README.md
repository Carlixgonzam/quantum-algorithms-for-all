# 02 — Deutsch-Jozsa y Simon

Los dos algoritmos "fundacionales": los primeros ejemplos históricos donde una computadora cuántica resuelve algo con una ventaja demostrable sobre cualquier algoritmo clásico determinista — eso sí, bajo una promesa muy específica sobre la función que se está evaluando.

La parte más interesante (y la que más se pregunta en examen) es qué pasa cuando **se rompe esa promesa**. Ni Deutsch-Jozsa ni Simon "fallan" de forma dramática cuando la función no cumple la promesa — simplemente dejan de ser deterministas y se vuelven genuinamente probabilísticos, con la probabilidad de éxito dependiendo suavemente de cuánto se aleja la función del caso prometido.

## Contenido

- **`deutsch-original.md`** — la versión de 1985, *sin* phase kickback (el segundo qubit se inicializa en $|0\rangle$, no en $|-\rangle$). Distinción importante: esta versión solo logra distinguir constante de balanceado con probabilidad 1 vs. 1/2 — no 1 vs. 0.

- **`deutsch-jozsa-moderno.md`** — la versión con phase kickback (mejora de Cleve-Ekert-Macchiavello-Mosca) que sí logra una distinción perfectamente determinista.

- **`caso-sin-promesa.md`** — qué probabilidad de medir $0^n$ se obtiene cuando $f$ no es ni constante ni balanceada, usando la fórmula general $P(0^n) = \left|\frac{1}{2^n}\sum_x (-1)^{f(x)}\right|^2$.

- **`simon.md`** — incluye el caso de un oráculo que *no* es genuinamente 2-a-1 (no cumple la promesa de Simon), y por qué ahí la probabilidad de obtener el "string secreto" $s$ ya no es cero ni uno, sino un valor intermedio que se puede calcular exactamente.

- **`ejercicios/`** — banco de problemas de este tema.
