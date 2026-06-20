# 03 — Algoritmo de Grover

Todo Grover se reduce a una rotación geométrica dentro de un plano de 2 dimensiones, generado por el subespacio "bueno" (estados marcados) y el subespacio "malo" (el resto). Una vez que esa imagen queda clara, todas las fórmulas —número óptimo de iteraciones, probabilidad de éxito, qué pasa si te pasás de iteraciones— salen casi solas.

Punto que casi nadie tiene claro a la primera: el speedup de Grover es **cuadrático**, no exponencial. Por eso, a diferencia de Shor, no se espera que dé una ventaja práctica a corto plazo en hardware real, aunque la ventaja teórica sea perfectamente real y demostrable.

## Contenido

- **`geometria-de-grover.md`** — el ángulo $\theta$ con $\sin(\theta)=\sqrt{M/N}$, y por qué cada iteración rota el estado por $2\theta$.

- **`numero-de-iteraciones.md`** — la fórmula $t \approx \frac{\pi}{4}\sqrt{N/M}$, y el fenómeno de "overshooting": iterar de más no garantiza mejorar la probabilidad, y a veces hasta puede empeorarla (o, en casos especiales, volver a mejorarla por periodicidad).

- **`caso-balanceado.md`** — qué pasa cuando exactamente la mitad del espacio de búsqueda está marcado ($M=N/2$): no hay ninguna ventaja, la probabilidad de éxito se queda fija en 1/2 sin importar cuántas iteraciones corras. Caso degenerado importante de entender.

- **`limitaciones.md`** — qué SÍ promete Grover (ventaja cuadrática demostrable, generalización vía amplitude amplification) y qué NO promete (ventaja práctica a corto plazo, dado el tamaño de $N$ que se necesita para justificar el overhead).

- **`ejercicios/`** — banco de problemas de este tema.
