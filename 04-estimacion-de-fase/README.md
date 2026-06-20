# 04 — Estimación de fase

El bloque de construcción detrás de Shor (y de buena parte de los algoritmos cuánticos "serios"). La idea completa cabe en una sola intuición: **el qubit de control nunca mide $U$ directamente — mide la fase relativa que $U$ le imprime a uno de sus eigenvectores**.

## Contenido

- **`circuito-y-costo.md`** — las cuatro partes del circuito de estimación de fase (Hadamards sobre $m$ qubits de control, operaciones controladas-$U$, transformada cuántica de Fourier inversa, mediciones) y por qué solo el costo de la $U$ controlada depende del problema concreto que se esté resolviendo — las otras tres partes tienen costo fijo en función de $m$.

- **`eigenvectores-y-fase.md`** — cómo usar fase estimation con un solo qubit de control para distinguir entre dos posibles operadores ($\mathbb{I}$ vs. $H$, por ejemplo), eligiendo el estado de entrada que sea eigenvector de ambos con eigenvalores distintos. Pista clave: si el estado de entrada no es eigenvector compartido de ambas opciones candidatas, el resultado deja de ser determinista.

- **`ejercicios/`** — banco de problemas de este tema.
