# La QFT: definición y propiedades

## Definición

$$\text{QFT}_N : |x\rangle \mapsto \frac{1}{\sqrt N}\sum_{y=0}^{N-1}\omega_N^{xy}|y\rangle, \qquad \omega_N=e^{2\pi i/N}$$

## Resultado que vale la pena memorizar: aplicar la QFT dos veces

$$\text{QFT}_N^2:|x\rangle\mapsto\frac1N\sum_z\Big(\sum_y\omega_N^{y(x+z)}\Big)|z\rangle$$

La suma interna es una suma geométrica de raíces de la unidad: vale $N$ cuando $x+z\equiv0\pmod N$ (es decir $z\equiv-x$), y se cancela a $0$ en cualquier otro caso (las raíces de la unidad se cancelan simétricamente).

$$\boxed{\text{QFT}_N^2:|x\rangle\mapsto|-x\bmod N\rangle}$$

## Por qué tiene sentido

Esto es exactamente análogo a lo que pasa con la transformada de Fourier continua clásica: $\mathcal F^2[f](x)=f(-x)$. La QFT es esencialmente su propia inversa salvo por esta reflexión $x\to-x$.

## Consecuencia directa

$$\text{QFT}_N^4 = \mathbb I$$

La QFT tiene **orden 4** como operador unitario — aplicarla cuatro veces siempre devuelve el estado original.

Ver `banco-de-problemas/estimacion-de-fase-y-shor.md` (Problema 1).
