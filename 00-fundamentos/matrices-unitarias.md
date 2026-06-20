# Matrices unitarias: eigenvalores y eigenvectores

## Lo esencial

Una matriz $U$ es unitaria si $U^\dagger U = UU^\dagger = I$. Esto la hace **normal**, y por el teorema espectral, toda matriz normal es diagonalizable con una **base ortonormal de eigenvectores**.

Sus eigenvalores tienen la forma:

$$\lambda = e^{i\theta} = \cos\theta + i\sin\theta, \quad \theta\in[0,2\pi)$$

**Punto que se presta a confusión:** el eigenvalor $\lambda$ es un número complejo — no es real, salvo en los casos especiales $\theta=0$ ($\lambda=1$) o $\theta=\pi$ ($\lambda=-1$). Lo que sí es real y vive en $[0,2\pi)$ es el ángulo $\theta$, no $\lambda$ mismo. Confundir el eigenvalor con su fase es el error más común en este tema.

## Consecuencias útiles

- Si todos los eigenvalores de $U$ son $1$, entonces $U=I$ (porque $U=VDV^\dagger$ con $D=I$).
- Si los únicos eigenvalores de $U$ son $\pm1$ (reales), entonces $U$ es necesariamente **Hermitiana**: como $U$ es normal y tiene eigenvalores reales, $U^\dagger=U$.
- Los eigenvalores siempre viven en el **círculo unitario** del plano complejo — esta es justamente la condición $|\lambda|=1$ que define a las matrices unitarias.

## Por qué importa para todo lo demás

Cada compuerta cuántica es una matriz unitaria, así que esta estructura algebraica (eigenvalores en el círculo unitario, base ortonormal garantizada) es lo que hace posible toda la maquinaria de estimación de fase: cuando $U|\psi\rangle=\lambda|\psi\rangle$, podemos "leer" $\lambda$ a través de la fase relativa que acumula un qubit de control — ver `04-estimacion-de-fase/eigenvectores-y-fase.md`.

Ver también: `banco-de-problemas/fundamentos-y-otros-circuitos.md` (Problema 1).
