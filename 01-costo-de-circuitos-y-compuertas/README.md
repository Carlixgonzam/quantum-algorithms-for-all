# 01 — Costo de circuitos y conjuntos de compuertas

Acá vive todo lo que tiene que ver con "qué tan caro es realmente este circuito" — desde contar size y depth en un diagrama, hasta construir un circuito reversible a partir de cualquier circuito booleano clásico, hasta entender qué significa que un conjunto de compuertas sea *universal*.

## Contenido

- **`tamano-y-profundidad.md`** — cómo contar size (número total de puertas) y depth (camino más largo de dependencias) sin caer en la trampa de confundir "columnas visuales" del diagrama con dependencias reales entre qubits. Incluye el método de scheduling por capas.

- **`conjuntos-universales-de-compuertas.md`** — por qué universalidad es una propiedad *estructural*, no una propiedad de compuertas específicas. No hace falta CNOT en particular (CZ, iSWAP o controlled-S sirven igual), y no hace falta ninguna compuerta de tres qubits.

- **`simulacion-de-circuitos-booleanos.md`** — el truco estándar para convertir AND/OR/FANOUT (no reversibles) en versiones reversibles: un único qubit de trabajo por puerta, no dos. Esto da un circuito cuántico de tamaño *lineal* en el tamaño del circuito booleano original, no cuadrático.

- **`ejercicios/`** — banco de problemas de este tema.

## La idea que conecta todo el módulo

Reversibilidad no es gratis — se paga con espacio extra (qubits auxiliares), no con tiempo extra ni con pérdida de información. Esa es la misma idea detrás de por qué Grover puede correr "sobre cualquier función para la que se conozca un circuito booleano": esta técnica de simulación lineal es el puente entre cualquier función clásica y un oráculo cuántico unitario utilizable.
