# Costo de circuitos y compuertas

## Problema 1 — Tamaño y profundidad de un circuito

**Enunciado.** Circuito de 5 qubits con: H en q0,q1,q2; un CNOT(q0→q4); T en q0; CNOT(q1→q2); Y en q3; CNOT(q3→q2); Z en q1; CNOT(q4→q2). ¿Size y depth?

**Tamaño:** se cuentan todas las puertas sin importar el qubit → **10**.

**Profundidad:** no es lo mismo que "columnas visuales" del diagrama — hay que rastrear, por cada qubit, en qué capa quedó disponible después de su última puerta, y asignar cada nueva puerta a `max(capas de sus qubits) + 1`.

| Capa | Puertas |
|---|---|
| 1 | H(q0), H(q1), H(q2), Y(q3) |
| 2 | CNOT(q0→q4), CNOT(q1→q2) |
| 3 | T(q0), CNOT(q3→q2), Z(q1) |
| 4 | CNOT(q4→q2) |

**Respuesta: size = 10, depth = 4.**

*Intuición:* el último CNOT depende de q4 (usado en la capa 2) y de q2 (usado en la capa 3) — por eso necesita su propia capa 4, aunque visualmente pudiera parecer alineado con otras puertas.

---

## Problema 2 — Simulación cuántica de circuitos booleanos

**Enunciado.** ¿Cómo se simula un circuito booleano clásico con un circuito cuántico?

**Respuesta:** se usa **un único qubit de trabajo** (inicializado en $|0\rangle$) por cada puerta AND, OR o FANOUT del circuito booleano (NOT no necesita qubit extra, ya es reversible). Con esto, el tamaño del circuito cuántico resultante crece **linealmente** en el tamaño del circuito booleano original.

*Intuición:* la reversibilidad se paga con espacio (qubits auxiliares), no con tiempo extra ni pérdida de información — es la misma idea que permite correr Grover sobre cualquier función con un circuito booleano conocido.

---

## Problema 3 — Afirmaciones verdaderas sobre eficiencia y costo computacional

**Enunciado.** ¿Cuáles de estas afirmaciones son verdaderas?

- *Suma de enteros en binario escala linealmente con el tamaño* → **Verdadera** ($O(n)$).
- *Una operación elemental involucra pocos bits/qubits y se hace rápido (ej. OR de dos bits)* → **Verdadera**, es la definición estándar.
- *Formalmente se asume un esquema de codificación fijo, pero en la práctica no importa cuál* → **Verdadera** (esquemas razonables son polinomialmente equivalentes).
- *El algoritmo "power" (exponenciación modular) tiene costo cuadrático* → **Falsa**: son $O(n)$ multiplicaciones de costo $O(n^2)$ cada una → $O(n^3)$, cúbico.
- *Encontrar un algoritmo polinomial es el paso final en términos de eficiencia* → **Falsa**: el grado del polinomio y las constantes siguen importando muchísimo en la práctica.
- *No existe algoritmo clásico eficiente para el GCD* → **Falsa**: el algoritmo de Euclides es eficiente ($O(n^2)$) desde hace más de 2000 años.

*Intuición:* esta es la misma razón por la que el paso final de Shor (calcular el gcd) es trivial — toda la dificultad de factorizar recae en encontrar el orden $r$, no en el GCD.

---

## Problema 4 — Conjuntos universales de compuertas

**Enunciado.** ¿Cuáles afirmaciones sobre conjuntos universales son verdaderas?

- *Existen infinitos conjuntos universales distintos* → **Verdadera**.
- *$\{H, T, \text{controlled-}S\}$ es universal* → **Verdadera**: $\text{CS}^2 = \text{CZ}$ (porque $S^2=Z$), y $\text{CZ}$ se convierte en CNOT con Hadamards, así que este conjunto genera $\{H,T,\text{CNOT}\}$, que ya se sabe universal.
- *Todo conjunto universal necesita una compuerta de 3 qubits* → **Falsa**: $\{H,T,\text{CNOT}\}$ usa solo 1 y 2 qubits.
- *Todo conjunto universal necesita específicamente CNOT* → **Falsa**: CZ, iSWAP, controlled-S, etc. sirven igual.
- *Dado un conjunto universal, se puede aproximar cualquier compuerta (ej. T) con precisión arbitraria* → **Verdadera**, es la definición misma de universalidad (teorema de Solovay-Kitaev).

*Intuición:* universalidad es una propiedad **estructural** — necesitás suficiente entrelazamiento de 2 qubits combinado con suficiente diversidad de rotaciones de 1 qubit para escapar del grupo de Clifford, no compuertas específicas.
