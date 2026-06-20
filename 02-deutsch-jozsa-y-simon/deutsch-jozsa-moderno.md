# Deutsch-Jozsa moderno (con phase kickback)

## La mejora respecto a 1985

La versión moderna (Cleve, Ekert, Macchiavello, Mosca) inicializa el segundo qubit en $|-\rangle=\frac{1}{\sqrt2}(|0\rangle-|1\rangle)$ en vez de $|0\rangle$. Esto activa **phase kickback**: en vez de que el oráculo escriba $f(x)$ en un registro separado, la información de $f(x)$ se transfiere como una fase global sobre el primer registro.

$$U_f|x\rangle|-\rangle = (-1)^{f(x)}|x\rangle|-\rangle$$

## Derivación para $n$ qubits

$$|0\rangle^{\otimes n}|-\rangle \xrightarrow{H^{\otimes n}} \frac{1}{\sqrt{2^n}}\sum_x|x\rangle|-\rangle \xrightarrow{U_f} \frac{1}{\sqrt{2^n}}\sum_x(-1)^{f(x)}|x\rangle|-\rangle$$

Aplicando $H^{\otimes n}$ al primer registro y midiendo, la probabilidad de obtener $0^n$ es:

$$P(0^n)=\left|\frac{1}{2^n}\sum_x(-1)^{f(x)}\right|^2$$

## Los dos casos prometidos

- **Constante:** todos los términos suman con el mismo signo → $P(0^n)=1$, determinista.
- **Balanceada:** la mitad de los signos son $+1$ y la mitad $-1$ → la suma es exactamente $0$ → $P(0^n)=0$, determinista (nunca se mide $0^n$).

Esta es la diferencia clave con la versión original de 1985: acá la distinción es **perfectamente determinista** (100% vs. 0%), no probabilística (100% vs. 50%) — ver `deutsch-original.md`.

## Qué pasa fuera de la promesa

Ver `caso-sin-promesa.md`: la misma fórmula $P(0^n)=\left|\frac{1}{2^n}\sum_x(-1)^{f(x)}\right|^2$ sigue siendo válida incluso si $f$ no es ni constante ni balanceada — solo deja de dar 0 o 1 exactos.
