# 00 — Fundamentos

Antes de hablar de algoritmos hay que tener clara la maquinaria de fondo: qubits, compuertas, medición, y por qué *todo* lo que hace una computadora cuántica tiene que ser reversible (unitario). Acá quedan las dos piezas que más se dan por sentadas y que en realidad esconden buena parte de la intuición de todo lo que viene después.

## Contenido

- **`matrices-unitarias.md`** — por qué los eigenvalores de una matriz unitaria viven en el círculo unitario (y son números *complejos*, no reales, aunque el ángulo de fase sí sea real); por qué toda matriz unitaria es diagonalizable con base ortonormal de eigenvectores; qué implica que una matriz normal tenga eigenvalores reales.

- **`modelo-de-consultas.md`** — la abstracción que permite comparar algoritmos cuánticos y clásicos contando *consultas* a un oráculo, ignorando deliberadamente cuánto cuesta construir ese oráculo por dentro. Esto es a la vez la mayor fortaleza del modelo (separa la pregunta teórica de la implementación) y su mayor limitación práctica (no siempre refleja problemas reales).

## La idea que conecta todo el módulo

Casi todos los algoritmos que vienen después —Deutsch-Jozsa, Simon, Grover, estimación de fase— dependen de que las operaciones involucradas sean unitarias. Entender *por qué* una matriz tiene que ser unitaria para ser una compuerta cuántica válida (conserva norma, es invertible, sus eigenvalores son fases puras) es la base de todo lo demás.
