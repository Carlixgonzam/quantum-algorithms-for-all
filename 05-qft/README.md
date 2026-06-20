# 05 — Transformada cuántica de Fourier (QFT)

La pieza que convierte información de fase en información de amplitud (y viceversa) — el ingrediente algebraico que hace posible la estimación de fase y, por extensión, Shor.

## Contenido

- **`definicion-y-propiedades.md`** — definición formal $\text{QFT}_N : |x\rangle \mapsto \frac{1}{\sqrt N}\sum_y \omega_N^{xy}|y\rangle$, y un resultado que vale la pena memorizar porque aparece seguido en examen: aplicar la QFT **dos veces** da $\text{QFT}_N^2 : |x\rangle \mapsto |-x \bmod N\rangle$. Esto implica directamente que $\text{QFT}_N^4 = \mathbb{I}$ — la QFT tiene orden 4 como operador unitario, análogo a lo que pasa con la transformada de Fourier continua clásica.
