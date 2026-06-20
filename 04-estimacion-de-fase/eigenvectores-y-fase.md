# Eigenvectores y fase: identificar una compuerta desconocida

## La idea central

El qubit de control en un circuito de estimación de fase **nunca mide $U$ directamente** — mide la fase relativa que $U$ le imprime a un eigenvector específico. Si el estado de entrada no es eigenvector de $U$, el resultado de la medición deja de ser determinista.

## Derivación general

Con un solo qubit de control y $|\psi\rangle$ eigenvector de $U$ con eigenvalor $\lambda$ (es decir $U|\psi\rangle=\lambda|\psi\rangle$), el circuito H–controlled-$U$–H deja al qubit de control en:

$$\frac12\big[(1+\lambda)|0\rangle+(1-\lambda)|1\rangle\big]$$

## Ejemplo trabajado: ¿$U=\mathbb I$ o $U=H$?

Para que la medición sea $0$ con $U=\mathbb I$ y $1$ con $U=H$, **ambos con probabilidad 1**, necesito que $|\psi\rangle$ sea eigenvector de **ambas** opciones:

- Con $U=\mathbb I$: cualquier estado es eigenvector con $\lambda=1$ → da medición 0 automáticamente, sin condición extra sobre $|\psi\rangle$.
- Con $U=H$: necesito medición = 1 con certeza, es decir $\lambda=-1$.

Los eigenvectores de $H$ están en los ángulos $\pi/8$ (eigenvalor $+1$) y $5\pi/8$ (eigenvalor $-1$) de la esfera de Bloch:

$$|\psi\rangle=\cos(5\pi/8)|0\rangle+\sin(5\pi/8)|1\rangle$$

## La pista que casi siempre da la clave

Si una pregunta pide encontrar un estado que produzca un resultado determinista para dos (o más) operadores candidatos distintos, la condición casi siempre es: **buscar un eigenvector compartido con eigenvalores distintos** entre los candidatos. Si el estado propuesto no cumple eso para alguno de los casos, el resultado en ese caso no será determinista.

Ver `banco-de-problemas/estimacion-de-fase-y-shor.md` (Problema 2).
