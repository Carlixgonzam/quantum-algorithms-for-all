# El algoritmo original de Deutsch (1985)

## La diferencia clave con la versión moderna

La versión de 1985 de Deutsch **no usa phase kickback**. El segundo qubit se inicializa en $|0\rangle$ (no en $|-\rangle$), y el oráculo actúa de forma estándar: $U_f|x\rangle|y\rangle = |x\rangle|y\oplus f(x)\rangle$.

## Derivación

$$|0\rangle|0\rangle \xrightarrow{H} \frac{1}{\sqrt2}(|0\rangle+|1\rangle)|0\rangle \xrightarrow{U_f} \frac{1}{\sqrt2}\big(|0\rangle|f(0)\rangle+|1\rangle|f(1)\rangle\big)$$

Aplicando $H$ otra vez al primer qubit:

$$\frac12|0\rangle\big(|f(0)\rangle+|f(1)\rangle\big) + \frac12|1\rangle\big(|f(0)\rangle-|f(1)\rangle\big)$$

## Los dos casos

**Constante** ($f(0)=f(1)$): $|f(0)\rangle+|f(1)\rangle=2|f(0)\rangle$, y el término con $|1\rangle$ se cancela exactamente. El estado queda $|0\rangle|f(0)\rangle$.

$$\Pr(\text{medir }0)=1$$

**Balanceada** ($f(0)\neq f(1)$): $|f(0)\rangle$ y $|f(1)\rangle$ son ortogonales, así que ambos términos del segundo registro contribuyen igual.

$$\Pr(\text{medir }0)=\left|\frac12\right|^2+\left|\frac12\right|^2=\frac12$$

## Por qué esto es más débil que Deutsch-Jozsa moderno

Esta versión solo logra una distinción **probabilística parcial**: 100% vs. 50%, no 100% vs. 0%. La mejora de Cleve, Ekert, Macchiavello y Mosca (usar $|-\rangle$ en vez de $|0\rangle$ para activar phase kickback) es lo que convierte este resultado parcial en una separación cuántico-clásica absoluta y perfectamente determinista — ver `deutsch-jozsa-moderno.md`.

Ver `banco-de-problemas/deutsch-jozsa-y-simon.md` (Problema 2).
