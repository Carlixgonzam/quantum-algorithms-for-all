# El circuito de estimación de fase y su costo

## Las cuatro partes

Con $m$ qubits de control y $U$ una unitaria de $n$ qubits:

1. **Hadamards** sobre los $m$ qubits de control → costo $O(m)$.
2. **Operaciones $U$ controladas** ($U, U^2, U^4,\ldots,U^{2^{m-1}}$) → **el costo depende completamente de qué es $U$**, no hay cota fija en términos de $n$ sin más información.
3. **Transformada cuántica de Fourier inversa** sobre los $m$ qubits de control → costo $O(m^2)$.
4. **Mediciones** sobre los $m$ qubits de control → costo $O(m)$.

## Por qué la parte 2 es distinta de las otras tres

Las partes 1, 3 y 4 tienen costo fijo en función de $m$ — un parámetro que **elegimos libremente** según la precisión que queramos. No dependen de la estructura del problema.

La parte 2, en cambio, hereda toda la dificultad del problema concreto que se esté resolviendo. Si $U$ es una compuerta simple, el costo es bajo. Si $U$ es una operación compleja y arbitraria, puede no haber forma eficiente de implementarla — y la estimación de fase, como marco general, no resuelve ese problema, simplemente lo hereda.

## Por qué esto importa para entender Shor

Esto explica directamente por qué Shor funciona: la "magia" de Shor no está en el marco de estimación de fase en sí (que es genérico), sino en que la multiplicación modular **sí** admite una implementación eficiente como $U$ controlada. Sin esa estructura específica, la estimación de fase por sí sola no garantiza nada sobre el costo total del algoritmo.

Ver `banco-de-problemas/estimacion-de-fase-y-shor.md` (Problema 3).
